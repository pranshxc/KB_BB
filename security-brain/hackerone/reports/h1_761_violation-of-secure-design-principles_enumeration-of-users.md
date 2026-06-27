---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '761'
original_report_id: '761'
title: Enumeration of users
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-01-19T20:22:02.156Z'
disclosed_at: '2014-10-03T20:34:10.540Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 20
tags:
- hackerone
- violation-of-secure-design-principles
---

# Enumeration of users

## Metadata

- HackerOne Report ID: 761
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2014-10-03T20:34:10.540Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

As I can see, you prevent enumeration of users (actually e-mails of registered users) in Sign In (https://hackerone.com/users/sign_in) and Forgot password (https://hackerone.com/users/password/new) functionalities. However, the users can be enumerated in Sign Up (https://hackerone.com/users/sign_up) - just enter existing and non-existent e-mail addresses and see the responses. To prevent enumeration of users - ask the user in the first step to enter e-mail and tell him/her  that the next instructions will be sent to this mail to finish the registration process. When the mail is already registered - tell the user about it in the mail. When it is not registered, the user gets an unique URL in the mail to continue the registration process.

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
