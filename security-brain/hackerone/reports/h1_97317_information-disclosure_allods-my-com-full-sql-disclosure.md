---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '97317'
original_report_id: '97317'
title: '[allods.my.com] Full SQL Disclosure'
weakness: Information Disclosure
team_handle: mailru
created_at: '2015-11-02T20:37:49.317Z'
disclosed_at: '2017-03-03T13:14:41.555Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# [allods.my.com] Full SQL Disclosure

## Metadata

- HackerOne Report ID: 97317
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2017-03-03T13:14:41.555Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Уязвимость имеет ту же природу, что и в #96729 и в #96727.

Уязвимость возникает вследствие чтения ошибок через включенный Debug-режим.

И там, и там - раскрытие информации за счёт debug-режима.

Но для того, что бы раскрыть SQL запрос необходимо произвести Stress-тест многочисленными запросами любой страницы форума.

Для примера - вот этой.

http://allods.my.com/forum/index.php?boardID=123&l=1&page=Board

В следствие натравлении фаззера (или просто циклического запроса страницы) таблица сессий будет переполнена. А так как Debug режим включен - мы увидим долгожданную ошибку.

Fatal error: Invalid SQL: INSERT INTO wcf1_session (sessionID, packageID, userID, ipAddress, userAgent, lastActivityTime, requestURI, requestMethod, username) VALUES ('00923087f58eaf5be62214f0c2d2d78e3b35d45b', 48, 0, '10.0.0.1', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21', 1446431403, '/forum/index.php?boardID=123&l=1&page=Board', 'GET', '' )

You get more information about the problem in our knowledge base: http://www.woltlab.com/help/?code=1114

Information:
error message: Invalid SQL: INSERT INTO wcf1_session (sessionID, packageID, userID, ipAddress, userAgent, lastActivityTime, requestURI, requestMethod, username) VALUES ('00923087f58eaf5be62214f0c2d2d78e3b35d45b', 48, 0, '10.0.0.1', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21', 1446431403, '/forum/index.php?boardID=123&l=1&page=Board', 'GET', '' )
error code: 1114
sql type: MySQLDatabase

sql error: The table 'wcf1_session' is full

sql error number: 1114
sql version: 
php version: 5.3.10-1ubuntu3.9
wcf version: 1.1.10 pl 2 (Tempest)
date: Mon, 02 Nov 2015 02:30:03 +0000
request: /forum/index.php?boardID=123&l=1&page=Board

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
