---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '510025'
original_report_id: '510025'
title: Invalid Read on exif_process_SOFn
weakness: Buffer Over-read
team_handle: ibb
created_at: '2019-03-15T08:45:38.365Z'
disclosed_at: '2020-10-10T02:17:08.150Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- buffer-over-read
---

# Invalid Read on exif_process_SOFn

## Metadata

- HackerOne Report ID: 510025
- Weakness: Buffer Over-read
- Program: ibb
- Disclosed At: 2020-10-10T02:17:08.150Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This  bug is present in exif_scan_thumbnail method of ext/exif/exif.c file.

Detailed description and steps to reproduce for this bug is present in bug report submitted to php.net.
Bug Report : https://bugs.php.net/bug.php?id=77540
PHP version : 7.1.26
CVE-ID : 2019-9640

## Impact

This bug may allow an attacker to read unintended data from memory.

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
