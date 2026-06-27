---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '577612'
original_report_id: '577612'
title: MSSQL injection via param Customwho in https://█████/News/Transcripts/Search/Sort/
  and WAF bypass
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2019-05-11T22:00:06.207Z'
disclosed_at: '2019-10-10T19:13:15.046Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- sql-injection
---

# MSSQL injection via param Customwho in https://█████/News/Transcripts/Search/Sort/ and WAF bypass

## Metadata

- HackerOne Report ID: 577612
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2019-10-10T19:13:15.046Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

MSSQL injection via param `Customwho` in https://███████/News/Transcripts/Search/Sort/

**Description:**

MSSQL injection via param `Customwho` in https://██████████/News/Transcripts/Search/Sort/

There is WAF, but we can make bypass and via global variable `@@LANGID` we can know that the base is used here - MSSQL

## Impact

Critical

## Step-by-step Reproduction Instructions

Via global variable `@@LANGID` we can find out that here is MSSQL database. ████

https://█████/News/Transcripts/Search/Sort/?Customwho=31002/**/|/**/@@LANGID

And if use a non-existing global variable, then we get an error. ██████

https://██████████/News/Transcripts/Search/Sort/?Customwho=31002/**/|/**/@@nonexisting

## Suggested Mitigation/Remediation Actions

Using prepared statement

## Impact

We can read and do other manipulations in the database. We can also try to make RCE

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
