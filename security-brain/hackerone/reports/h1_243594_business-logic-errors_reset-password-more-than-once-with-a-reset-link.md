---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '243594'
original_report_id: '243594'
title: Reset password more than once with a reset link
weakness: Business Logic Errors
team_handle: weblate
created_at: '2017-06-27T11:16:15.416Z'
disclosed_at: '2017-08-21T18:04:08.592Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- business-logic-errors
---

# Reset password more than once with a reset link

## Metadata

- HackerOne Report ID: 243594
- Weakness: Business Logic Errors
- Program: weblate
- Disclosed At: 2017-08-21T18:04:08.592Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Though passwords reset links cannot be used more than once but I found a case where one could do so.

##Reproduction Steps
1. Request a Password Reset on demo.weblate.org
2. Click the reset link in email
3. Enter a new password
4. Click `Set my password`
5. Then you'll be redirected to the login page
6. Click `reset it` again
7. Fill the email and the captcha
8. Click `Reset my Password`
9. Instead of a message to check mail, you'll be prompted with the `Password Reset form`
10. Enter a new password and set it
11. Password successfully changed again
12. Repeat from 6

Shuaib

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
