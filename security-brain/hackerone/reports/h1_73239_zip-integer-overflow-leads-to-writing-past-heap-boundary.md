---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '73239'
original_report_id: '73239'
title: ZIP Integer Overflow leads to writing past heap boundary
team_handle: ibb
created_at: '2015-03-18T00:00:00.000Z'
disclosed_at: '2015-03-18T00:00:00.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# ZIP Integer Overflow leads to writing past heap boundary

## Metadata

- HackerOne Report ID: 73239
- Weakness: 
- Program: ibb
- Disclosed At: 2015-03-18T00:00:00.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=69253

Integer overflow in the _zip_cdir_new function in zip_dirent.c in libzip 0.11.2 and earlier, as used in the ZIP extension in PHP before 5.4.39, 5.5.x before 5.5.23, and 5.6.x before 5.6.7 and other products, allows remote attackers to cause a denial of service (application crash) or possibly execute arbitrary code via a ZIP archive that contains many entries, leading to a heap-based buffer overflow.

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
