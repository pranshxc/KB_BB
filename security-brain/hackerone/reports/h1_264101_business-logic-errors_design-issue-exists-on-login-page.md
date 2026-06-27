---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '264101'
original_report_id: '264101'
title: design issue exists on login page
weakness: Business Logic Errors
team_handle: legalrobot
created_at: '2017-08-28T16:57:40.953Z'
disclosed_at: '2017-08-28T17:48:02.229Z'
has_bounty: false
visibility: full
substate: spam
vote_count: 11
asset_identifier: app.legalrobot.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# design issue exists on login page

## Metadata

- HackerOne Report ID: 264101
- Weakness: Business Logic Errors
- Program: legalrobot
- Disclosed At: 2017-08-28T17:48:02.229Z
- Has Bounty: No
- Visibility: full
- Substate: spam

## Original Report

legalrobot allows an user to set email as password only by resetting password either by logged in and changing it into profile

password changed succesfully 

but the user couldn't log in to the app.legalrobot.com 
because 

js checks with email and password and it states it couldn't be same 

also not allowing the user to log in 

Design issues 

{F216519}

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
