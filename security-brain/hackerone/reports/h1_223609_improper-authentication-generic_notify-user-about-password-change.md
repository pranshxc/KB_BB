---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223609'
original_report_id: '223609'
title: Notify user about password change
weakness: Improper Authentication - Generic
team_handle: weblate
created_at: '2017-04-24T23:29:21.806Z'
disclosed_at: '2017-05-17T18:14:12.437Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Notify user about password change

## Metadata

- HackerOne Report ID: 223609
- Weakness: Improper Authentication - Generic
- Program: weblate
- Disclosed At: 2017-05-17T18:14:12.437Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

There is an issue with password reset functionality with Weblate: user is not receiving notification when he reset password.

Good thing: when user change his info like profile update, password change. User get email notification for password change etc.

Issue: user not always gets a notification about password change. When user change his password then a notification is not send to the user.

It is good practice to always send email notification for user when a password change.

Please let me know if more details required.

thanks

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
