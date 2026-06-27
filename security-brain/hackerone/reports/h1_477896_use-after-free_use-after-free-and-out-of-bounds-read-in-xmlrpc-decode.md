---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '477896'
original_report_id: '477896'
title: Use after free and out of bounds read in xmlrpc_decode()
weakness: Use After Free
team_handle: ibb
created_at: '2019-01-11T10:10:08.276Z'
disclosed_at: '2020-11-09T01:48:05.244Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- use-after-free
---

# Use after free and out of bounds read in xmlrpc_decode()

## Metadata

- HackerOne Report ID: 477896
- Weakness: Use After Free
- Program: ibb
- Disclosed At: 2020-11-09T01:48:05.244Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Malformed input can lead to use after free and out of bounds memory errors.

This has been fixed with the latest updates of PHP (7.1.26/7.2.14/7.3.1).

(Note: I reported those as separate bugs to PHP, but they had the same underlying bug and were fixed by the same commit. The release notes only mention "out of bounds read", but this is misleading, as a use after free error is potentially more severe.)

Bugs reported to PHP:
https://bugs.php.net/bug.php?id=77242
https://bugs.php.net/bug.php?id=77249

## Impact

If the xmlrpc functionality of PHP is used to parse untrusted input from a public API point it can potentially be used to gain code execution.

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
