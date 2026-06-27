---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '915110'
original_report_id: '915110'
title: No Email Checking at Invitation Confirmation Link leads to Account Takeover
  without User Interaction at CrowdSignal
weakness: Improper Access Control - Generic
team_handle: automattic
created_at: '2020-07-04T01:36:04.584Z'
disclosed_at: '2020-11-18T14:23:12.728Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 53
tags:
- hackerone
- improper-access-control-generic
---

# No Email Checking at Invitation Confirmation Link leads to Account Takeover without User Interaction at CrowdSignal

## Metadata

- HackerOne Report ID: 915110
- Weakness: Improper Access Control - Generic
- Program: automattic
- Disclosed At: 2020-11-18T14:23:12.728Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team,
When you have a team account, you can invite users to your team from https://app.crowdsignal.com/users/list-users.php
If you invite a user, you will see this :
{F893386}
As you can see, there is confirmation link and we can see it from our dashboard.
And if you invite existing email in website, you can see the confirmation link again. And in this link, there is no e-mail check, when you click to confirmation link, you will log-in to victim's account without any error, credentials.

## Steps To Reproduce:

  1. Go to https://app.crowdsignal.com/users/list-users.php with your team account
  1. Invite an existing email (write victim's email)
  1. And click to confirmation link with your account
  1. You will log-in to victim's account directly

## PoC video :
{F893388}

## Impact

Account Takeover without user interaction

Thanks,
Bugra

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
