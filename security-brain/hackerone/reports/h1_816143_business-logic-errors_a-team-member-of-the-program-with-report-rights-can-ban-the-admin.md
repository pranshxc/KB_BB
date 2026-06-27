---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '816143'
original_report_id: '816143'
title: A team member of the program with Report rights can ban the Admin
weakness: Business Logic Errors
team_handle: security
created_at: '2020-03-10T17:49:55.074Z'
disclosed_at: '2020-05-15T17:22:21.766Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# A team member of the program with Report rights can ban the Admin

## Metadata

- HackerOne Report ID: 816143
- Weakness: Business Logic Errors
- Program: security
- Disclosed At: 2020-05-15T17:22:21.766Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Our team has conducted a number of studies (tests) in the field of permission `Report`. We noticed that a team member of the program with such permission can ban a member with `Admin` rights

## Steps To Reproduce:
1) Admin submit new report in program
2) A team member with Report rights can use the 'Ban reporters ' panel via their report

my group - `one_permission` have permission `Report`

{F743466}
█████

3) After `ban` , admin can't create new report in program (it's not logical)

{F743464}

## Impact

Ban the Admin in program

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
