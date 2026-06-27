---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '685007'
original_report_id: '685007'
title: Password Reset Link not expiring after changing the email Leads To Account
  Takeover
weakness: Improper Authentication - Generic
team_handle: imgur
created_at: '2019-08-30T10:37:07.483Z'
disclosed_at: '2019-12-03T15:30:01.609Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 71
tags:
- hackerone
- improper-authentication-generic
---

# Password Reset Link not expiring after changing the email Leads To Account Takeover

## Metadata

- HackerOne Report ID: 685007
- Weakness: Improper Authentication - Generic
- Program: imgur
- Disclosed At: 2019-12-03T15:30:01.609Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

###Vulnerability:
Password Reset Link not expiring after changing the email

###Proof Of Concept:

1.Send the password reset link to your email.
2.Don`t open the password link just copy it and paste into any editor.
3.Open your account.
4.Go to your account settings.
5.Under account, you will see Account Overview.
6.Go to the Email and password Option and change the email and verify it.
7.After changing the email go to your password reset link which you copied.
8.Change your password.


BooM password Changed.

#####Thanks

## Impact

The attacker can still change the password if victim thinks his/her account is compromised and decided to change his/her email.

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
