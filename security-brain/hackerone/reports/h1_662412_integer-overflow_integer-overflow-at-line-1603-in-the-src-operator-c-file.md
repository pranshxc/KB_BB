---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '662412'
original_report_id: '662412'
title: Integer overflow  at line 1603 in the src/operator.c file
weakness: Integer Overflow
team_handle: curl
created_at: '2019-07-29T01:10:32.565Z'
disclosed_at: '2021-02-08T07:55:42.258Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- integer-overflow
---

# Integer overflow  at line 1603 in the src/operator.c file

## Metadata

- HackerOne Report ID: 662412
- Weakness: Integer Overflow
- Program: curl
- Disclosed At: 2021-02-08T07:55:42.258Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
[add summary of the vulnerability]
On systems with a 64 bit, if —retry-max-time > 18446744073709552, config->retry-max-time*1000L will be overflow  at line 1603 in the src/operator.c file. Similarly, the same is true for 32-bit operating systems.
## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. [add step]
run: curl --retry-max-time 18446744073709552 -v 127.0.0.1:8080/test.html
  1. [add step]
  1. [add step]

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

If the integer overflow is triggered, the parameter retry-max-time will be illegal.

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
