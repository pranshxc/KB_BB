---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '10377'
original_report_id: '10377'
title: All Active user sessions should be destroyed when user change his password!
weakness: Violation of Secure Design Principles
team_handle: c2fo
created_at: '2014-04-30T03:25:25.971Z'
disclosed_at: '2014-09-23T00:15:39.978Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# All Active user sessions should be destroyed when user change his password!

## Metadata

- HackerOne Report ID: 10377
- Weakness: Violation of Secure Design Principles
- Program: c2fo
- Disclosed At: 2014-09-23T00:15:39.978Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
There is an user sessions issue on your application that should be fixed.

Proof of Concept
------------------------
Suppose, you have an account on *C2FO* (app.c2fo.com).
Somehow an attacker manage to get your password and logged in your account.. after knowing that your ID has been compromised what you'll do ?
i guess first thing that will popup into your head is, "I should change my password!" and you'll change the password.. maximum users just change his/her password when they recover their ID.
in *C2FO*, changing the password doesn't destroys the other sessions which are logged in with old passwords.
As other sessions is not destroyed, attacker will be still logged in your account even after changing password, cause his session is still active.. he'll have complete access on your account till that session expires!
So, your account remains insecure even after the changing of password.

PATCH
----------

* When some change his/her password, each and every active sessions that belongs to that particular account must be destroyed!
*  I would recommend you to follow Facebook on this security issue.. They fixed this issue few months back by adding a process that asks users whether user want to close all open sessions or not right after changing password.

So there is two way, either you let users to choose if they want to keep active sessions or just destroy every active sessions when an users change his/her password!

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
