---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1072277'
original_report_id: '1072277'
title: Host Header injection in oslo.io (using X-Forwarded-For header) leading to
  email spoofing
weakness: Business Logic Errors
team_handle: logitech
created_at: '2021-01-05T21:03:32.373Z'
disclosed_at: '2021-01-07T21:18:41.842Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
asset_identifier: '*.oslo.io'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Host Header injection in oslo.io (using X-Forwarded-For header) leading to email spoofing

## Metadata

- HackerOne Report ID: 1072277
- Weakness: Business Logic Errors
- Program: logitech
- Disclosed At: 2021-01-07T21:18:41.842Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#Hello team
##I hope it will be a happy year for you and for me 😇 
## Summary:

I found Host Header injection in oslo.io  
I tried to use it to show the security effect on users And I found this

## Steps To Reproduce:

 1. Well, first of all, enter your project 
2.Make an invitation by email 
3.Now through the burpsuite 
If we try to change the host, 403 will appear
  {F1145857}

So we will use  ```X-Forwarded-Host:  example.com```
 
PoC : 
{F1145858}

## Impact

Many things can be done, including deceiving the user and referring to something else or a login page and stealing their account
>>There is a lot of information about it here : 

 https://portswigger.net/web-security/host-header

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
