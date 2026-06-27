---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '134757'
original_report_id: '134757'
title: staff memeber can install apps even if have limitied access
weakness: Privilege Escalation
team_handle: shopify
created_at: '2016-04-26T12:20:30.814Z'
disclosed_at: '2016-05-04T22:56:12.471Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- privilege-escalation
---

# staff memeber can install apps even if have limitied access

## Metadata

- HackerOne Report ID: 134757
- Weakness: Privilege Escalation
- Program: shopify
- Disclosed At: 2016-05-04T22:56:12.471Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hey ;
for example staff member have limit access to orders
when this memeber want install app (scope read_orders)  ,error message showed :

Oauth error invalid_request: You do not have permission to access the requested scopes

bug:
-----
staff memeber can install app even if have limit access to scops
https://youtu.be/AoFLfiDDUog

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
