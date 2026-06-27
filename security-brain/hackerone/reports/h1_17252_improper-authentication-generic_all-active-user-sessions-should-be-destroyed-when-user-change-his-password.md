---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17252'
original_report_id: '17252'
title: All Active user sessions should be destroyed when user change his password!
weakness: Improper Authentication - Generic
team_handle: uzbey
created_at: '2014-06-23T02:02:14.475Z'
disclosed_at: '2014-07-30T20:56:00.450Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# All Active user sessions should be destroyed when user change his password!

## Metadata

- HackerOne Report ID: 17252
- Weakness: Improper Authentication - Generic
- Program: uzbey
- Disclosed At: 2014-07-30T20:56:00.450Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
There is an user sessions issue on your application that should be fixed.

Proof of Concept
------------------------
Suppose, you have an account on **uzbey**
Somehow an attacker manage to get your password and logged in your account.. after knowing that your ID has been compromised what you'll do ?
i guess first thing that will popup into your head is, "I should change my password!" and you'll change the password.. maximum users just change his/her password when they recover their ID.
in **uzbey**, changing the password doesn't destroys the other sessions which are logged in with old passwords.
(Logging in with the new password doesn't invalidate the older sessions either)
As other sessions is not destroyed, attacker will be still logged in your account even after changing password, cause his session is still active.. he'll have complete access on your account till that session expires!
So, your account remains insecure even after the changing of password.

PATCH
----------

* When someone change his/her password, each and every active sessions that belongs to that particular account must be destroyed!
* I would recommend you to follow Facebook on this security issue.. They fixed this issue few months back by adding a process that asks users whether user want to close all open sessions or not right after changing password.

So there is two way, either you let users to choose if they want to keep active sessions or just destroy every active sessions when users change his/her password!

I look forward to hearing from you!

Thanks and Best Wishes.

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
