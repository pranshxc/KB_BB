---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1624421'
original_report_id: '1624421'
title: CSRF to ATO at https://█████/user/account [HtUS]
weakness: Cross-Site Request Forgery (CSRF)
team_handle: deptofdefense
created_at: '2022-07-04T14:14:29.146Z'
disclosed_at: '2023-01-06T18:50:07.543Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF to ATO at https://█████/user/account [HtUS]

## Metadata

- HackerOne Report ID: 1624421
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: deptofdefense
- Disclosed At: 2023-01-06T18:50:07.543Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hello dod security team today while i was doing pentest on your scope
i came across
https://████████/user/account
so i register and after that tried to edit my data and the data was in json request
so i simple change content-type to
content-type application/x-www-form-urlencoded
and the data was change
and in the next step i create html file 
to edit users data with 
0 click 
which allow me to change victim email and leads to account takeover
check my html poc file and video

## Impact

account takeover

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
