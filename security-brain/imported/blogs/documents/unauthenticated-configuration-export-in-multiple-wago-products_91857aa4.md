---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-16_unauthenticated-configuration-export-in-multiple-wago-products.md
original_filename: 2023-02-16_unauthenticated-configuration-export-in-multiple-wago-products.md
title: Unauthenticated Configuration Export in Multiple WAGO Products
category: documents
detected_topics:
- command-injection
- automation-abuse
- oauth
- access-control
- path-traversal
- csrf
tags:
- imported
- documents
- command-injection
- automation-abuse
- oauth
- access-control
- path-traversal
- csrf
language: en
raw_sha256: 91857aa4a9323d7e44b2c0fab96797a69f3cbd4cf158011218a85029a1d91ebf
text_sha256: 34437cad7a952b53a4897a4464878c780124e10d13dac2898eff07acb3a9a464
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthenticated Configuration Export in Multiple WAGO Products

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-16_unauthenticated-configuration-export-in-multiple-wago-products.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, oauth, access-control, path-traversal, csrf
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `91857aa4a9323d7e44b2c0fab96797a69f3cbd4cf158011218a85029a1d91ebf`
- Text SHA256: `34437cad7a952b53a4897a4464878c780124e10d13dac2898eff07acb3a9a464`


## Content

---
title: "Unauthenticated Configuration Export in Multiple WAGO Products"
page_title: "Security Advisory: Unauthenticated Configuration Export in Multiple WAGO Products | ONEKEY Research | Research | ONEKEY"
url: "https://onekey.com/blog/security-advisory-wago-unauthenticated-config-export-vulnerability/"
final_url: "https://www.onekey.com/resource/security-advisory-wago-unauthenticated-config-export-vulnerability"
authors: ["ONEKEY (@onekey_sec)"]
programs: ["WAGO"]
bugs: ["Path traversal", "Security code review"]
publication_date: "2023-02-16"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1665
---

[Resources](/resources)

>

[Research](/resources/research)

>

Security Advisory: Unauthenticated Configuration Export in Multiple WAGO Products

# Security Advisory: Unauthenticated Configuration Export in Multiple WAGO Products

![Security Advisory: Unauthenticated Configuration Export in Multiple WAGO Products](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b82392576838fde8dd5c6_6712ae275f72b4574c03535f_03.jpeg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

January 15, 2023

5

min read

TablE of contents

Example H2

## READY TO UPGRADE YOUR RISK MANAGEMENT?

Make cybersecurity and compliance efficient and effective with ONEKEY.

[See it in Action](/book-a-demo)

## Introduction

As shown in our [previous security advisory for the Asus M25 NAS](https://b1eyc.myrdbx.io/blog/security-advisory-asus-m25-nas-vulnerability/), we recently introduced a “zero-day identification” module that performs static code analysis on proprietary applications found within firmware uploaded to ONEKEY’s platform. 

This module reported two potential issues within a [WAGO Series PFC100](https://www.wago.com/global/automation-technology/discover-plcs/pfc100) configuration API: a path traversal and a command injection vulnerability. The command injection turned out to be a false positive (we strengthened our analysis capabilities since then) but it got us to investigate a specific PHP file where we identified that the authentication and authorization code blocks were commented. 

We verified that it could lead to an unauthenticated configuration export using an emulated device and reported both this issue and the path traversal to WAGO. 

## Unauthenticated Configuration Export

**Affected vendor & product** | 

  * Series WAGO PFC100 (750-81xx/xxx-xxx)
  * Series WAGO PFC200 (750-82xx/xxx-xxx)
  * WAGO Compact Controller CC100 (751-9301)
  * WAGO Edge Controller (752-8303/8000-002)
  * Series WAGO Touch Panel 600 Standard Line (762-4xxx)
  * Series WAGO Touch Panel 600 Advanced Line (762-5xxx)
  * Series WAGO Touch Panel 600 Marine Line (762-6xxx)

  
---|---  
**Vendor Advisory** | <https://cert.vde.com/de/advisories/VDE-2022-054/>  
**Vulnerable version** | Firmware versions >= 16 and <= 22.  
**Fixed version** | We recommend all affected users to install FW22 Patch 1 or higher.  
**CVE IDs** | [CVE-2022-3738](https://nvd.nist.gov/vuln/detail/CVE-2022-3738)  
**Impact (CVSS)** | 4.3 (medium) [(CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N)](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N&version=3.1)  
**Credit** | Q. Kaiser, ONEKEY Research Lab  
Research supported by [Certainity](https://www.certainity.com/)  
  
## Summary

The configuration API of the web-based management interface (WBM) of WAGOs programmable logic controller (PLC) does not require authentication and offers the download of files in a specific folder. This folder typically contains backups created since the last reboot, which might hold sensitive data.

##  
Impact

A successful exploit could allow the attacker to download a copy of the running firmware or the VPN configuration. Both these files would hold sensitive information such as user credentials or cryptographic material. 

Note that to be able to download the files, they must have been generated by a legitimate user since the last reboot.  
  

## Description

The WAGO web admin interface is written in PHP and has a page allowing for VPN configuration or firmware export found at `/var/www/wbm/php/file_transfer/offer_download.php`. Within this file, lines 30 to 46 are commented using a multi-line comment. This effectively disables the authentication and authorization checks that were supposed to be performed on those lines.
  
  
  <?php
  include_once "wbm_lib.inc.php";
  include_once __DIR__.'/wbm_lib.inc.php';
  include_once __DIR__.'/file_transfer.inc.php';
  include_once __DIR__.'/../authentication/session_lifetime.inc.php';
  use transfer\FileTransfer;
  // define constants
  /*
  define("DOWNLOAD_DIR", "/tmp");
  define("UPLOAD_DIR", "/tmp");
  */
  define("DOWNLOAD_FILENAME_FRAGMENT", "firmware_backup");
  // Offer backup download file. Function takes the first file in download directory (there should be only one),
  // transfers it to browser and deletes the file afterwards.
  function OfferDownload()
  {
  $status = SUCCESS;
  $errorText = "";
  $transfer; // optional, of type FileTransfer
  /*
  // check for correct session and reset session timeout
  $status = Session_HandleSessionLifeTime($_GET["csrf_id"],false);
  if(SUCCESS != $status)
  {
  $errorText = Session_GetErrorTxt($status);
  }
  else if(!isset($_SESSION["username"]) || USER_ADMIN != $_SESSION["username"])
  {
  $status = ACCESS_NOT_ALLOWED;
  $errorText = "Access not allowed.";
  }
  // check if folder is given
  else
  */
  {
  if(!isset($_GET["download_dir"]))

##  
**Authenticated Path Traversal (Bonus)**

WAGO does not consider the authenticated path traversal to be a vulnerability since it can only be triggered by a user with administrative privileges. A user with these privileges can simply create a backup of the running firmware and download it, making the path traversal and possibility to download arbitrary files useless. We fully agree with that assessment, but still wanted to show how it was found.

The path traversal was reported as affecting download.php. As we can see in the screenshot below, the `$downloadPath` value is used by a `fopen` call.

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8bad2b82119e3dfedf0c_image-2-1024x479.png)

This `$downloadPath` is directly obtained from the GET parameter "download":
  
  
  $downloadPath = '';
  
  if (isset($_GET['download'])) {
  $downloadPath = $_GET['download'];
  
  // check file exists
  if(!file_exists($downloadPath))
  {
  die_with_response(200, [
  'error' => new WBMError(ERROR_GROUP_FILE_TRANSFER, ERROR_CODE_DOWNLOAD_FILE_DOES_NOT_EXIST, 'File does not exist')
  ]);
  }
  
  // check access rights
  if(!is_readable($downloadPath))
  {
  die_with_response(200, [
  'error' => new WBMError(ERROR_GROUP_FILE_TRANSFER, ERROR_CODE_DOWNLOAD_FILE_NOT_READABLE, 'File is not readable')
  ]);
  }
  }

The file content is then returned to the user:
  
  
  $file = fopen($downloadPath, 'r');
  if(!$file) {
  die_with_response(200, [
  'error' => new WBMError(ERROR_GROUP_FILE_TRANSFER, ERROR_CODE_DOWNLOAD_FILE_NOT_READABLE, 'File is not readable')
  ]);
  }
  
  // put fitting filetype to header
  header("Content-Type: application/octet-stream");
  
  // send header with proposal of fitting filename
  header(sprintf("Content-Disposition: attachment; filename=\"%s\"",  basename($downloadPath)));
  
  // send file size
  header('Content-Length: '.filesize($downloadPath));
  
  // before sending the file content, add a cookie to tell the frontend that the download will be started
  setcookie("download($downloadPath)", 'started', 0, '/');
  
  flush();
  
  // read and send file chunkwise
  while (!feof($file)) {
  print fread($file, 1024*1024); // read 1MiB...
  flush();  // ... and send to browser
  }
  fclose($file);

## Key Takeaways

Having the possibility to automatically identify unknown high-risk and critical vulnerabilities is a powerful capability have - a super-power both for operators and manufacturers of IACS. Operators get a chance to efficiently validate vendor claims on a low-effort basis and security manufacturers can fix such vulnerabilities before even shipping devices to their clients. While it is important to be as confident as possible about potential vulnerabilities, sometimes something that just looks like a vulnerability turns out to reveal a vulnerable area of the application.

## Timeline

**2022-10-17** – Sent coordinated disclosure request to [psirt@wago.com](mailto:psirt@wago.com)

**2022-10-17** – Answer from WAGO PSIRT (Product Security Incident Response Team), establishment of secure communication channel. 

**2022-10-21** – First feedback from WAGO PSIRT on reproduction. 

**2022-10-21** – Second feedback from WAGO PSIRT on authenticated path traversal. 

**2022-11-10** – WAGO PSIRT provides us with CVE (Common Vulnerabilities and Exposures) ID and CVSS (Common Vulnerability Scoring System) score, start coordination with CERT@VDE 

**2022-12-08** – WAGO PSIRT shares draft advisory with us and CERT@VDE 

**2023-01-12** – CERT@VDE releases WAGO advisory 

**2023-01-16** – ONEKEY releases its advisory 

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
