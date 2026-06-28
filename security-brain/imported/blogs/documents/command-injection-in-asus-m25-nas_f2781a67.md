---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-01_command-injection-in-asus-m25-nas.md
original_filename: 2022-12-01_command-injection-in-asus-m25-nas.md
title: Command Injection in Asus M25 NAS
category: documents
detected_topics:
- command-injection
- sqli
- path-traversal
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- sqli
- path-traversal
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: f2781a6781b1f5ff6da6331c27e30d390fc3732520e232b5872e9f62d78e5015
text_sha256: 7602f46bfcc667deeac05464967badb4c785e4c7e8ef03b9b86b9b171fe00c8e
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Command Injection in Asus M25 NAS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-01_command-injection-in-asus-m25-nas.md
- Source Type: markdown
- Detected Topics: command-injection, sqli, path-traversal, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `f2781a6781b1f5ff6da6331c27e30d390fc3732520e232b5872e9f62d78e5015`
- Text SHA256: `7602f46bfcc667deeac05464967badb4c785e4c7e8ef03b9b86b9b171fe00c8e`


## Content

---
title: "Command Injection in Asus M25 NAS"
page_title: "Security Advisory: Asus M25 NAS Vulnerability | ONEKEY Research | Research | ONEKEY"
url: "https://onekey.com/blog/security-advisory-asus-m25-nas-vulnerability/"
final_url: "https://www.onekey.com/resource/security-advisory-asus-m25-nas-vulnerability"
authors: ["Quentin Kaiser (@QKaiser)"]
programs: ["Asus"]
bugs: ["OS command injection", "Source code disclosure"]
publication_date: "2022-12-01"
added_date: "2022-12-20"
source: "pentester.land/writeups.json"
original_index: 1830
---

[Resources](/resources)

>

[Research](/resources/research)

>

Security Advisory: Asus M25 NAS Vulnerability

# Security Advisory: Asus M25 NAS Vulnerability

![Security Advisory: Asus M25 NAS Vulnerability](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b824787fa1cccd32089b4_6712ae63f045700b98904967_07.jpeg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

November 30, 2022

4

min read

TablE of contents

Example H2

## READY TO UPGRADE YOUR RISK MANAGEMENT?

Make cybersecurity and compliance efficient and effective with ONEKEY.

[See it in Action](/book-a-demo)

## Introduction

We recently deployed the first component of our "zero-day identification" module, which aimed at identifying vulnerability patterns in scripting languages. It's been a long time coming and we want to share a few technical details about it with you.

Our objective is to support identification of vulnerability patterns in both scripting languages and compiled binaries. We started off with scripting languages as it seemed to be the easiest path to get results fast. Our first order of business was to identify the distribution of scripting languages within our corpus based off our file categorization. These statistics guided us in choosing which languages to support first.

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8bbb38084bb808ba3432_image-1.png)

Given what we observed, we chose to focus on two languages: Python and PHP. JavaScript is well represented too but it's mostly observed in client-side web administration interfaces code, which is not that interesting to an attacker. Shell scripts and Lua code will probably be the next ones to be supported.

## Static Code Analysis

To identify vulnerabilities, we perform taint analysis by reconstructing the abstract syntax tree and we then traverse this tree. With this approach, we can dramatically increase accuracy of the results and assure that user-controlled input is actually being processed in an insecure way, reducing the overall number of false-positives reported. At the moment, we look for the following vulnerability classes:

  * arbitrary command injection ([CWE-77](https://cwe.mitre.org/data/definitions/77.html))
  * path traversal ([CWE-23](https://cwe.mitre.org/data/definitions/23.html))
  * SQL injection ([CWE-89](https://cwe.mitre.org/data/definitions/89.html))
  * insecure communications ([CWE-319](https://cwe.mitre.org/data/definitions/319.html) / [CWE-923](https://cwe.mitre.org/data/definitions/923.html))
  * weak cryptographic ciphers / hashing algorithms usage ([CWE-327](https://cwe.mitre.org/data/definitions/327.html))
  * loose equality ([CWE-697](https://cwe.mitre.org/data/definitions/697.html))
  * unsafe deserialization ([CWE-502](https://cwe.mitre.org/data/definitions/502.html))

Before deploying the PHP static code analysis checker, we tested it with hundreds of selected sample firmware images and reviewed the results. This led to the discovery of around 15 critical bugs spanning 6 different vendors. All these bugs were reported to affected vendors and are in the process of being fixed.

Except this one.

This one is special because it affects a NAS device from Asus, which according to them "_has been EOL for years_ ", with the latest firmware version dating back 10 years. Since there's no fix in sight, we don't have to wait for the 90 days and can publish the interesting details.

With this analysis module only being the first step and active research being conducted in the area of automated detection of potential 0-day vulnerabilities, you may expect a constant stream of technical advisories about bugs we already identified and ones we still have to uncover.

Now onto the advisory !

## Arbitrary Command Injection Through Cookies

A command injection bug was identified during our scan campaign, so we downloaded the sample and validated the automated results manually.

**Affected vendor & product** | Asus M25 NAS  
---|---  
**Vendor Advisory** | NONE  
**Vulnerable version** | All versions  
**Fixed version** | None  
**CVE IDs** | [CVE-2022-4221](https://www.cve.org/CVERecord?id=CVE-2022-4221)  
**Impact** | 9.8 (Critical) [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)  
**Credit** | Q. Kaiser, ONEKEY Research Lab  
Research supported by [Certainity](https://www.certainity.com/)  
  
This bug is probably the easiest one we had to deal with. As we can see in the screenshot below, a cookie value is used unsanitized in a call to `exec()`. By adding a semi-colon followed by any kind of arbitrary command, we can inject commands. The code is reachable unauthenticated.

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8bbc38084bb808ba3593_nas_m25_rce_cookie-1024x579.png)

The interesting part here is that Asus copied this file from AjaXplorer, an open-source project, but inserted the command injection bug by trying to add some authentication layer (code between "`ALPHA_CUSTOMIZE`" comment).

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8bbb38084bb808ba342f_image.png)

## Key Takeaways

You may argue this vulnerability is very obvious and easy to find - and you are absolutely right. It is easy to find and it should have never ended up in production in the first place. Not 10 years ago and especially not today. But bugs like this are a steady companion when researching the security of embedded devices and underline the importance of shedding light into the supply-chain of your devices. This makes the security level of SBOM, device configuration, and also proprietary applications transparent - the only way to reliably determine your own security posture and cyber resilience.

## Timeline

**2022-09-12** \- Sent coordinated disclosure request to security@asus.com

**2022-09-13** \- Asus answered "[...] since this model, NAS-M25 is end of life for years, we will not maintain its firmware and its security.".

**2022-12-01** \- ONEKEY release its advisory

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
