---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '197789'
original_report_id: '197789'
title: '[insideok.ru] Database Dump'
weakness: Improper Authentication - Generic
team_handle: ok
created_at: '2017-01-12T10:34:47.707Z'
disclosed_at: '2018-04-25T17:28:49.355Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
tags:
- hackerone
- improper-authentication-generic
---

# [insideok.ru] Database Dump

## Metadata

- HackerOne Report ID: 197789
- Weakness: Improper Authentication - Generic
- Program: ok
- Disclosed At: 2018-04-25T17:28:49.355Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

http://insideok.ru/db.sql

Внутри - учётки админов на 2016 год.

-- Хост: localhost
-- Время создания: Сен 03 2016 г., 12:00
-- Версия сервера: 5.5.47-cll-lve
-- Версия PHP: 5.4.45


# Структура таблицы `users`

`CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) unsigned NOT NULL,
  █████
  ███████
  ███████
██████████
███
██████████
███
█████████
███████
████████
█████
█████
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8 AVG_ROW_LENGTH=5461;`


# Дамп данных таблицы users

`INSERT INTO `users` (██████████) VALUES
████
███
████████
███
████
███████
████████
███████
█████
███
███
████████
███████
███████
████████
██████
████████
████
███`

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
