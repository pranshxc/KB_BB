---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '107664'
original_report_id: '107664'
title: Изменение текстов вариантов ответа в опросах
team_handle: vkcom
created_at: '2015-12-31T14:53:23.635Z'
disclosed_at: '2018-01-30T19:03:01.294Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
---

# Изменение текстов вариантов ответа в опросах

## Metadata

- HackerOne Report ID: 107664
- Weakness: 
- Program: vkcom
- Disclosed At: 2018-01-30T19:03:01.294Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Работает в профилях/группах с открытой стеной и на любых публичных страницах.
1) При помощи wall.getById получаем ид нужного опроса
2) При помощи wall.post отправляем пост с нужным опросом в предложенные новости паблика или на стену профиля/группы непосредственно изначально создавших опрос.
3) Редактируем, варианты ответа изменяются как и в нашем, так и в первоначальном посте.
Для примера изменил варианты ответа в одном из старых опросов группы LIVE
http://vk.com/wall-2158488_356836

Чтобы исправить проблему достаточно просто проверять является ли человек изменяющий опрос его создателем/администратором создавшей его группы.
С Новым Годом!

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
