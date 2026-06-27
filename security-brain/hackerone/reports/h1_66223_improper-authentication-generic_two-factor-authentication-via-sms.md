---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '66223'
original_report_id: '66223'
title: Two-factor authentication (via SMS)
weakness: Improper Authentication - Generic
team_handle: coinbase
created_at: '2015-06-05T22:22:51.813Z'
disclosed_at: '2015-06-16T18:45:52.934Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Two-factor authentication (via SMS)

## Metadata

- HackerOne Report ID: 66223
- Weakness: Improper Authentication - Generic
- Program: coinbase
- Disclosed At: 2015-06-16T18:45:52.934Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Coinbase Security Team

I just found a problem in Two-factor authentication mechanism, here is the details and how to reproduce this issue:

I have two accounts with two emails on `coinbase.com` i active `2FA` on the both of two emails with this phone number `+201066462288`.

From `Chrome` i will try to login using my first email `a_diaa_2007@yahoo.com` and now i recieved my code related to this email here `6020930`.

From `FireFox` i will try to do the same thing using my second email `diaa.diab.2012@gmail.com` and now i recieved my second code for the second email `1091566`.

Logically, the following steps must be excuted to make the two accounts be logged in:

`a_diaa_2007@yahoo.com` => `6020930`
`diaa.diab.2012@gmail.com` => `1091566`

But the problem is when i change the two code and emails to be 
`a_diaa_2007@yahoo.com` => `1091566`
`diaa.diab.2012@gmail.com` => `6020930`

I found myself be logged in with two accounts and there is no problem there, The exactly problem is you allow accounts that have the same number to be logged in with each other verification code if they request a login via SMS.

Thank you.
Diaa

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
