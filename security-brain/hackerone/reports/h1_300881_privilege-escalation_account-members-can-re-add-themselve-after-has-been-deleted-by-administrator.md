---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '300881'
original_report_id: '300881'
title: Account members can re-add themselve after has been deleted by administrator
weakness: Privilege Escalation
team_handle: mavenlink
created_at: '2017-12-28T01:04:01.627Z'
disclosed_at: '2018-05-03T18:36:50.342Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- privilege-escalation
---

# Account members can re-add themselve after has been deleted by administrator

## Metadata

- HackerOne Report ID: 300881
- Weakness: Privilege Escalation
- Program: mavenlink
- Disclosed At: 2018-05-03T18:36:50.342Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Reproduction:
=========

- As an administrator, invite an account members e.g: user1@email.com via https://app.mavenlink.com/settings/account/members 
- An invitation link sent to user1@email.com, as user1, open email inbox and click on the link, notice the link redirects to page url:
https://app.mavenlink.com/account_invitations/[token]/acceptances/new
- Note the above link.
- As user1, Click "Accept", the user has been added as an active member.
- As administrator, remove user1 from active member list.
- As user1, go to the noted link: https://app.mavenlink.com/account_invitations/[token]/acceptances/new,
and click "Accept", the user has been added to the group again.

## Impact

Any user can add himself after has been deleted from an administrator.

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
