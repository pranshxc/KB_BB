---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8846'
original_report_id: '8846'
title: localStorage не чистится после выхода
weakness: Information Disclosure
team_handle: mailru
created_at: '2014-04-21T21:13:28.618Z'
disclosed_at: '2014-12-10T19:05:41.425Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# localStorage не чистится после выхода

## Metadata

- HackerOne Report ID: 8846
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2014-12-10T19:05:41.425Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Steps to reproduce:
1. Идем https://e.mail.ru/login
2. Авторизуемся и при этом снимаем галочку с чекбоска  "запомнить почту" (не обязательно, в принципе)
3. После удачной авторизации жмём "Выход"
4.  После того как вышли, идем опять https://e.mail.ru/login
5. Смотрим локальное хранилище (localStorage) браузера и видим кучу инфы о юзере.

Expected:
После нажатия на кнопку выход, localStorage у e.mail.ru должен очищаться. Т.к. заходя в свой аккаунт с чужого компьютера пользователь ожидает, что после нажатия на кнопку "Выход" он на компьютере  не оставит никакой личной информации.

P.S.
Пользуюсь mail.ru вот уже 6 лет. Большое спасибо за такой удобный сервис.

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
