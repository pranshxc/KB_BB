---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1164452'
original_report_id: '1164452'
title: Remote code execution due to unvalidated file upload
weakness: Improper Input Validation
team_handle: mtn_group
created_at: '2021-04-13T20:39:14.533Z'
disclosed_at: '2022-09-01T17:29:41.958Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: mtn.cm
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-input-validation
---

# Remote code execution due to unvalidated file upload

## Metadata

- HackerOne Report ID: 1164452
- Weakness: Improper Input Validation
- Program: mtn_group
- Disclosed At: 2022-09-01T17:29:41.958Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello 
I found a critical vunerability in one of your site, where user can upload any file type as a profile picture (including php file)


## Steps To Reproduce:
1. Visit https://careers.mtn.cm and register as a user.
2. After successful registration, login and update your data.
3. When uploading profile photo, select any file type.
 4. When its updated, view the source code of the page, you will see your file with complete path.
5. Copy the file path and paste into your browser.
6. Boom your file will be executed



## Supporting Material/References:
Here i upload non-harmful file as a poc 
```
<?php
echo "proof of concept (PoC) by aliyugombe@wearehackerone.com";
?>
```
https://careers.mtn.cm/en/user/images/users/-13-04-2021-20-15-16-payload.php

## Impact

Attacker can upload malicious file and inject to your server or deface the entire website since its possible to upload php file and gain access to direct file path.

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
