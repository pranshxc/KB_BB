---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '258318'
original_report_id: '258318'
title: filin.mail.ru user's e-mail address disclosure
team_handle: mailru
created_at: '2017-08-09T18:19:34.378Z'
disclosed_at: '2018-02-21T11:51:33.707Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: ideas.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# filin.mail.ru user's e-mail address disclosure

## Metadata

- HackerOne Report ID: 258318
- Weakness: 
- Program: mailru
- Disclosed At: 2018-02-21T11:51:33.707Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте! Данный проект участвует в программе баунти?
Я нашла проблему проекта вопросы/ответы. На сколько мне известно, то в данном проекте доступным является только ИД пользователя и его НИК для общего просмотра, НО можно посмотреть адрес почты каждого участника проекта (дает адрес почты данный адрес https://filin.mail.ru/ )но в данном проекте почта не должна быть публично доступной. Для того чтобы узнать адрес почты любого пользователя нужно удобным способом включить перехват входящих запросов - переходим на страницу пользователя - и просматриваем данные по адресу https://filin.mail.ru/ - там будут картинки пользователя и полный адрес его почтового ящика, РАБОТАЕТ СО ВСЕМИ ПОЛЬЗОВАТЕЛЯМИ. Есть скрин. Данный адрес нам показывает аватарку пользователя, а берет ее из почты и засвечивает и ее адрес.

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
