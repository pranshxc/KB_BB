---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13602'
original_report_id: '13602'
title: Session not expired on logout
team_handle: factlink
created_at: '2014-05-27T10:41:45.964Z'
disclosed_at: '2014-07-08T10:00:32.423Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
---

# Session not expired on logout

## Metadata

- HackerOne Report ID: 13602
- Weakness: 
- Program: factlink
- Disclosed At: 2014-07-08T10:00:32.423Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

factlink is  not  expiring  sessions immediately  after logout

1. log on to https://staging.factlink.com/

2. Open HTTP LIVE  HEADERS  and  login in https://staging.factlink.com/  with your correct  username and password  
3. capture  request for ex click on settings   ( https://staging.factlink.com/user/user_name/edit)
4.and  immediately logout  the  website 

5.   replay  the  captured request    and  your logged  back into  your account  without  any username and password

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
