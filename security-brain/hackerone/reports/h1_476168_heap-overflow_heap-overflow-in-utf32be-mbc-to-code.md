---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '476168'
original_report_id: '476168'
title: Heap overflow in utf32be_mbc_to_code
weakness: Heap Overflow
team_handle: ibb
created_at: '2019-01-07T20:15:56.831Z'
disclosed_at: '2020-11-09T01:48:51.477Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- heap-overflow
---

# Heap overflow in utf32be_mbc_to_code

## Metadata

- HackerOne Report ID: 476168
- Weakness: Heap Overflow
- Program: ibb
- Disclosed At: 2020-11-09T01:48:51.477Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=77418

Buffer overflow in mbc_to_code functions for UTF32BE, UTF32LE, UTF16BE, and UTF16LE due to incorrect length assumptions of a buffer. Provided a patch that was adapted to check the length of the buffer prior to using it.

## Impact

Memory leakage and/or corruption

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
