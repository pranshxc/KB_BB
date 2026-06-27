---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '187714'
original_report_id: '187714'
title: Vine - overwrite account associated with email via android application
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2016-12-02T14:08:03.500Z'
disclosed_at: '2017-06-14T23:35:01.220Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
tags:
- hackerone
- improper-authentication-generic
---

# Vine - overwrite account associated with email via android application

## Metadata

- HackerOne Report ID: 187714
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2017-06-14T23:35:01.220Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

It's possible to deny any user from logging in to his account by overwriting the password associated with his email. This is not an account takeover because while we do override the password associated with that specific mail we just login to a "new" account and not the user's original one.

Steps to reproduce:
===
1) Create first account via Vine for android with the mail firstaccountmail@gmail.com with the password Bla123
2) You can now see that you can login to the account created above.
3) Go and create another account - this time with a different password and with the mail Firstaccountmail@gmail.com - notice the CAPS (you can put the caps everywhere on the mail).
4) Finish the creation process - and see that it succeeds
5) Now go back and try to login with firstaccountmail@gmail.com and the password Bla123 and see that you can't. However, it's possible to login with firstaccountmail@gmail.com and the second password you have created - but you"ll login to the second created account.

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
