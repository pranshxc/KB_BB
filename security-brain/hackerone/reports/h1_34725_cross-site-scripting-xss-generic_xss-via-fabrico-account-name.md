---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '34725'
original_report_id: '34725'
title: XSS via Fabrico Account Name
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2014-11-06T19:23:33.010Z'
disclosed_at: '2016-07-11T18:04:28.386Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS via Fabrico Account Name

## Metadata

- HackerOne Report ID: 34725
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2016-07-11T18:04:28.386Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

O.S: Windows 8
Browser: Google Chrome

Steps to reproduce:
1) Inject This Payload while Signing Up your account at fabrico
#"><img src=x onerror=alert(2);>
2) After the Confirmation, Activate your account 

That's it Pop Will indicate XSS vulnerability

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
