---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '36105'
original_report_id: '36105'
title: CRLF Injection [ishop.qiwi.com]
team_handle: qiwi
created_at: '2014-11-15T12:55:28.427Z'
disclosed_at: '2016-10-24T22:22:45.578Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
---

# CRLF Injection [ishop.qiwi.com]

## Metadata

- HackerOne Report ID: 36105
- Weakness: 
- Program: qiwi
- Disclosed At: 2016-10-24T22:22:45.578Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

/* Я уже слал эту уязвимость 09.06.2014 и она исправлена. Просили переслать через hackerone. */

Сценарий перенаправления с http://ishop.qiwi.com/  на httpS://ishop.qiwi.com/  уязвим к атаке типа CRLF Injection.

PoC
Создание Cookie test=test для сайтов *.qiwi.com
Уязвимы все браузеры, кроме FireFox
http://ishop.qiwi.com/test%0dSet-Cookie:test2=test;domain=.qiwi.com

Возможно использование в комбинации с другими факторами/уязвимостями (в случае их наличия):
- XSS через Cookie
- Фиксация сессии
- Обход CSRF защиты на основе Cookie 
и т.п.

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
