---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '785785'
original_report_id: '785785'
title: '[Web ICQ Client] XSS-inj in polls'
weakness: Cross-site Scripting (XSS) - DOM
team_handle: mailru
created_at: '2020-01-29T20:10:08.290Z'
disclosed_at: '2020-02-14T19:20:45.955Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
asset_identifier: ICQ
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# [Web ICQ Client] XSS-inj in polls

## Metadata

- HackerOne Report ID: 785785
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: mailru
- Disclosed At: 2020-02-14T19:20:45.955Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application: WEB ICQ Client - https://web.icq.com/

Testing environment: Browser (firefox)

Steps to reproduce
- Создаем новый опрос
- Указываем в варианты ответов произвольный HTML код
- Отправляем

Actual results
- Введенный HTML код срабатывает

Демонстрация работы: █████

## Impact

Частичный перехват контроля над аккаунтом пользователя

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
