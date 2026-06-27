---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1486820'
original_report_id: '1486820'
title: Invitation Email is resent as a Reminder after invalidating pending email invites
weakness: Improper Access Control - Generic
team_handle: mattermost
created_at: '2022-02-21T03:36:02.510Z'
disclosed_at: '2022-04-19T11:37:01.653Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: '*.mattermost.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# Invitation Email is resent as a Reminder after invalidating pending email invites

## Metadata

- HackerOne Report ID: 1486820
- Weakness: Improper Access Control - Generic
- Program: mattermost
- Disclosed At: 2022-04-19T11:37:01.653Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team , I have found an issue through which unwanted users can be added to victim's workspace inside *.cloud.mattermost.com  .

So I have created an workspace with my email id , let's say email1 and invited email2 to my workspace . Email2 is not having an account at mattermost , So email2 will be a fresh account. But I noticed that there is no option present to cancel the invite . This will lead to the issue . Let's see this in detail -

Real life case - Suppose a victim has invited someone to the workspace by putting email id but later on victim decided to withdraw the email id but there is no such option present due to which attacker can now join the workspace which leads to info disclosure . Also victim can mistype the email while inviting but victim now can't withdraw that email invite.

Mitigation - There should be an option present to cancel the invite sent to any email.

Steps to reproduce -
1) create account at mattermost and then create a workspace for yourself inside -  *.cloud.mattermost.com
2) now invite email2 (email2 is not having account at mattermost) by invite option
3) now you will notice that there is no way present to cancel the invite
4) now email2 can easily join the workspace

## Impact

Unwanted users can join the workspace leading to information disclosure.

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
