---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '672245'
original_report_id: '672245'
title: Use After Free in GC with Certain Destructors
weakness: Use After Free
team_handle: ibb
created_at: '2019-08-13T13:17:43.075Z'
disclosed_at: '2020-11-09T01:45:39.148Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 0
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- use-after-free
---

# Use After Free in GC with Certain Destructors

## Metadata

- HackerOne Report ID: 672245
- Weakness: Use After Free
- Program: ibb
- Disclosed At: 2020-11-09T01:45:39.148Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The bug submitted at: https://bugs.php.net/bug.php?id=72530
The fix committed at: http://git.php.net/?p=php-src.git;a=commit;h=60a7e60b61b8e4a3d455974c83f76a26546ce117

## Impact

The bug can be abused for leaking arbitrary memory blocks or execute arbitrary code remotely via PHP’s object deserializing. ex: unserialize/phar/session

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
