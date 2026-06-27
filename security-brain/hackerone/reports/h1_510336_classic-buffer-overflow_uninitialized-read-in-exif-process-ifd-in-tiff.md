---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '510336'
original_report_id: '510336'
title: Uninitialized read in exif_process_IFD_in_TIFF
weakness: Classic Buffer Overflow
team_handle: ibb
created_at: '2019-03-15T14:21:28.872Z'
disclosed_at: '2020-10-10T02:18:18.265Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 0
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- classic-buffer-overflow
---

# Uninitialized read in exif_process_IFD_in_TIFF

## Metadata

- HackerOne Report ID: 510336
- Weakness: Classic Buffer Overflow
- Program: ibb
- Disclosed At: 2020-10-10T02:18:18.265Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This bug can be reproduced only in 32 bit PHP builds.
This bug is present in exif_process_IFD_in_TIFF method of ext/exif/exif.c file.

Detailed description and steps to reproduce for this bug is present in bug report submitted to php.net.
Bug Report : https://bugs.php.net/bug.php?id=77509
PHP version : 7.1.26
CVE-ID : 2019-9641

## Impact

Uninitialized variables may leak data from memory.

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
