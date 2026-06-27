---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1913263'
original_report_id: '1913263'
title: HTML Injection at https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/unsubscribe
weakness: Cross-Site Scripting (XSS)
team_handle: mozilla
created_at: '2023-03-20T17:50:34.520Z'
disclosed_at: '2023-10-20T09:32:12.474Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
asset_identifier: monitor.mozilla.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss
---

# HTML Injection at https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/unsubscribe

## Metadata

- HackerOne Report ID: 1913263
- Weakness: Cross-Site Scripting (XSS)
- Program: mozilla
- Disclosed At: 2023-10-20T09:32:12.474Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello, 

The "Unsubscribe" page seems to be affected by Cross-Site Scripting (XSS) .Unfortunately my IP was blocked and I couldn't go ahead with the test to find a real proof of concept. So I'll just stick to this

POC:

https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/unsubscribe?%27%22%3E%3C/title%3E%3Cscript%3Ealert(xss)%3C/script%3E%3E%3Cmarquee%3E%3Ch1%3EXSS%3C/h1%3E%3C/marquee%3E 

Cheers

## Impact

An attacker could use this to inject malicious client side code, such as JavaScript, and execute it within the context of another user. This could possibly lead to user account compromises, user’s being socially engineered and many more attacks against the application’s users.

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
