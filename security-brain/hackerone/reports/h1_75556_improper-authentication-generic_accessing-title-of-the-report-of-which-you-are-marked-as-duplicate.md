---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '75556'
original_report_id: '75556'
title: Accessing title of the report of which you are marked as duplicate
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2015-07-15T10:04:45.012Z'
disclosed_at: '2015-07-17T18:17:49.548Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-authentication-generic
---

# Accessing title of the report of which you are marked as duplicate

## Metadata

- HackerOne Report ID: 75556
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2015-07-17T18:17:49.548Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

You can see the title of the report of which you are marked as Duplicate

Steps to Reproduce:
1. Report a bug to a team
2. Now that team marks your bug as 'Duplicate (#Report_ID).(but does not shares the report with you)
3. When that bug is marked as Resolved then you can see the title of that bug at https://hackerone.com/settings/reputation/log

This is clearly a lack of authentication as unless the bug is not shared or it is not public you should not be allowed to see any of its content.

Thanks

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
