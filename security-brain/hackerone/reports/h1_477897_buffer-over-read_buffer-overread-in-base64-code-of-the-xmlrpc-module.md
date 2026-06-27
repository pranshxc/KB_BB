---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '477897'
original_report_id: '477897'
title: buffer overread in base64 code of the xmlrpc module
weakness: Buffer Over-read
team_handle: ibb
created_at: '2019-01-11T10:11:55.189Z'
disclosed_at: '2020-11-09T01:48:23.671Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- buffer-over-read
---

# buffer overread in base64 code of the xmlrpc module

## Metadata

- HackerOne Report ID: 477897
- Weakness: Buffer Over-read
- Program: ibb
- Disclosed At: 2020-11-09T01:48:23.671Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Malformed input to the xmlrpc_decode function can cause an out of bounds read in the base64 code.

This is fixed in the latest updates of PHP (7.3.1 etc.)

Report:
https://bugs.php.net/bug.php?id=77380

## Impact

If the attacker has access to the decoded output this may leak memory contents.

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
