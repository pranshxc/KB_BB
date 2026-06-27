---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '93535'
original_report_id: '93535'
title: Session retention is present which reveals the customer info
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2016-03-24T08:04:54.176Z'
disclosed_at: '2016-05-09T22:35:46.185Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# Session retention is present which reveals the customer info

## Metadata

- HackerOne Report ID: 93535
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2016-05-09T22:35:46.185Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Issue : 

Session retention is present at partner.uber.com which reveals all senstive data


Steps to reproduce :

1)Login to partner.uber.com under any driver profile
2)navigate to summary page or any page e.g payment page
3)logout the application
4)press back button of the application

application reveals the information


Impact & real time scenario :

How it affects drivers :

Imagine a driver was logging in at uber in a public system and logsout the application,now another user whom wish to know about the driver,clicks on back button of the browser to reveal the info

Technical info :

session was not cleared which makes the application to reveal all sensitive info

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
