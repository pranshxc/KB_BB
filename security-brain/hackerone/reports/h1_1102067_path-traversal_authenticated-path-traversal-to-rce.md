---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1102067'
original_report_id: '1102067'
title: Authenticated path traversal to RCE
weakness: Path Traversal
team_handle: concretecms
created_at: '2021-02-12T10:41:51.990Z'
disclosed_at: '2021-10-15T16:37:38.539Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: https://github.com/concrete5/concrete5
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# Authenticated path traversal to RCE

## Metadata

- HackerOne Report ID: 1102067
- Weakness: Path Traversal
- Program: concretecms
- Disclosed At: 2021-10-15T16:37:38.539Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

** crayons **

## Description
The `bFilename` parameter in the scenario `index.php/ccm/system/dialogs/block/design/submit` is vulnerable to remote code execution via path traversal vulnerability. Authenticated attacker with rights to edit web application pages can upload malicious PNG file containing PHP code using any attachment upload functions (for example in comment section of the blog) and then use its relative path in `bFilename` parameter while editing layout design.  The file, supplied in vulnerable parameter will be included in PHP, leading to injected malicious code to run.

## Testing setup :
Concrete5 CMS version: 8.5.4
PHP Version: 7.2.24

## Steps to reproduce
1) Login to your Concrete5 account with rights to edit pages
2) Upload using any attachment upload function png file, containing php code at its end. You can use file ```png-transparent.png``` from the attachments . It is empty PNG file with the following payload at its end:

```
<?php system("uname -a");?>
```
You can get file path for example by viewing uploaded file properties:
{F1193239}
3) Navigate to page edit constructor
4) Select any element (for example Sidebar) and click "Add Layout" -> "Add Layout"
5) Click on newly added block and select "Edit layout Design" -> Save
6) Get the request from step 5 from any web proxy (for example Burp Suite) and resend it modifying `bFilename` with the system relative path to the uploaded file, for example:

```
bFilename=../../../../application/files/9316/1312/5391/png-transparent.png
```
7) Reload the page, your are editing, and see the payload fired

{F1193235}

## Credits
This bug was found as a part of Solar Security CMS Reseach, with https://hackerone.com/d0bby, https://hackerone.com/wezery0, https://hackerone.com/silvereniqma in collaboration. Can you, please, add them to this report?

## Impact

Authenticated attacker with page editing rights can run arbitrary system commands and obtain sensitive information

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
