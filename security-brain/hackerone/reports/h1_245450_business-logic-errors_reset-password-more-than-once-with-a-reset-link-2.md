---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '245450'
original_report_id: '245450'
title: 'Reset password more than once with a reset link #2'
weakness: Business Logic Errors
team_handle: weblate
created_at: '2017-07-03T05:57:24.610Z'
disclosed_at: '2017-10-07T14:44:40.467Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- business-logic-errors
---

# Reset password more than once with a reset link #2

## Metadata

- HackerOne Report ID: 245450
- Weakness: Business Logic Errors
- Program: weblate
- Disclosed At: 2017-10-07T14:44:40.467Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Sequel to the fix on #243594, this is still possible.

##Reproduction Steps
1. Request password reset
- Load the link in email and set a new password
- Navigate to https://demo.weblate.org/accounts/reset/
- Fill the email and captcha
- You'll be prompted to enter a new password

NOTE: I figured that if action is not performed after a few minutes, then this doesn't work. 

I suggest you make the link expire after use than setting a time frame.

Best!

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
