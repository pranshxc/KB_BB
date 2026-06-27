---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1109311'
original_report_id: '1109311'
title: SQL injection in  https://www.acronis.cz/ via the log parameter
weakness: SQL Injection
team_handle: acronis
created_at: '2021-02-23T07:48:46.695Z'
disclosed_at: '2021-06-11T12:58:04.810Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 96
asset_identifier: Other Acronis Domains
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- sql-injection
---

# SQL injection in  https://www.acronis.cz/ via the log parameter

## Metadata

- HackerOne Report ID: 1109311
- Weakness: SQL Injection
- Program: acronis
- Disclosed At: 2021-06-11T12:58:04.810Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I have discovered a SQL injection in https://www.acronis.cz/ using the POST request via the log parameter.
Using sqlmap, I have retrieved the current user: 'u_acronis@localhost''

The command used:
sqlmap  -p log -r request-cz.txt --current-user  --level=2 --risk=2

I did not perform any other actions.

## Impact

An attacker can use SQL injection it to bypass a web application's authentication and authorization mechanisms and retrieve the contents of an entire database.
This can also be used by an attacker to execute OS commands, which may then be used to escalate an attack even further.

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
