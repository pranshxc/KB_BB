---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '230076'
original_report_id: '230076'
title: Takeover of an account via reset password options after removing the account
weakness: Improper Authentication - Generic
team_handle: weblate
created_at: '2017-05-20T06:53:22.466Z'
disclosed_at: '2017-06-13T15:41:17.436Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Takeover of an account via reset password options after removing the account

## Metadata

- HackerOne Report ID: 230076
- Weakness: Improper Authentication - Generic
- Program: weblate
- Disclosed At: 2017-06-13T15:41:17.436Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, 

The Reset password mechanism can't validate or authenticate an user properly. After removing a user account it's possible to takeover the user account by using reset password option. which is turn into takeover an account. 

##Step to Reproduce: 

1. Go to [weblate](https://demo.weblate.org)
2. Remove your account from [weblate](https://demo.weblate.org)
3. Now go to for [login](https://demo.weblate.org/accounts/login/)
4. Enter username or email and password, try to login. you are failed to login because email and password is removed
5. Now click on [reset it](https://demo.weblate.org/accounts/reset/)
6. Enter email and captcha and hit `Reset my password`
{F186309}
7. Open mail and click on reset password link 
{F186311}
8. Now enter Password twice and login to the account 

After doing all the steps you are successfully able to change the password.
{F186313}

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
