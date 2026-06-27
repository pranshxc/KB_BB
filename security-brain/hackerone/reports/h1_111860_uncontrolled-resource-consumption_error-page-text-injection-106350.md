---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '111860'
original_report_id: '111860'
title: 'Error Page Text Injection #106350'
weakness: Uncontrolled Resource Consumption
team_handle: withinsecurity
created_at: '2016-01-20T14:30:40.259Z'
disclosed_at: '2016-03-18T19:16:43.119Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Error Page Text Injection #106350

## Metadata

- HackerOne Report ID: 111860
- Weakness: Uncontrolled Resource Consumption
- Program: withinsecurity
- Disclosed At: 2016-03-18T19:16:43.119Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team ,

####Description : 
This report is similar to #106350 , as we can see in report an user or attacker is __able to inject his text__ into error page and can trap to user to visit other site by adding following link  `/test/%2f../It%20has%20been%20changed%20by%20a%20new%20one%20https://www.Attacker.com%20so%20go%20to%20the%20new%20one%20since%20this%20one` after the Domain name , and it got fixed after that report with static 404 error page , 

but i got place where __old fix is not getting apply__ , so i hope u will like to fix this too .

####POC URL : https://withinsecurity.com/wp-admin/test/%2f../It%20has%20been%20changed%20by%20a%20new%20one%20https://www.Attacker.com%20so%20go%20to%20the%20new%20one%20since%20this%20one

Please let me know if any more info needed !

__Thank You
Geekboy :)__

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
