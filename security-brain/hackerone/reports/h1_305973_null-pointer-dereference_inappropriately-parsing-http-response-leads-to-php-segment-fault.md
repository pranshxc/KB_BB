---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '305973'
original_report_id: '305973'
title: Inappropriately parsing HTTP response leads to PHP segment fault!
weakness: NULL Pointer Dereference
team_handle: ibb
created_at: '2018-01-17T17:29:19.969Z'
disclosed_at: '2019-11-12T09:18:47.648Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- null-pointer-dereference
---

# Inappropriately parsing HTTP response leads to PHP segment fault!

## Metadata

- HackerOne Report ID: 305973
- Weakness: NULL Pointer Dereference
- Program: ibb
- Disclosed At: 2019-11-12T09:18:47.648Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description
-----
A NULL Pointer Deference in parsing HTTP header. It is very easy to trigger this segment fault and may be vulnerable in some scenarios.


　
## Original bug report
-----
- https://bugs.php.net/bug.php?id=75535

　
## Note
-----
- None

　
Thanks :)

## Impact

Segment fault

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
