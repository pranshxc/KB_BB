---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150540'
original_report_id: '150540'
title: All Active user sessions should be destroyed when user change his password!
weakness: Improper Authentication - Generic
team_handle: olx
created_at: '2016-07-11T10:09:21.584Z'
disclosed_at: '2018-01-08T11:43:48.729Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- improper-authentication-generic
---

# All Active user sessions should be destroyed when user change his password!

## Metadata

- HackerOne Report ID: 150540
- Weakness: Improper Authentication - Generic
- Program: olx
- Disclosed At: 2018-01-08T11:43:48.729Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hello security,
There is an user sessions issue on your application that should be fixed.
Proof of Concept

Suppose, you have an account on olx.com
Somehow an attacker manage to get your password and logged in your account.. after knowing that your ID has been compromised what you'll do ?
i guess first thing that will popup into your head is, "I should change my password!" and you'll change the password.. maximum users just change his/her password when they recover their ID.
In " olx" changing the password doesn't destroys the other sessions which are logged in with old passwords.
As other sessions is not destroyed, attacker will be still logged in your account even after changing password, cause his session is still active.. he'll have complete access on your account till that session expires!
So, your account remains insecure even after the changing of password.

PATCH

When some change his/her password, each and every active sessions that belongs to that particular account must be destroyed!
I would recommend you to  add a process that asks users whether user want to close all open sessions or not right after changing password.

So there is two way, either you let users to choose if they want to keep active sessions or just destroy every active sessions when an users change his/her password!

Please Fix This Vulnerability AND let me know.
Looking forward to hear from you.
Best Regards,
r4hul

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
