---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '99686'
original_report_id: '99686'
title: '[w1.dwar.ru] Core Dump'
weakness: Memory Corruption - Generic
team_handle: mailru
created_at: '2015-11-14T17:43:53.515Z'
disclosed_at: '2017-03-27T13:11:16.875Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- memory-corruption-generic
---

# [w1.dwar.ru] Core Dump

## Metadata

- HackerOne Report ID: 99686
- Weakness: Memory Corruption - Generic
- Program: mailru
- Disclosed At: 2017-03-27T13:11:16.875Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Если помните багу с HeartBleed, то там можно было читать оперативную память сервера в поисках Credential информации.

Здесь же похожая уязвимость, когда сервер crash-ится, на жестком диске остаётся дамп памяти вместе со всеми данными, которые можно анализировать для выяснения причины падения.

https://wiki.archlinux.org/index.php/Core_dump

Самая хохма, что этот дамп доступен пользователям Web.

https://w1.dwar.ru/core

Качаем дамп с указанием диапазона:

GET /core HTTP/1.1
Range: bytes=0-100099
Host: w1.dwar.ru

Меняя диапазоны байтов, получаем всякие данные...

Вот пример:

php -d memory_limit=256M -d error_log=/opt/WWWRoot/w1.dragons/wwwroot/crons/mng

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
