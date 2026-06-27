---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '11927'
original_report_id: '11927'
title: Stored XSS on http://cards.mail.ru
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-05-13T12:23:15.140Z'
disclosed_at: '2014-12-10T19:09:03.423Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS on http://cards.mail.ru

## Metadata

- HackerOne Report ID: 11927
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2014-12-10T19:09:03.423Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Эксперементируя с html редактором на странице отправки открытки http://cards.mail.ru/card/compose.html?cid=7842
был найден вектор, который проходит проверки и остаётся:
asdf<br>
<iframe src=javascript:alert(2) <
В итоге, хранимый xss на страницах
http://cards.mail.ru/card/status.html?fcid=acff40d2aad6a1bb49ba650788b0806f
и 
http://cards.mail.ru/card/receive.html?tcid=bef7886ed4771bb6de75d026c0105b6f
Последняя ссылка попадает напрямую в почтовый ящик жертвы.

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
