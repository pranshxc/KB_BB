---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '390359'
original_report_id: '390359'
title: SOAP WSDL Parser SQL Code Execution
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2018-08-03T22:44:59.457Z'
disclosed_at: '2019-01-16T19:16:49.737Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 29
tags:
- hackerone
- sql-injection
---

# SOAP WSDL Parser SQL Code Execution

## Metadata

- HackerOne Report ID: 390359
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2019-01-16T19:16:49.737Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
SOAP WSDL Parser SQL Code Execution

**Description:**
It was possible to parse WSDL resources and read all functions from the SOAP Admin Panel, therefor i was able to repeat the sql query with a tampered request with my own custom SQL command.
i was able to extract all the database names for PoC, there is no doubt in my mind that i could login to the admin panel and compromise the entire DoD Information System.

## Impact
Remote Code Execution

## Step-by-step Reproduction Instructions

1. Visit:███ and go to the staff links 'CIMScan'
Image: █████/34570b2eaa899ae001e1bc666be3546a.png
2. ████/c400bc1369bddeca580646b14c38a562.png
3. ████/32e085f593bfbf8599359d968cf52dc0.png

## Product, Version, and Configuration (If applicable)
Web Application

## Suggested Mitigation/Remediation Actions
I will report it to CIMScan since i am not sure if this affect's your code, it might very well be the code of CIMScan which in that case you will need to remove it from your website to prevent employees from being compromised.

## Impact

Remote Code Execution

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
