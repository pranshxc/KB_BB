---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '293105'
original_report_id: '293105'
title: XSS в личных сообщениях
team_handle: ok
created_at: '2017-11-26T23:51:05.422Z'
disclosed_at: '2018-01-13T11:59:20.335Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
tags:
- hackerone
---

# XSS в личных сообщениях

## Metadata

- HackerOne Report ID: 293105
- Weakness: 
- Program: ok
- Disclosed At: 2018-01-13T11:59:20.335Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Доброго времени суток. Я нашел XSS в личных сообщениях. 

Поле, где юзер набирает сообщения не фильтруется. Туда можно встроить скрипт, используя багу, которую я описывал раньше. Пишем сообщение и у друга срабатывает XSS.

Вы исправили возможность пилить ники, содержащие специальные символы через мобильную версию, но у меня осталось парочка. Прошу заметить, что у других людей и злоумышленников также могли остаться такие ники.

Пример аккаунта вам для тестов:
79601920522
90177715q

Прошу не блокировать. Данные аккаунты сейчас на вес - золото.

{F242442}

Еще скрин:

{F242440}

██████████

Спасибо.

## Impact

Злоумышленник может заюзать XSS.

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
