---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '696266'
original_report_id: '696266'
title: '"Bounties paid in the last 90 days" discloses the undisclosed bounty amount
  in program statistics'
weakness: Information Disclosure
team_handle: security
created_at: '2019-09-17T07:06:51.386Z'
disclosed_at: '2020-02-21T19:13:37.034Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 82
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# "Bounties paid in the last 90 days" discloses the undisclosed bounty amount in program statistics

## Metadata

- HackerOne Report ID: 696266
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2020-02-21T19:13:37.034Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

## Summary:

I have found a bypass on this disclosed report: [Know undisclosed Bounty Amount when Bounty Statistics are enabled.](https://hackerone.com/reports/148050)

## Description:

When a program does not disclose how much bounty is paid to particular report, but if bounty statics is enabled then undisclosed Bounty Amount can be enumerated using the __"Bounties paid in the last 90 days".__

"Bounties paid in the last 90 days" is the total amount paid in the last 90 days, so by doing a basic mathematical equation, we can be able to determine the undisclosed bounty amount, below is the formula to get the undisclosed bounty amount.

__Formula__

`old` = `Old Bounties paid in the last 90 days` >> Total 90 days bounty paid
`new` = `New Bounties paid in the last 90 days` >> Everytime the 90 days bounty changes

`undisclosed amount` = `old - new`

## Mitigation:

Use the same fix you have applied in this report #148050

## Impact

Disclosing the undisclosed bounty amount for program which is not disclosing bounties in their settings.

Let me know if anything else is needed.

Regards
Japz

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
