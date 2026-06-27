---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1081817'
original_report_id: '1081817'
title: mysql.initial.sql file is accessable for everyone
weakness: Information Disclosure
team_handle: qiwi
created_at: '2021-01-19T19:00:01.535Z'
disclosed_at: '2021-03-31T07:58:37.144Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
asset_identifier: '*.rapida.ru'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# mysql.initial.sql file is accessable for everyone

## Metadata

- HackerOne Report ID: 1081817
- Weakness: Information Disclosure
- Program: qiwi
- Disclosed At: 2021-03-31T07:58:37.144Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

здравствуйте.
я нашел mysql.initial.sql файл Roundcube Webmail initial database structure.
оно открыта для всех.
это sql файл которая создает структуру разных таблиц как user,session,cache и так далее

### PoC
* url: ```https://contact.rapida.ru/mysql.initial.sql```

{F1164134}

{F1164136}

## Impact

* information disclosure
* sql code disclosure

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
