---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '447742'
original_report_id: '447742'
title: 'SQL Injection in Login Page: https://█████/█████████/login.php'
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2018-11-20T16:11:30.338Z'
disclosed_at: '2020-05-14T16:48:11.416Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- sql-injection
---

# SQL Injection in Login Page: https://█████/█████████/login.php

## Metadata

- HackerOne Report ID: 447742
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2020-05-14T16:48:11.416Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
I believe I've discovered an error based SQL injection in the login page for https://████/██████/login.php.

**Description:**
When browsing to the webpage https://█████/██████/login.php and entering certain control characters into the "Username" field, and SQL error (Oracle) is produced.

## Impact
This is hard to gauge as I did not attempt to fully exploit the SQL injection point. Once I identified that it was an error-based SQL injection, I stopped. The website also has a Web Application Firewall and IPS implemented, so bypasses would need to be used to fully exploit it. I didn't know the rules for this program in regard to bypasses defenses with automated tools like sqlmap the --tamper parameter. 

## Step-by-step Reproduction Instructions

1. Browse to https://█████████/███/login.php
2. Enter " '; --  " into the username field
3. The error "ORA-00933: SQL command not properly ended" is produced

## Product, Version, and Configuration (If applicable)
██████████ █████████ Portal
Version: 3.0.89
Last Modified: Oct 04, 2018 

## Suggested Mitigation/Remediation Actions
Parameterized queries should be used to separate the command and data portions of the intended query to the database. These queries prevent an attacker from tampering with the query logic and extending a concatenated database query string. Code reviews should be conducted to identify any additional areas were the application or other applications in the organization are vulnerable to this attack.
Additionally, input validation should be enforced on the server side in order to ensure that only expected data is sent in queries. Where possible security specific libraries should be used in order to provide an additional layer of protection.

## Impact

A skilled attacker could likely gain access to the database for the website, and depending on the privileges of the database user, gain access to other databases or compromise the system hosting the database engine.

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
