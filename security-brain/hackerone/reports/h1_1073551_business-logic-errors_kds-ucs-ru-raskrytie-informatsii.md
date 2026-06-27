---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1073551'
original_report_id: '1073551'
title: kds.ucs.ru - раскрытие информации.
weakness: Business Logic Errors
team_handle: mailru
created_at: '2021-01-07T15:44:32.722Z'
disclosed_at: '2021-11-06T19:03:23.716Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
asset_identifier: Foodplex
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# kds.ucs.ru - раскрытие информации.

## Metadata

- HackerOne Report ID: 1073551
- Weakness: Business Logic Errors
- Program: mailru
- Disclosed At: 2021-11-06T19:03:23.716Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

При посещение главной страницы, прогружается main-страница, она ссылается на JS-скрипт https://kds.ucs.ru/app/apiMock.js
В скрипте сетятся такие данные, как:
Токен(скорее всего авторизации)
Почта аккаунта диллера:  ({"data":{"id":"a.tutin@ucs.ru","userRole":"Dealer"}});
Список всех клиентов, кто пользуется кассой(Название и id компании)
Так-же в низу файла выволдятся настройки некоторых компаний и uuid компаний(Скорее всего отображается только часть тех компаний, к которым у диллера есть доступ)
Ещё есть ШАБЛОНЫ настроек профиля, Профили, Клиенты и куча всего прочего. Я прикреплю файл с нормальной кодировкой.

## Impact

Раскрытие информации, не достаточная проверка авторизации.

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
