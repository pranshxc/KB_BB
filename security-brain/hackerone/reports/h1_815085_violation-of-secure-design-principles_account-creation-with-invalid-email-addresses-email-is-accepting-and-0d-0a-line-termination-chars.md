---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '815085'
original_report_id: '815085'
title: Account creation with invalid email addresses / email is accepting % and %0d%0a
  line termination chars
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2020-03-09T13:56:00.538Z'
disclosed_at: '2024-02-04T16:58:28.007Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 139
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Account creation with invalid email addresses / email is accepting % and %0d%0a line termination chars

## Metadata

- HackerOne Report ID: 815085
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2024-02-04T16:58:28.007Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hackerone SignUp feature is misconfigured with email parameter. Email address parameter is accepting % and %0d%0a character along with genuine email address. Using this technique hackerone user account can be created but cannot be verified as there is not possible to verify those invalid email accounts. Basically random use of invalid email address, attacker can create multiple accounts.

**Description:**
As email address field always being verified with any special character (except @ and .) but here email is accepting % and line termination char %0d%0a

### Steps To Reproduce

1. SignUp with new hacker account 
2. Use email address adding with character like % or %0d%0a, account will be created and you will get a account creation message
████ ███████
{F742080}
3. Even if you try now to login using same above email and password then you will get same message for account is already created and need to verify email
█████
4. You can not use the same invalid email again, as it will show an error of reuse of that invalid email address

## Impact

>>Garbage value can be stored in database using user account signup form
>>Multiple account can be created, just like if any use has real account with his email address, then also account can be created by adding %0d%0a or % char
>>Account is created using invalid email address, but can not be used

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
