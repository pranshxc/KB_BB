---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '255021'
original_report_id: '255021'
title: Profile shows incorrect account creation date
team_handle: legalrobot
created_at: '2017-07-30T17:47:25.104Z'
disclosed_at: '2017-07-31T04:29:22.775Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# Profile shows incorrect account creation date

## Metadata

- HackerOne Report ID: 255021
- Weakness: 
- Program: legalrobot
- Disclosed At: 2017-07-31T04:29:22.775Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I get to know that you are using showing joined time. it's contain design issue. I think that you show for once user login in to their account and it should show from howmany minutes that user logged in?
but i can see here a design issue, is that whenever we refresh page https://app.legalrobot.com/account , it started from 0 seconds.

here i can see that function issue, that is reset to 0 after every page reset. (https://app.legalrobot.com/account). it should reset only at logout time.

Thanks,
Vishal.

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
