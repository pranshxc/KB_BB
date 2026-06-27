---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '351361'
original_report_id: '351361'
title: Administrator can create user without entering high security mode
weakness: Improper Authentication - Generic
team_handle: phabricator
created_at: '2018-05-14T09:56:08.683Z'
disclosed_at: '2018-05-22T09:27:26.906Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- improper-authentication-generic
---

# Administrator can create user without entering high security mode

## Metadata

- HackerOne Report ID: 351361
- Weakness: Improper Authentication - Generic
- Program: phabricator
- Disclosed At: 2018-05-22T09:27:26.906Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When an administrator wants to create a user, he can go to https://phabricator.example.com/people/create/ and will be required to enter his MFA token in order to enter high security mode.

However, if an administrator goes to https://phabricator.example.com/people/new/standard/ he will bypass the choice of user type and go straight to the new standard user form. This form allows the administrator to create a new user without entering high security mode.

mongoose

## Impact

The attacker could create a user account for someone that is not supposed to have access to Phabricator, or for himself in order to keep his access to Phabricator after losing access to the (compromised) administrator account.

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
