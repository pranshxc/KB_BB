---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '723044'
original_report_id: '723044'
title: SQL INJECTION  in https://████/██████████
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2019-10-25T22:00:26.116Z'
disclosed_at: '2022-04-29T13:56:20.270Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- sql-injection
---

# SQL INJECTION  in https://████/██████████

## Metadata

- HackerOne Report ID: 723044
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2022-04-29T13:56:20.270Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Bug is : Sql injection in https://██████████/████████  via Referer
I've confirmed the vulnerability using sleep SQL queries with various arithmetic operations. The sleep command combined with the arithmetic operations will cause the server to sleep for various amounts of time depending on the result of the arithmetic operation.

##Proof of concept :
1- go to https://██████████/████████  and capture Request 
2- put this payload in Referer '+(select*from(select(sleep(6*6)))a

## Impact

##Impact :
An attacker can manipulate the SQL statements that are sent to the MySQL database and inject malicious SQL statements. The attacker is able to change the logic of SQL statements executed against the database.

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
