---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '30008'
original_report_id: '30008'
title: Выполнение кода PHP через FastCGI
team_handle: mailru
created_at: '2014-10-05T02:27:14.555Z'
disclosed_at: '2015-12-11T10:59:09.814Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
---

# Выполнение кода PHP через FastCGI

## Metadata

- HackerOne Report ID: 30008
- Weakness: 
- Program: mailru
- Disclosed At: 2015-12-11T10:59:09.814Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте,
Уязвимость существует на http://bw.mail.ru/

любой файл можно воспроизвести как php

http://bw.mail.ru/robots.txt
http://bw.mail.ru/robots.txt/c37hun.php

http://bw.mail.ru/layout/all//img/img_mailru.gif
http://bw.mail.ru/layout/all//img/img_mailru.gif/c37hun.php

А для исправления Вам нужно добавить cgi.fix_pathinfo = 0 в php.ini

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
