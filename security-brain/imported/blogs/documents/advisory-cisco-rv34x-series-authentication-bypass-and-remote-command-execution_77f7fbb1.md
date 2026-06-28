---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-13_advisory-cisco-rv34x-series-authentication-bypass-and-remote-command-execution.md
original_filename: 2021-04-13_advisory-cisco-rv34x-series-authentication-bypass-and-remote-command-execution.md
title: 'Advisory: Cisco RV34X Series – Authentication Bypass and Remote Command Execution'
category: documents
detected_topics:
- command-injection
- access-control
- mfa
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- access-control
- mfa
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 77f7fbb16f8ed4818b00e0e670f94150f1164a71db3fb368d29a3681dac0a985
text_sha256: 8d1e5d33297b6592ca81fa0773c5fe70b0cbe610c3fd15a314c5b4f8e56275c5
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Advisory: Cisco RV34X Series – Authentication Bypass and Remote Command Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-13_advisory-cisco-rv34x-series-authentication-bypass-and-remote-command-execution.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, mfa, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `77f7fbb16f8ed4818b00e0e670f94150f1164a71db3fb368d29a3681dac0a985`
- Text SHA256: `8d1e5d33297b6592ca81fa0773c5fe70b0cbe610c3fd15a314c5b4f8e56275c5`


## Content

---
title: "Advisory: Cisco RV34X Series – Authentication Bypass and Remote Command Execution"
page_title: "Advisory: Cisco RV34X Series - Authentication Bypass and Remote Command Execution | ONEKEY Research | Research | ONEKEY"
url: "https://onekey.com/blog/advisory-cisco-rv34x-authentication-bypass-remote-command-execution/"
final_url: "https://www.onekey.com/resource/advisory-cisco-rv34x-authentication-bypass-remote-command-execution"
authors: ["T. Shiomitsu"]
programs: ["Cisco"]
bugs: ["Authentication bypass", "OS command injection", "RCE"]
publication_date: "2021-04-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3744
---

[Resources](/resources)

>

[Research](/resources/research)

>

Advisory: Cisco RV34X Series - Authentication Bypass and Remote Command Execution

# Advisory: Cisco RV34X Series - Authentication Bypass and Remote Command Execution

![Advisory: Cisco RV34X Series - Authentication Bypass and Remote Command Execution](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8228097c5aad5c0c0b49_6712aea448102fa67cb3117a_15.jpeg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

April 12, 2021

5

min read

TablE of contents

Example H2

## READY TO UPGRADE YOUR RISK MANAGEMENT?

Make cybersecurity and compliance efficient and effective with ONEKEY.

[See it in Action](/book-a-demo)

## **TLDR**

In early 2021, we reported a few security issues to Cisco related to their RV34X series of routers, two of which have been recently patched. The issues in question were an authentication bypass and system command injection, both in the web management interface. These can be chained together to achieve unauthenticated command execution. Cisco [has released an advisory](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sb-rv-bypass-inject-Rbhgvfdx), and assigned CVE IDs as follows: 

  * RV34X /upload Authorization Bypass Vulnerability (CVE-2021-1472)
  * RV34X OS Command injection in Cookie string (CVE-2021-1473)

The issues have been fixed in firmware version 1.0.03.21 in the RV34X series. Cisco has noted that the RV26X and RV16X series are also affected by the authentication bypass issue, and has released firmware version 1.0.01.03 to address this. This post contains a root cause analysis for these bugs. Enjoy! [caption id="attachment_4060" align="aligncenter" width="719"]![Cisco RV340](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8bb6c2cafebeb233e0eb_routers-rv340.jpeg) © Cisco[/caption]  Affected vendor & product | Cisco Small Business RV Series Router ([www.cisco.com](https://www.cisco.com/))  
---|---  
Vulnerable version | RV34X 1.0.3.20 & below, RV16X/RV26X 1.0.01.02 & below.  
Fixed version | RV34X series: [1.0.03.21](https://software.cisco.com/download/home/286287791/type/282465789/release/1.0.03.21). RV16X/RV26X: 1.0.01.03.  
CVE IDs | CVE-2021-1472, CVE-2021-1473  
Impact | 5.3 (medium) [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?calculator&version=3.1&vector=\(AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N\)) 8.8 (high) [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?calculator&version=3.1&vector=\(AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L\))  
Credit | T. Shiomitsu, IoT Inspector Research Lab  
  
## **RV34X/RV26X/RV16X /upload Authorization Bypass Vulnerability (CVE-2021-****1472****)**

While Cisco has noted that this issue affects other devices, I'll only go over the specifics of how it affects the RV34X series here. On RV34X devices, the web management interface is served by `nginx` on port 443. `nginx` is configured (by files in `/etc/nginx/`) so that requests made to the URIs `/upload`, `/form-file-upload` and `/api/operations/ciscosb-file:form-file-upload` are all passed to a CGI binary called `upload.cgi`. Depending on which URI is requested, the behavior of `upload.cgi` is slightly different. In firmware revisions earlier than 1.0.3.20, there was no real attempt to restrict access to these `upload.cgi`-related endpoints. In fact, a set of command injection issues from late 2020 affecting the RV34X series were initially disclosed as post-authentication issues but later revised to reflect the fact that these could be exploited pre-authentication (after a very charitable and publicly-uncredited researcher - cough cough - tipped off the Cisco PSIRT). These were tracked by the ZDI as [ZDI-20-1100](https://www.zerodayinitiative.com/advisories/ZDI-20-1100/) and [ZDI-20-1101](https://www.zerodayinitiative.com/advisories/ZDI-20-1101/), and you can see the [Cisco advisory here](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-rv-osinj-rce-pwTkPCJv). While the ZDI advisories have not been updated and still show the initial lower CVSS rating – the Cisco advisory and CVSS scores have been updated to reflect the pre-authentication nature of the bugs. In 1.0.03.20, an authentication check was implemented. This was written into `nginx` configuration, which you can see here: ![Auth Bypass Nginx Conf Crop](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8bd338f52dbe9c4aa4e1_auth_bypass_nginx_conf_crop.png) The attempt here appears to be to check that some `Authorization` header is set, and/or that a file exists in the `/tmp/websession/token/` folder with the same name as the request `sessionid` cookie. Then a user is assumed to be authorized. Unfortunately, there’s a fatal flaw in this fix. The logic is such that **any non-null****`Authorization` ****header** would set `$deny` to “0”. So, sending literally  _any_ valid-looking `Authorization` header as part of a request to `/upload` will bypass the authorization check. 

## **RV34X OS Command injection in Cookie string (CVE-2021-****1473****)**

Once we have bypassed authentication, it’s then possible to interact directly with the `/upload` endpoint. Requests made to this endpoint are passed directly to the `upload.cgi` binary by the `nginx``uwsgi` CGI configuration. Within the `main()` function in `upload.cgi`, the `HTTP_COOKIE` environmental variable is read, and the value from the `sessionid` cookie is extracted using a simple series of `strtok_r` and `strstr`. This specific `sessionid`-reading logic is notable because, due to the `strtok_r` call, it’s not possible to use “;” characters in any injection, as it will prematurely terminate the injection string. In pseudocode, it looks like this: 
  
  
  if (HTTP_COOKIE != (char *)0x0) { 
  StrBufSetStr(cookie,HTTP_COOKIE); 
  cookie = StrBufToStr(cookie); 
  cookie = strtok_r(cookie, ";", &saveptr); 
  while (cookie != 0x0) { 
  cookie = strstr(cookie, "sessionid="); 
  if (cookie != 0x0) { 
  sessionid_cookie_value = pathparam_ + 10; 
  } 
  } 
  }

Because our HTTP request is made to the `/upload` URI, the `main()` function in `upload.cgi` calls a function at `000124a4`, which I’ve named `handle_upload()`. This function takes a pointer to the `sessionid` cookie value as its first argument. `void handle_upload(char *sessionId, char *destination, char *option, char *pathparam, char *fileparam, char *cert_name, char *cert_type, char *password) ` It also takes several other arguments, each of which are populated by the multipart request parsing that takes place in the `main()` function. The names I’ve given these arguments roughly align with the names of the parameters that this multipart ingesting logic looks for. 

> Depending on what string is passed as the `pathparam` parameter, slightly different code paths will be taken, which means that slightly different checks must be bypassed to be able to reach the vulnerable code. In this example, I am using a request with the `pathparam` set to “Configuration”, so the pseudocode I'm showing reflects this.

Within `handle_upload()`, a `curl` command is constructed with a call to `sprintf`, the resulting buffer of which is then passed directly to `popen`: 
  
  
  ret = strcmp(pathparam, "Configuration"); 
  if (ret == 0) { 
  config_json = upload_Configuration_json(destination,fileparam); 
  if (config_json != 0) { 
  post_data = json_object_to_json_string(config_json); 
  sprintf(command_buf, "curl %s --cookie \'sessionid=%s\' -X POST -H \'Content-Type: application/json\' -d\'%s\' ", jsonrpc_cgi, sessionId , post_data); 
  debug("curl_cmd=%s",command_buf); 
  __stream = popen(command_buf, "r"); 
  if (__stream != (FILE *)0x0) { 
  [...snip...] 
  }

The `sessionid` cookie value that we have passed in our request is passed directly into this `sprintf()` call. With a crafted `sessionid` value, we would therefore be able to inject arbitrary commands into this command buffer. This will run the command with the privileges of the `upload.cgi` binary which, in this case, is `www-data`. 

## **Key Takeaways**

Logic bugs can be quite easy to introduce, and sometimes tricky to identify. Authentication can be difficult to implement well, especially when multiple authorization methods might be accepted. As higher-end embedded devices start to use more common server software components (for purposes they were not necessarily intended for), there are often more layers of complexity introduced - thicker web servers requiring more precise configuration, CGI binaries, middleware gluing things together. Each layer introduces opportunities for mis-configuration, which could lead to security issues. [![Copy Of Ads 480 120](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8236692550f5d60746d6_Copy-of-Ads-480_120.png)](https://www.iot-inspector.com/demo/)

## **Timeline**

_2021-01-02_ : Initial disclosure made to Cisco PSIRT. _2021-01-07_ : Confirmation of receipt of disclosure from Cisco PSIRT. _2021-01-27_ : Confirmation that issue is valid from Cisco PSIRT. _2021-02-12_ : Update from Cisco PSIRT. _2021-03-23_ : We contact Cisco PSIRT for timeline update and CVE IDs. _2021-03-23_ : Cisco PSIRT respond giving us timeline and CVE IDs. _2021-04-07_ : Cisco release advisory.

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
