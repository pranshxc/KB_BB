---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '258237'
original_report_id: '258237'
title: '[et.mail.ru] ssrf 2'
weakness: Server-Side Request Forgery (SSRF)
team_handle: mailru
created_at: '2017-08-09T12:29:02.198Z'
disclosed_at: '2017-12-28T15:31:11.858Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: '*.mail.ru / Mail.Ru - another project (except subdomains delegated
  to external entities)'
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# [et.mail.ru] ssrf 2

## Metadata

- HackerOne Report ID: 258237
- Weakness: Server-Side Request Forgery (SSRF)
- Program: mailru
- Disclosed At: 2017-12-28T15:31:11.858Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Привет, я подождал пока вы решите #251220 Эту багу, да она фикс. Затем я проверил другую и она работает, и видимо она не принадлежит одним и тем же параметрам при исправлении.

Domain, site, application
--
https://et.mail.ru/forums/

Steps to reproduce
--
1)Заходим например в общий раздел
https://et.mail.ru/forums/forumdisplay.php?f=1
2)Нажимаем "+Новая тема".
3)Чуть ниже есть форма управления вложениями - нажимаем ее
4)Выбираем загрузить с сайта и вписываем http://localhost:11211/asd.jpg
5)Так же, где то через 30 секунд  -- Ошибка 504.

PoC, exploit code, screenshots, video, references, additional resources
--
F210895

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
