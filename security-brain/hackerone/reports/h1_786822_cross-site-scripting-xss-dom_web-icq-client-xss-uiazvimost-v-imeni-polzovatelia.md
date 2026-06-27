---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '786822'
original_report_id: '786822'
title: '[Web ICQ Client] XSS уязвимость в имени пользователя'
weakness: Cross-site Scripting (XSS) - DOM
team_handle: mailru
created_at: '2020-01-31T11:09:49.635Z'
disclosed_at: '2020-02-14T19:20:55.283Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: ICQ
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# [Web ICQ Client] XSS уязвимость в имени пользователя

## Metadata

- HackerOne Report ID: 786822
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: mailru
- Disclosed At: 2020-02-14T19:20:55.283Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application: WEB ICQ Client - https://web.icq.com/

Testing environment: Browser (firefox)

Steps to reproduce
1. Устанавливаем имя пользователя, содержащее HTML код
2. Создаем канал/группу, в который приглашаем любого пользователя
3. Разрешаем/Запрещаем писать пользователю

Actual results
В нотификации отображаемой в чате выполнится HTML код указанный в имени пользователя (отсутствует фильтрация).

На сколько понимаю, применение узконаправленное (данные уведомления отображаются только у получателя и отправителя настроек ограничений). 

Screencast:
████

P. S.: В клиентском браузере отображается название канала, вместо логина администратора, применившего санкции. Название канала так же может содержать HTML код:
{F702013}

## Impact

Выполнение произвольного JS в Web клиенте

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
