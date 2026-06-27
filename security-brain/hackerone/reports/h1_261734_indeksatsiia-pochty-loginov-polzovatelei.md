---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '261734'
original_report_id: '261734'
title: Индексация почты/логинов пользователей
team_handle: bumble
created_at: '2017-08-20T13:08:59.097Z'
disclosed_at: '2018-06-24T10:03:08.928Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
---

# Индексация почты/логинов пользователей

## Metadata

- HackerOne Report ID: 261734
- Weakness: 
- Program: bumble
- Disclosed At: 2018-06-24T10:03:08.928Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте! Если проверить и ввести в гугл поиск site:badoo.com inurl:?email=  то мы получим много страниц, перейдя по ссылкам которых нам будет виден полностью логин(почта) пользователя. Для примера получаем вот такую ссылку https://badoo.com/id/signin/?email=nocai%40yahoogroups.com&sold1=LT9EIDYZaQ-0kpW6rMJGwH_FXC35loVj
где логин является nocai@yahoogroups.com  или https://badoo.com/ru/signin/?email=spip%40rezo.net&sold1=2lUdND_SQwvFeRGr97WfTkJyBIx1oqij здесь логин spip@rezo.net
Ваша система говорить что такой логин существует, я думаю что эти данные индексировались по какой-то ошибке, которую вы должны устранить, так как нынешние технологии помогают подобрать пароль к любому логину, и это может быть опасно для ваших пользователей.

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
