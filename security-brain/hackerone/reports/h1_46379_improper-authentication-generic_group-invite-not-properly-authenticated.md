---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '46379'
original_report_id: '46379'
title: Group Invite not properly authenticated
weakness: Improper Authentication - Generic
team_handle: nearby
created_at: '2015-02-03T22:59:20.192Z'
disclosed_at: '2015-02-12T01:41:38.031Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# Group Invite not properly authenticated

## Metadata

- HackerOne Report ID: 46379
- Weakness: Improper Authentication - Generic
- Program: nearby
- Disclosed At: 2015-02-12T01:41:38.031Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

There is no check whether the inviting user is allowed to invite a user into a group and through manipulation a user may sent themself and invite to any group.

Example:
Group A created by User 1 with Owner invitation only with ID x
User 2 sends malicious himself invite with ID x and receives invite to Group A


API Call that needs to be fixed:
https://www.wnmlive.com/api/groups/invites

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
