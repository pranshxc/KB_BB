---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '23921'
original_report_id: '23921'
title: broken authentication
weakness: Improper Authentication - Generic
team_handle: concretecms
created_at: '2014-08-12T21:38:17.827Z'
disclosed_at: '2014-09-21T03:58:39.924Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# broken authentication

## Metadata

- HackerOne Report ID: 23921
- Weakness: Improper Authentication - Generic
- Program: concretecms
- Disclosed At: 2014-09-21T03:58:39.924Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

Steps to Replicate:-

1) Create a concrete5 account.
2) request a Password Reset link in Email( don't use it)
3) Login with the Desired Password
4) Change the Password Several Times From Settings ( This destroys all the Active Sessions) in my case i've made upto 10 Password changes.
5) After several password changes, you can use that Password reset link( mentioned in Step 2) to change your Password.

I would Suggest Expiring all the Password Reset tokens After Several Successful Password Changes has been made to the Account. Supposing That these Changes are made by the User of the account itself, Because an Active Password token After Several Session Destructions Should not be Active anymore.

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
