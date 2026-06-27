---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '915114'
original_report_id: '915114'
title: IDOR when editing users leads to Account Takeover without User Interaction
  at CrowdSignal
weakness: Insecure Direct Object Reference (IDOR)
team_handle: automattic
created_at: '2020-07-04T01:52:20.526Z'
disclosed_at: '2020-11-18T14:23:32.970Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 182
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR when editing users leads to Account Takeover without User Interaction at CrowdSignal

## Metadata

- HackerOne Report ID: 915114
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: automattic
- Disclosed At: 2020-11-18T14:23:32.970Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team,
If you click `Edit` button on any user of your team at https://app.crowdsignal.com/users/list-users.php, you will send a GET request to `https://app.crowdsignal.com/users/invite-user.php?id=(userid)&popup=1`
In this endpoint, `id` parameter is vulnerable for IDOR. When you change the user ID, you will see victim's email in response like that :
{F893392}
And if you click `Update Permissions` button, you will log-in to victim's account directly.
Also, user IDs are sequential. And they have a simple range with `00010006` to `19920500+`

## Steps To Reproduce:

  1. Log-in to your team account at CrowdSignal
  1. Go to https://app.crowdsignal.com/users/invite-user.php?id=19920465&popup=1
  1. You will see my email, and if you click `Update Permissions`, you will takeover my account.
  1. You can change the user ID to random number with `00010006` - `19920500` range.

## Impact

IDOR leads to account takeover without user interaction

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
