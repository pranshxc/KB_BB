---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '118718'
original_report_id: '118718'
title: User with Read-Only permissions can manually public disclosure the report
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2016-02-25T09:24:49.046Z'
disclosed_at: '2016-04-21T01:55:24.892Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# User with Read-Only permissions can manually public disclosure the report

## Metadata

- HackerOne Report ID: 118718
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-04-21T01:55:24.892Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I would like to report an incomplete fix of #109483 this report .manually disclose functionality is not consider for fix that cause read-only team members to post a public comment.

In hackerone public disclose have a three types 

1.Team/User Request a public disclose a bug
2.Team/user Agree a public disclose a bug
3.Team member Manually public disclose  a bug

Poc :

1.Login into Program(testbug) as owner account 
2.Create a new group with "Report" Permission . Add a user to that group
3.Create a new group with "Read-only" Permission . Add a user to that group
3.Login into user account Report a bug  to Program (testbug)
4."Report" Permission User closed a bug to Resolved and ask for "Public disclose" 
5."Read-only" Permission user able to "Manually public disclose" a bug .

Regards,
Techguynoob

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
