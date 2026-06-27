---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7931'
original_report_id: '7931'
title: Issue with remember_user_token
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-04-17T21:30:55.231Z'
disclosed_at: '2015-05-28T04:48:47.701Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Issue with remember_user_token

## Metadata

- HackerOne Report ID: 7931
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2015-05-28T04:48:47.701Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When a user logs out, cookie named remember_user_token is invalidated on the user side. When the user log in again with functionality 'remember me for a week', he gets the same value of  remember_user_token as previously. 

Moreover, when there is only cookie named remember_user_token in request, the user gets the same value of remember_user_token in forthcoming response.

As it can be seen in the aforementioned cases, remember_user_token is not regenerated, what constitutes a weakness in lifecycle of this cookie.

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
