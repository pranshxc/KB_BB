---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1296597'
original_report_id: '1296597'
title: Business logic error
weakness: Business Logic Errors
team_handle: upchieve
created_at: '2021-08-09T18:05:33.495Z'
disclosed_at: '2021-08-11T17:46:25.198Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 0
asset_identifier: hackers.upchieve.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Business logic error

## Metadata

- HackerOne Report ID: 1296597
- Weakness: Business Logic Errors
- Program: upchieve
- Disclosed At: 2021-08-11T17:46:25.198Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi UPCHIEVE SECURITY TEAM

I'm Anto

Vulnerability :
Business logic error
There is no password verification while changing a password.

Steps to Reproduce :
1). Go to (https://hackers.upchieve.org/resetpassword).
2). Click the change password.
3). If your old password was ex:  hacker and in new password enter the same password ex: hacker.
4). The password will be updated.

There is no password check mechanism on there.
Fix it by making an alert
" Your new password must be different"

## Impact

Business logic error
Please let me know if this can be fixed :)

Regards,
Anto

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
