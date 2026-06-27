---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '93020'
original_report_id: '93020'
title: Способ узнать имя человека и ВУЗ удаленной страницы
weakness: Privilege Escalation
team_handle: vkcom
created_at: '2015-10-08T23:03:35.650Z'
disclosed_at: '2016-10-17T20:35:29.795Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- privilege-escalation
---

# Способ узнать имя человека и ВУЗ удаленной страницы

## Metadata

- HackerOne Report ID: 93020
- Weakness: Privilege Escalation
- Program: vkcom
- Disclosed At: 2016-10-17T20:35:29.795Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. Выбираем любую удаленную страницу.
2. Например, открываем http://vk.com/id55555
3. Видим сообщение о том, что "Страница удалена, либо еще не создана" и никакой информации более.
4. Воспользуемся widget_subscribe.php с одним лишь параметром oid
5. https://vk.com/widget_subscribe.php?oid=55555
6. Profit! Наталья Кузнецова
7. Кстати, я смог на неё ещё и подписаться. После этого я смог узнать ВУЗ.
Для этого на странице виджета с переданным параметром открываем инспектор и для класса "w_subscr_btn" удаляем стиль display:none (ну либо ставим block и т.д.). Во всплывающем окне кликаем "Подписаться". Вуаля!

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
