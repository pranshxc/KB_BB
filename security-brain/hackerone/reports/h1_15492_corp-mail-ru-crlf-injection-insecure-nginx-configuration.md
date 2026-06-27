---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15492'
original_report_id: '15492'
title: '[corp.mail.ru] CRLF Injection / Insecure nginx configuration'
team_handle: mailru
created_at: '2014-06-07T15:35:01.817Z'
disclosed_at: '2016-10-06T12:22:10.332Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# [corp.mail.ru] CRLF Injection / Insecure nginx configuration

## Metadata

- HackerOne Report ID: 15492
- Weakness: 
- Program: mailru
- Disclosed At: 2016-10-06T12:22:10.332Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Сценарий перенаправления с http://corp.mail.ru/ на http://corp.mail.ru/ru/ уязвим к атаки типа CRLF Injection.

PoC 
Установка cookie test=test на .mail.ru
Подвержены все браузеры, кроме FireFox
http://corp.mail.ru/%0dSet-Cookie:test=test;domain=.mail.ru;

Может быть использовано в комбинации с другими уязвимостями (в случае их наличия) / факторами, например:
1) XSS через Cookie
2) Фиксация сессии
2) Обход CSRF защиты основанной на Cookie

PoC
Установка предопределенного CSRF-токена на всех Django сайтах в зоне *.mail.ru (calendar.mail.ru, biz.mail.ru и т.п.)
Подвержены все браузеры, кроме FireFox
 http://corp.mail.ru/%0dSet-Cookie:csrftoken=x;domain=.mail.ru;

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
