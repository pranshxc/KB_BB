---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '983710'
original_report_id: '983710'
title: SQL injection when configuring a database
weakness: SQL Injection
team_handle: impresscms
created_at: '2020-09-16T18:31:34.940Z'
disclosed_at: '2021-01-14T21:33:09.846Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: https://github.com/impresscms/impresscms
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- sql-injection
---

# SQL injection when configuring a database

## Metadata

- HackerOne Report ID: 983710
- Weakness: SQL Injection
- Program: impresscms
- Disclosed At: 2021-01-14T21:33:09.846Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I found a SQL Injection in the form of a system install (Database configuration)

## Steps To Reproduce:
- Run command: `git clone https://github.com/ImpressCMS/impresscms.git`
- Stop at a menu item: `Database configuration`
- In the `Database name` field, insert the following exploit:


```sql
 impresscms`;create database `vuln
```

{F990522}

-  Submit the form

{F990524}

- Two databases (`impresscms`, `vuln`) created successfully. POC is attached to the report

## Supporting Material/References:
[PHP addslashes](https://www.php.net/manual/en/function.addslashes.php) - single quote ('), double quote ("), backslash, NUL (the NUL byte), but **Backtick is not escaped!**

## Impact

Executing arbitrary code on a database

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
