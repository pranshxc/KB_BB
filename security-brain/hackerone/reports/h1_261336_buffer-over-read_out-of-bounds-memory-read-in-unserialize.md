---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '261336'
original_report_id: '261336'
title: Out of Bounds Memory Read in unserialize()
weakness: Buffer Over-read
team_handle: ibb
created_at: '2017-08-18T13:22:28.231Z'
disclosed_at: '2018-11-27T15:59:52.325Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- buffer-over-read
---

# Out of Bounds Memory Read in unserialize()

## Metadata

- HackerOne Report ID: 261336
- Weakness: Buffer Over-read
- Program: ibb
- Disclosed At: 2018-11-27T15:59:52.325Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The finish_nested_data function in ext/standard/var_unserializer.re in PHP before 5.6.31, 7.0.x before 7.0.21, and 7.1.x before 7.1.7 is prone to a buffer over-read while unserializing untrusted data. Exploitation of this issue can have an unspecified impact on the integrity of PHP.

This has been fixed and assigned CVE-2017-12933 the bug report is here: https://bugs.php.net/bug.php?id=74111

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
