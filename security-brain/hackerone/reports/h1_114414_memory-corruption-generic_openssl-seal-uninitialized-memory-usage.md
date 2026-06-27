---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '114414'
original_report_id: '114414'
title: openssl_seal() uninitialized memory usage
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-02-03T13:01:11.393Z'
disclosed_at: '2019-11-12T09:38:26.105Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# openssl_seal() uninitialized memory usage

## Metadata

- HackerOne Report ID: 114414
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-11-12T09:38:26.105Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

openssl_seal() is prone to use uninitialized memory that can be turned into a code execution.

Details about bug: https://bugs.php.net/bug.php?id=71475 (already fixed)
Details about exploitation: http://akat1.pl/?id=1 (released after bug was fixed)

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
