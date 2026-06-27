---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '118965'
original_report_id: '118965'
title: Distinguish EP+Private vs Private programs in HackerOne
weakness: Information Disclosure
team_handle: security
created_at: '2016-02-26T16:10:25.076Z'
disclosed_at: '2016-04-25T05:03:36.832Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Distinguish EP+Private vs Private programs in HackerOne

## Metadata

- HackerOne Report ID: 118965
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2016-04-25T05:03:36.832Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi! I would like to provide the following matrix in order to distinguish between EP+Private vs Private programs in HackerOne, without the need to login.

I am using two endpoints. These are:
1. https://hackerone.com/ENTITY/thanks/2012.json and
2. https://hackerone.com/ENTITY/thanks/2013.json

If ENTITY is SANDBOX the response in 1 is 401 and the response in 2 is 401
If ENTITY is EP the response in 1 is 500 and the response in 2 is 401
If ENTITY is EP+Private  the response in 1 is 500 and the response in 2 is 401
If ENTITY is Private the response in 1 is 401 and the response in 2 is 401
If ENTITY is Public the response in 1 in 500 and the response in 2 is 200
If ENTITY is User the response in 1 is 404 and the response in 2 is 404

As you may see from the above matrix, you can distinguish between EP+Private and Private programs based on the Return number.

Thanks!

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
