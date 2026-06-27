---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '399382'
original_report_id: '399382'
title: XSS in e.mail.ru
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2018-08-25T11:49:37.413Z'
disclosed_at: '2018-09-24T11:17:32.326Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: e.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS in e.mail.ru

## Metadata

- HackerOne Report ID: 399382
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2018-09-24T11:17:32.326Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Приветствую! Нашел XSS на e.mail.ru, при написании письма.

Предыстория:
Для начала я взял аккаунт на Яндексе с готовым xss вектором в имени "><img src=x onerror=alert()>, но возникла некая трудность в плане авторизации, меня не пропускало из за недопустимых символов в имени, тогда я взял смартфон, и авторизовался через приложение Mail.ru почта оттуда. И вуаля! с ПК версии теперь можно авторизоваться через Яндекс.

Шаги для воспроизведения:

1. Логинимся на почту через Яндекс.
2. Переходим в "написать письмо"
3. Получаем Alert.

## Impact

Cross-Site Scripting.

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
