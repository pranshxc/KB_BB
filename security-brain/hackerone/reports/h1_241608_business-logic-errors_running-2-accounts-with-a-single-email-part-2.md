---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '241608'
original_report_id: '241608'
title: Running 2 accounts with a single email [Part 2]
weakness: Business Logic Errors
team_handle: weblate
created_at: '2017-06-20T08:28:57.327Z'
disclosed_at: '2017-10-07T14:44:59.575Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- business-logic-errors
---

# Running 2 accounts with a single email [Part 2]

## Metadata

- HackerOne Report ID: 241608
- Weakness: Business Logic Errors
- Program: weblate
- Disclosed At: 2017-10-07T14:44:59.575Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Following the fix on #224072, I decided to try this in another way and it worked!

##Reproduction Steps
1. Login with Github on Browser1 and set a password to it.
- With another email, signup on Weblate on Browser2
- In the new account on  Browser2, do the following:
> Confirm email and Set a Password
Add a Google Account with the same email used to signup Github
Now, disconnect the email used to signup
So, it the email is default to same email on the other account

4. Reload both browsers to confirm, https://hosted.weblate.org/accounts/profile/#account
- Logout any of the browsers
- Trying to login with the email and any of the set passwords pops an **Internal Server Error**

Accompanying screenshots are attached below.

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
