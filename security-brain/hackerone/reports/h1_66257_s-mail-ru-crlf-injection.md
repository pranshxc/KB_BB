---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '66257'
original_report_id: '66257'
title: '[s.mail.ru] CRLF Injection'
team_handle: mailru
created_at: '2015-06-06T07:18:29.325Z'
disclosed_at: '2016-10-03T11:56:30.189Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# [s.mail.ru] CRLF Injection

## Metadata

- HackerOne Report ID: 66257
- Weakness: 
- Program: mailru
- Disclosed At: 2016-10-03T11:56:30.189Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Сценарий перенаправления с https://s.mail.ru/ на https://cloud.mail.ru/ уязвим к атаки типа CRLF Injection.

PoC 
Установка cookie crlf=injection на .mail.ru
Подвержены все браузеры, кроме FireFox

https://s.mail.ru/test%0dSet-Cookie:crlf=injection;domain=.mail.ru;

Может быть использовано в комбинации с другими уязвимостями (в случае их наличия) / факторами, например:
1) XSS через Cookie
2) Фиксация сессии
2) Обход CSRF защиты основанной на Cookie

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
