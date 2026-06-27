---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161924'
original_report_id: '161924'
title: Password Reset Link issue
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2016-08-21T12:28:08.191Z'
disclosed_at: '2016-09-23T12:16:57.893Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-authentication-generic
---

# Password Reset Link issue

## Metadata

- HackerOne Report ID: 161924
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2016-09-23T12:16:57.893Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
i found out about an issue in your password reset links and their expiration
Steps to reproduce:
Request a password reset link to an account
Login to the account afterwards
Logout and use the link to reset the password
The link would not be expired

Now i know that the links need to expire after a certain time, but thinking logically there is no point of keeping the link alive once the user has logged in, It indicates the possibility that the user's original email has been compromised and the attacker has requested the link, This way the user's account can be compromised.

Attack Scenario:
Attacker requests the password reset link, User logs in, Link does not expire even after that. The attacker can use the link easily. Infact requesting a link when the account is logged in from a location should be prohibited to prevent compromise

I think this should be fixed, 
Thanks

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
