---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1037714'
original_report_id: '1037714'
title: XSS in Email Input [intensedebate.com]
weakness: Cross-site Scripting (XSS) - Generic
team_handle: automattic
created_at: '2020-11-18T17:09:13.160Z'
disclosed_at: '2020-12-26T10:58:15.527Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 95
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in Email Input [intensedebate.com]

## Metadata

- HackerOne Report ID: 1037714
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: automattic
- Disclosed At: 2020-12-26T10:58:15.527Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I found an XSS in Email input. This input is not sanitized like other inputs allowing user to execute xss payloads.

## Platform(s) Affected:
https://www.intensedebate.com/edit-user-account

## Steps To Reproduce:
1. Navigate to your account.
2. In email address, add the below payload next to your email.
`"><img src=x onerror=alert(document.cookie);>`

## Supporting Material/References:
██████

## Impact

Reflected XSS, An attacker can execute malicious javascript codes on the target application (email input specifically). It is highly recommended to fix this one because it is found in sensitive input (email).

Kind Regards.

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
