---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '343752'
original_report_id: '343752'
title: lootdog.io XSS
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mailru
created_at: '2018-04-26T22:17:15.857Z'
disclosed_at: '2018-06-04T09:26:07.952Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: '*.lootdog.io'
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# lootdog.io XSS

## Metadata

- HackerOne Report ID: 343752
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mailru
- Disclosed At: 2018-06-04T09:26:07.952Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

В данной ссылке можно наблюдать опенредирект:

1. https://lootdog.io/register?next=http://mail.ru?https%3A%2F%2Flootdog.io%2F

Заполняем эту форму, подтверждаем номер:
{F290679}

Нас перекидывает на http://mail.ru

## Impact

open redirect

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
