---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '123572'
original_report_id: '123572'
title: Unauthorized Team members viewing
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2016-03-16T10:48:38.664Z'
disclosed_at: '2016-07-02T00:11:29.400Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 11
tags:
- hackerone
- improper-authentication-generic
---

# Unauthorized Team members viewing

## Metadata

- HackerOne Report ID: 123572
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2016-07-02T00:11:29.400Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

In a Team, a user that does not have an admin permission at https://hackerone.com/[team_name]/team_members can view the list of users in the Program by visiting 
https://hackerone.com/[team_name]/team_members.json
Although it is only a user with an admin permission that can view the Team members and modify their permission, but other members that do not have such right can view ALL the members in the Team.

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
