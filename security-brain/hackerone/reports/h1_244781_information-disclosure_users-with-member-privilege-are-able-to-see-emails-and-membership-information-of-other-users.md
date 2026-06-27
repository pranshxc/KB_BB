---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '244781'
original_report_id: '244781'
title: Users with member privilege are able to see emails and membership information
  of other users
weakness: Information Disclosure
team_handle: wakatime
created_at: '2017-06-30T16:08:40.549Z'
disclosed_at: '2017-09-25T22:14:41.272Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- information-disclosure
---

# Users with member privilege are able to see emails and membership information of other users

## Metadata

- HackerOne Report ID: 244781
- Weakness: Information Disclosure
- Program: wakatime
- Disclosed At: 2017-09-25T22:14:41.272Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:** According to the rules of Leaderboard Teams only Owners and admins have access to other team members' personal information like email address, roles etc.

Users whose role set as "Member" can't see other users' details.

But through API it is possible for a user with member role to reveal personal information of all team members.

**Vulnerable URL: `https://wakatime.com/api/v1/users/current/leaderboards/<team_id>/members`**

**Steps to reproduce:**

1. Join a Leaderboard team as a member.
2. Copy the team id.
3. Visit the vulnerable url.

You'll find that emails of all members being disclosed.

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
