---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '121696'
original_report_id: '121696'
title: Bypass  two-factor authentication
weakness: Improper Authentication - Generic
team_handle: slack
created_at: '2016-03-09T11:16:26.373Z'
disclosed_at: '2017-11-18T12:00:15.780Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
tags:
- hackerone
- improper-authentication-generic
---

# Bypass  two-factor authentication

## Metadata

- HackerOne Report ID: 121696
- Weakness: Improper Authentication - Generic
- Program: slack
- Disclosed At: 2017-11-18T12:00:15.780Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

If a user set 2FA, a user has to enter verification code when a user tries to reset password. 

Under the "Password Reset" page, a user can enter wrong two-factor authentication code many times. I said "many times" because your bug bounty policy stated...

Exclusions

Issues found through automated testing

So, I may not be allowed to brute force in order to check how many times a user can enter wrong 2FA codes. I didn't use any automated tools and didn't brute force for my testing.

I tested that I could still reset my password after I entered wrong 2FA codes 20 times manually. It seems that a user can brute force 2FA codes.

-----step to reproduce-----

1. A user sends a password reset message to user's registered email.

2. Go to "Password Reset" page from #1's message.

3. Set a new password and Brute force two-factor auth code

----------------------------------

After a user reset password, a user will go to slack's home page. From that page a user can do anything. 

Two factor authentication is another layer of protection. Even if a user leaked email address and password, a user will be protected by additional security(2FA). 

If an attacker hacked victim's email, an attacker will be able to take over slack's 2FA enabled account by brute forcing 2FA code on password reset page.

Recommendation: If a user entered wrong 2FA codes many times, a user will be blocked temporary.

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
