---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '245334'
original_report_id: '245334'
title: Lack of Password Confirmation When Changing Email
weakness: Violation of Secure Design Principles
team_handle: wakatime
created_at: '2017-07-02T13:06:15.472Z'
disclosed_at: '2017-07-03T06:49:30.028Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- violation-of-secure-design-principles
---

# Lack of Password Confirmation When Changing Email

## Metadata

- HackerOne Report ID: 245334
- Weakness: Violation of Secure Design Principles
- Program: wakatime
- Disclosed At: 2017-07-03T06:49:30.028Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

When any user wants to change the password, current password is asked for proceeding the request. This should also be implemented on changing the email.

Attack Scenerio :  When some forget to logout from the account in a publc computer, anyone can change the email to its own and verify it. And after that using the forget password feature, it can change the password too.

Reference From : #546

Best Regards,
Pratyush Janghel

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
