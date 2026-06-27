---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '126377'
original_report_id: '126377'
title: Changing Driver Passwords With Only an Authenticated Session (no password,
  no email)
weakness: Violation of Secure Design Principles
team_handle: uber
created_at: '2016-03-27T20:40:16.011Z'
disclosed_at: '2016-06-13T22:21:38.390Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Changing Driver Passwords With Only an Authenticated Session (no password, no email)

## Metadata

- HackerOne Report ID: 126377
- Weakness: Violation of Secure Design Principles
- Program: uber
- Disclosed At: 2016-06-13T22:21:38.390Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

It is possible to completely take over a driver's account with only an authenticated session. If a driver is logged on and wants to change their password, they will be asked for their current password (```changePassword.png```), but when they want to change their email, they are not asked for their current password (```changeEmail.png```).  Once a driver's email has been changed, it is trivial to reset their password through the password reset page (which only requires access to the driver's email account). 

So the steps to take over a driver's account from an authenticated session are: 

1. Change the driver's email to something that is attacker controlled
2. Log out
3. Use the forgot your password page to have a reset link sent to the attacker controlled email
4. Use the link to reset the driver's password

In order to fix this, you have to add password authentication for changing the email associated with the account (or do what you do for riders and not allow changing the email). 

Thanks,
David Dworken

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
