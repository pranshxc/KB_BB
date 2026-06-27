---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '92251'
original_report_id: '92251'
title: Issue with Password reset functionality
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2015-10-04T08:36:27.427Z'
disclosed_at: '2016-05-23T21:43:54.841Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Issue with Password reset functionality

## Metadata

- HackerOne Report ID: 92251
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2016-05-23T21:43:54.841Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Dear Team,

There are password change issues with uber.
there are two issues:
1)User is not receiving notification when he reset password via password reset link.
2)Password reset link is not expiring after used once.

Good thing: when user change his info like profile update, password change. User get email notification for password change etc.

Issue: user not always gets a notification about password change. When user change his password via password reset link then such a notification is not send to the user.

Now why user should get email notification. when he reset password using password reset link,  reset link should be one time usable but user's password reset link is not getting expired and if users email account get compromised he can reset users uber account password without notifying user.

It is good practice to always send email notification for user for any user related info update.

Steps to reproduce:
1)Go on password reset link: https://login.uber.com/forgot-password
2)put email address and get password reset link on email in my case: https://login.uber.com/pw/f42ba1449f06694893f2bbdaf2d1****
3) now to check if user getting email notification: log into account and reset password from profile. user will get email notification.
4) now again change password by password reset link user will not get any notification for password change.
5) User can use same link for n number of time to reset his password.
if this link get leaked or account compromised anybody can reset legitimate users password. 

Please let me know if more details required.

Thanks & Regards,
Ninad Sarang

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
