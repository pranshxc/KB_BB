---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178094'
original_report_id: '178094'
title: php_snmp_parse_oid integer overflow in memory allocation
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-10-25T21:01:23.607Z'
disclosed_at: '2019-11-12T09:26:12.350Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# php_snmp_parse_oid integer overflow in memory allocation

## Metadata

- HackerOne Report ID: 178094
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-11-12T09:26:12.350Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=72708

An integer overflow in memory allocation allows to write past the allocated buffer, resulting in heap memory corruption.

Details and proof of concept are in the linked bug report; feel free to ask for more details if needed.

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
