---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15777'
original_report_id: '15777'
title: Process of changing email address and password does not asks old Password.
weakness: Improper Authentication - Generic
team_handle: automattic
created_at: '2014-06-09T19:48:35.506Z'
disclosed_at: '2014-07-11T00:53:40.012Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Process of changing email address and password does not asks old Password.

## Metadata

- HackerOne Report ID: 15777
- Weakness: Improper Authentication - Generic
- Program: automattic
- Disclosed At: 2014-07-11T00:53:40.012Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

This Vulnerability could be destructive if The user uses a shared computer,or if he uses wordpress in a cyber cafe and forgets to logout from wordpress.
If any user uses his wordpress account in some other computer and forgets to logout,his accounts remain insecure.I was wondered that wordpress did not asked me to enter my password before changing the email address/password of my account.
So,in this particular case,if someone forgets to logout from wordpress after using on shared computer, or think that while he was using wordpress on some others computer at that time something happens with his connection.That time he will be unable to logout from wordpress .And his account will be in deep danger.
Cause anyone who have access to the account can change the account email address/password and takeover the account.As the process does not require to enter his old password for verification.

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
