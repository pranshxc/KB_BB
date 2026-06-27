---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '975827'
original_report_id: '975827'
title: Permanent DoS with one click.
weakness: Uncontrolled Resource Consumption
team_handle: automattic
created_at: '2020-09-06T19:07:58.256Z'
disclosed_at: '2020-11-19T07:45:47.650Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 126
asset_identifier: '*.tumblr.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Permanent DoS with one click.

## Metadata

- HackerOne Report ID: 975827
- Weakness: Uncontrolled Resource Consumption
- Program: automattic
- Disclosed At: 2020-11-19T07:45:47.650Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello Team, messages of a user who deletes their account leave DoS effects on another user.


## Platform(s) Affected:
[website/mobile app/service]

## Steps To Reproduce & PoC:
Before you start testing, create two accounts.
cyanpiny+attacker@gmail.com
cyanpiny+victim@gmail.com
Confirm e-mails to send messages.

  1. Log into the attacker's account.
  2. Message the victim from the attacker's account.
  3. Delete the attacker's account.
  4. Log into the victim's account.
  5. Check the victim's message box.
  6. The victim cannot use the account again.

Video:
{F978195}

## Impact

The victim cannot use the account again.

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
