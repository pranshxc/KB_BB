---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159943'
original_report_id: '159943'
title: Create an Unexpected Object and Don't Invoke __wakeup() in During Deserialization
team_handle: ibb
created_at: '2016-08-17T06:30:29.105Z'
disclosed_at: '2019-10-13T11:09:59.593Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# Create an Unexpected Object and Don't Invoke __wakeup() in During Deserialization

## Metadata

- HackerOne Report ID: 159943
- Weakness: 
- Program: ibb
- Disclosed At: 2019-10-13T11:09:59.593Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=72663

the first commit for fix this bug at:
https://github.com/php/php-src/commit/448c9be157f4147e121f1a2a524536c75c9c6059
but this commit lead to type confusion, i reported this bug at comments. then the improve fix commit at:
https://github.com/php/php-src/commit/639f7fde6a51c23d7c670358fbcb777ac1a143f3

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
