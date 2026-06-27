---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1625036'
original_report_id: '1625036'
title: Insecure loading of ICU data through ICU_DATA environment variable
team_handle: nodejs
created_at: '2022-07-04T22:28:55.618Z'
disclosed_at: '2023-03-19T17:10:01.903Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Insecure loading of ICU data through ICU_DATA environment variable

## Metadata

- HackerOne Report ID: 1625036
- Weakness: 
- Program: nodejs
- Disclosed At: 2023-03-19T17:10:01.903Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Node.js correctly ignores the NODE_ICU_DATA environment variable when it is running with elevated privileges (e.g. setuid root).

ICU on the other hand still honors the ICU_DATA environment variable, without regard for privilege level.

## Impact

ICU is not very resilient to crafted data files but since users can select custom data files anyway with the `--icu-data-dir` flag, the real-world impact is probably not much worse than what is already possible through documented means...

...which doesn't mean it shouldn't be fixed because scenarios where it is in fact exploitable are imaginable, just not very likely.

Suggestions:

- build ICU with ICU_NO_USER_DATA_OVERRIDE defined
- sanitize the environment before initializing ICU

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
