---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '661847'
original_report_id: '661847'
title: Integer overflows in tool_operate.c at line 1541
weakness: Integer Overflow
team_handle: curl
created_at: '2019-07-27T15:07:00.843Z'
disclosed_at: '2021-01-01T15:40:09.134Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- integer-overflow
---

# Integer overflows in tool_operate.c at line 1541

## Metadata

- HackerOne Report ID: 661847
- Weakness: Integer Overflow
- Program: curl
- Disclosed At: 2021-01-01T15:40:09.134Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
[add summary of the vulnerability]
In tool_operate.c at line 1541, if --retry-delay>18446744073709552, config->retry_delay*1000 > 2^64 results in integer overflows, on 64 bit architectures; 
## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. [add step]
Tool_operate.c add a "printf" at line 1538 as following:
printf("config->retry_delay*1000L = %ld\n", config->retry_delay*1000L);
  2. [add step]
make
  1. [add step]
run command:  
./src/curl --retry-delay 18446744073709552 -v 192.168.222.1:8080/test.html
output:
config->retry_delay*1000L = 384

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

The flaw exists on 32&64 bit architectures, it results in retry-delay is invalid.

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
