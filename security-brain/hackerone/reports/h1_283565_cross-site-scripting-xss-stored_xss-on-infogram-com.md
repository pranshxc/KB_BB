---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '283565'
original_report_id: '283565'
title: XSS on infogram.com
weakness: Cross-site Scripting (XSS) - Stored
team_handle: infogram
created_at: '2017-10-27T15:57:21.110Z'
disclosed_at: '2017-11-01T10:02:27.325Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS on infogram.com

## Metadata

- HackerOne Report ID: 283565
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: infogram
- Disclosed At: 2017-11-01T10:02:27.325Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

There is a XSS on Report templates.

Free templates : Report Classic 

When we modify the values of table we can put XSS Payload.

Payload used : 

"><img src=x onerror=prompt(0);>
"/><svg/onload=alert(0);>

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
