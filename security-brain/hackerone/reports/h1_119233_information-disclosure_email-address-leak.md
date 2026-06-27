---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '119233'
original_report_id: '119233'
title: Email Address Leak
weakness: Information Disclosure
team_handle: security
created_at: '2016-03-15T05:47:19.790Z'
disclosed_at: '2016-03-31T04:07:40.417Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Email Address Leak

## Metadata

- HackerOne Report ID: 119233
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2016-03-31T04:07:40.417Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hello,

I have found out that when a team invites a team member via username, the email address of the invited user is being disclosed after he accepted it. 

This can be abused since we all know that the email address is not publicly visible through hackerone profile. One team can abuse its function by inviting a user to join the team with a permission of read-only on the team in exchange of exposing the invited users email without his knowing of it.

In the https://hackerone.com/[program-handle]/groups you can create a group that has a read only privilege. F78875

To reproduce

Just go to https://hackerone.com/[program-handle]/team_members

Invite a user via their username with and select the group with a read-only permission.

After the user has accepted it since he dont know that it is a read-only permission. the email address of the user will be disclosed. F78874

Thanks!
Mikko

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
