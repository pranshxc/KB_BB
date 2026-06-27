---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '73237'
original_report_id: '73237'
title: Buffer Over flow when parsing tar/zip/phar in phar_set_inode
team_handle: ibb
created_at: '2015-04-14T00:00:00.000Z'
disclosed_at: '2015-04-14T00:00:00.000Z'
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

# Buffer Over flow when parsing tar/zip/phar in phar_set_inode

## Metadata

- HackerOne Report ID: 73237
- Weakness: 
- Program: ibb
- Disclosed At: 2015-04-14T00:00:00.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=69441

Multiple stack-based buffer overflows in the phar_set_inode function in phar_internal.h in PHP before 5.4.40, 5.5.x before 5.5.24, and 5.6.x before 5.6.8 allow remote attackers to execute arbitrary code via a crafted length value in a (1) tar, (2) phar, or (3) ZIP archive.

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
