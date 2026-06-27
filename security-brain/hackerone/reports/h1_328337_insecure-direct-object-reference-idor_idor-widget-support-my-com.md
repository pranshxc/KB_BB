---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '328337'
original_report_id: '328337'
title: IDOR widget.support.my.com
weakness: Insecure Direct Object Reference (IDOR)
team_handle: mailru
created_at: '2018-03-21T16:31:56.558Z'
disclosed_at: '2018-04-26T15:02:48.778Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: '*.lootdog.io'
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR widget.support.my.com

## Metadata

- HackerOne Report ID: 328337
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: mailru
- Disclosed At: 2018-04-26T15:02:48.778Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

На lootdog.io можно обратиться в службу поддержки. Когда мы создали тикет и хотим его подгрузить, то выполняется запрос http://widget.support.my.com/ticket/view/2918863?authentication_type=2&project_id=777777783&████████&device_id=undefined&idfa=&locale=ru_RU&format=json&callback=angular.callbacks._5&proxy= .
После view/ мы можем ввести чужой номер тикета и увидеть переписку между пользователем и службой поддержки. Например http://widget.support.my.com/ticket/view/291886?authentication_type=2&project_id=777777783&█████████&device_id=undefined&idfa=&locale=ru_RU&format=json&callback=angular.callbacks._5&proxy= .

## Impact

Можно просматривать все тикеты support.my.com

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
