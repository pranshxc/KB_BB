---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-16_unauthenticated-remote-command-execution-in-multiple-wago-products.md
original_filename: 2023-05-16_unauthenticated-remote-command-execution-in-multiple-wago-products.md
title: Unauthenticated Remote Command Execution in Multiple WAGO Products
category: documents
detected_topics:
- command-injection
- automation-abuse
- supply-chain
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- supply-chain
- api-security
language: en
raw_sha256: 1c68566324cff0a5719609908ae5d129453b5de577f8cf833ac77894fec5f4bf
text_sha256: 48df2d89845d989b9e445c94dea608b2d5da935bc5f74184004ccf27e66116f0
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthenticated Remote Command Execution in Multiple WAGO Products

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-16_unauthenticated-remote-command-execution-in-multiple-wago-products.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, supply-chain, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `1c68566324cff0a5719609908ae5d129453b5de577f8cf833ac77894fec5f4bf`
- Text SHA256: `48df2d89845d989b9e445c94dea608b2d5da935bc5f74184004ccf27e66116f0`


## Content

---
title: "Unauthenticated Remote Command Execution in Multiple WAGO Products"
page_title: "Security Advisory: Unauthenticated Remote Command Execution in Multiple WAGO Products | ONEKEY Research | Research | ONEKEY"
url: "https://onekey.com/blog/security-advisory-wago-unauthenticated-remote-command-execution/"
final_url: "https://www.onekey.com/resource/security-advisory-wago-unauthenticated-remote-command-execution"
authors: ["Quentin Kaiser (@QKaiser)"]
programs: ["WAGO"]
bugs: ["RCE", "OS command injection", "Security code review"]
publication_date: "2023-05-16"
added_date: "2023-05-18"
source: "pentester.land/writeups.json"
original_index: 1150
---

[Resources](/resources)

>

[Research](/resources/research)

>

Security Advisory: Unauthenticated Remote Command Execution in Multiple WAGO Products

# Security Advisory: Unauthenticated Remote Command Execution in Multiple WAGO Products

![Security Advisory: Unauthenticated Remote Command Execution in Multiple WAGO Products](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b823defca5c977d2f7034_6712ae6a06a43383a9a0a6f2_08.jpeg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

May 15, 2023

4

min read

TablE of contents

Example H2

## READY TO UPGRADE YOUR RISK MANAGEMENT?

Make cybersecurity and compliance efficient and effective with ONEKEY.

[See it in Action](/book-a-demo)

## Introduction

As we already demonstrated through our recent advisories ([Asus M25 NAS](https://b1eyc.myrdbx.io/blog/security-advisory-asus-m25-nas-vulnerability/), [Phoenix Contact](https://b1eyc.myrdbx.io/blog/security-advisory-multiple-vulnerabilities-in-phoenix-contact-routers/), [NetModule,](https://b1eyc.myrdbx.io/blog/security-advisory-netmodule-multiple-vulnerabilities/) and [Festo](https://b1eyc.myrdbx.io/blog/advisory-festo-cecc-x-m1-command-injection-vulnerabilities/)) our "zero day identification" module is quite versatile when it comes to finding bugs in PHP, Lua, or Python code we find in firmware uploaded to ONEKEY's platform. However, we recently discovered that we were missing an interesting source for PHP taint analysis: [PHP wrappers](https://www.php.net/manual/en/wrappers.php).

PHP comes with many built-in wrappers for various URL-style protocols for use with the filesystem functions such as _fopen()_ , _copy()_ , _file_exists()_ and _filesize()_. They are sometimes used to read the content of HTTP requests or command line arguments by using `php://input`, `php://stdin`, or `php://fd/0` (ok the last one is a bit far fetched and came up when we discussed potential sources for the taint analysis, but you get the point :) ).

We recently added these wrappers as a source and scanned some sample firmware images. Within the scan results was an unauthenticated command injection affecting [WAGO Series PFC100](https://www.wago.com/global/automation-technology/discover-plcs/pfc100) web interface. 

We immediately confirmed our findings on a real device (we got one since the latest advisory) and reported the issue to WAGO. They were extremely fast in responding and fixing the vulnerability (around 45 days from reporting to patch release). Hats off to them and CERT@VDE.

## Unauthenticated Remote Command Execution

**Affected vendor & product** | 

  * Series WAGO PFC100 (750-81xx/xxx-xxx)
  * Series WAGO PFC200 (750-82xx/xxx-xxx)
  * WAGO Compact Controller CC100 (751-9301)
  * WAGO Edge Controller (752-8303/8000-002)
  * Series WAGO Touch Panel 600 Standard Line (762-4xxx)
  * Series WAGO Touch Panel 600 Advanced Line (762-5xxx)
  * Series WAGO Touch Panel 600 Marine Line (762-6xxx)

  
---|---  
**Vendor Advisory** | <https://cert.vde.com/de/advisories/VDE-2023-007/>  
**Vulnerable version** | Firmware versions >= 16 and <= 23.  
**Fixed version** | Affected users users must install FW22 Patch 1 or FW24 depending on the affected device. Refer to vendor advisory for more information.  
**CVE IDs** | [CVE-2023-1698](https://nvd.nist.gov/vuln/detail/CVE-2023-1698)  
**Impact (CVSS)** | 9.8 (critical) ([AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N&version=3.1))  
**Credit** | Q. Kaiser, ONEKEY Research Lab  
Research supported by [Certainity](https://www.certainity.com/)  
  
## Summary

The “legal information” plugin of WAGO web-based-management interface contains a command injection vulnerability allowing for the execution of arbitrary commands with privileges of the user `www`.

## Impact

A successful exploit allows an attacker to create new users and change the device configuration, which can result in unintended behavior, denial of service, and full system compromise.

## Description

The WAGO web admin interface has a "legal information" features where users can list open source licenses of third party software used by WAGO. This is required to comply with those software licenses.

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8b8ff920cc0571435ff8_image-2-1024x621.png)

The vulnerability is present in PHP code located at `/var/www/wbm/plugins/wbm-legal-information/platform/pfcXXX/licenses.php`.

Below we see that a `$packageId` variable is read from the JSON structure received in the HTTP body through the use of the PHP wrapper `php://input`.

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8b8ff920cc0571435ff5_image-1024x395.png)

Next, on line 19, the `$packageId` variable is used in a `shell_exec` call without prior sanitization, leading to unauthenticated arbitrary command injection.

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8b8ff920cc0571435ff0_image-1-1024x456.png)

By sending the request below, an attacker would make the device execute the command `id`:
  
  
  curl -s -k -X POST --data '{"package":";id;#"}' https://ip.of.device/wbm/plugins/wbm-legal-information/platform/pfcXXX/licenses.php | jq
  {
  "package": {
  "id": ";id;#",
  "name": ";id;#",
  "version": null
  },
  "license": "uid=1000(www) gid=1000(www)\n"
  }

## Key Takeaways

This vulnerability serves as an example that static analysis tools needs constant care so as not to miss potential issues. We strive to continuously improve our zero-day identification module by identifying what we are potentially missing both in bug classes, and in ways that these can be exploited.

It's also interesting to note that the vulnerability affects a rather uninteresting feature of the product that rather looks static when you don't have access to the code. I know it would not have been my prime focus as a pentester.

## Timeline

**2023-03-29** – Sent coordinated disclosure request to [psirt@wago.com](mailto:psirt@wago.com)

**2023-03-29** – Answer from WAGO PSIRT (Product Security Incident Response Team), establishment of secure communication channel.

**2023-03-30** – WAGO PSIRT provides us with CVE (Common Vulnerabilities and Exposures) ID and CVSS (Common Vulnerability Scoring System) score, start coordination with CERT@VDE 

**2023-04-27** – WAGO PSIRT shares draft advisory with us and CERT@VDE 

**2023-05-15** – CERT@VDE releases WAGO advisory 

**2023-05-16** – ONEKEY releases its advisory

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
