---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1072857'
original_report_id: '1072857'
title: '[titans.3clans.ru] phpBB 3.0.8 - Захват аккаунта администратора + удалённое
  выполнение кода.'
weakness: OS Command Injection
team_handle: mailru
created_at: '2021-01-06T16:42:00.642Z'
disclosed_at: '2021-11-06T19:05:38.340Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: Hosting
asset_type: OTHER
max_severity: none
tags:
- hackerone
- os-command-injection
---

# [titans.3clans.ru] phpBB 3.0.8 - Захват аккаунта администратора + удалённое выполнение кода.

## Metadata

- HackerOne Report ID: 1072857
- Weakness: OS Command Injection
- Program: mailru
- Disclosed At: 2021-11-06T19:05:38.340Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Наткнулся на сайт http://titans.3clans.ru, он стоит на 188.93.63.60 ( hostname: 	newsdclans.ext.terrhq.ru)
Везде весело мыло админа ```negasus@mail.ru```, вбив его в интернете, я нашёл пароли от почты. К форуму подошла такая комбинация:
Negasus:43046721
Дальше идём в админ-панель, "/adm/index.php", в настройках безопасности разрешаем выполнение php-кода в стилях, затем редактируем любой шаблон.
Я в видео использовал вызов phpinfo();
```
<!-- PHP -->

phpinfo();

<!-- ENDPHP -->
```
На странице сайта(в зависимости от шаблона, который мы правим)видим phpinfo()

## Impact

Удалённое выполнение кода

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
