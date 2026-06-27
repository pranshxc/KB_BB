---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '165570'
original_report_id: '165570'
title: Race Condition in account survey
weakness: Violation of Secure Design Principles
team_handle: slack
created_at: '2016-09-03T20:44:49.995Z'
disclosed_at: '2017-11-12T11:25:59.583Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
- violation-of-secure-design-principles
---

# Race Condition in account survey

## Metadata

- HackerOne Report ID: 165570
- Weakness: Violation of Secure Design Principles
- Program: slack
- Disclosed At: 2017-11-12T11:25:59.583Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There exists a race condition in the beginning survey, allowing a user to get $100 in credit multiple times. In my example, I made 2 asynchronous requests, and was credited with $200.

POC:

1. Create a new slack team.
2. Set your password, and find the account creation survey.
3. Complete the survey, and intercept the request using a proxy such as BurpSuite.
4. Repeat the request asynchronously, such as in the command line by executing `(command) & (command)`.
5. The survey will be credited to your account multiple times. See the attached screenshot.

Please let me know if you need any more information.

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
