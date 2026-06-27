---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '546'
original_report_id: '546'
title: Logical issues with account settings
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-01-01T15:23:05.995Z'
disclosed_at: '2015-05-28T04:52:35.867Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- violation-of-secure-design-principles
---

# Logical issues with account settings

## Metadata

- HackerOne Report ID: 546
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2015-05-28T04:52:35.867Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

earlier email was not allowed to change ,but now there is no verification on changing email. when user try to change the password , they were asked to verify the request by entering old password. For the same reason a verification should be there on changing email.The worst part is hackone send verification mail on new mail id , and change the "join " date even on email change request.
 scenario: if some one left his account open on public computer(say office or cafe), then attacker can change the email ,verify it himself. Then abuse forgot password field to take over whole account.

Suggested mitigation: a password field can be applied(just like facebook do) or verification mail should be send on old email id registered.

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
