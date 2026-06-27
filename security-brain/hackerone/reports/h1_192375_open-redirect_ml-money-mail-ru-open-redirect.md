---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '192375'
original_report_id: '192375'
title: '[ml.money.mail.ru] Open Redirect'
weakness: Open Redirect
team_handle: mailru
created_at: '2016-12-19T10:21:25.773Z'
disclosed_at: '2017-03-02T13:17:10.263Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- open-redirect
---

# [ml.money.mail.ru] Open Redirect

## Metadata

- HackerOne Report ID: 192375
- Weakness: Open Redirect
- Program: mailru
- Disclosed At: 2017-03-02T13:17:10.263Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**PoC**
Только для неавторизованных пользователей (без cookie Mpop)
```
https://ml.money.mail.ru//blackfan.ru
```

**HTTP Response**
```
HTTP/1.1 302
...
Location: //blackfan.ru?dmr_refresh=1
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
