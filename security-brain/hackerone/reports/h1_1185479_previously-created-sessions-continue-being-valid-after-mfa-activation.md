---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1185479'
original_report_id: '1185479'
title: Previously created sessions continue being valid after MFA activation
team_handle: cs_money
created_at: '2021-05-06T04:27:52.997Z'
disclosed_at: '2021-05-18T16:04:45.514Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 8
asset_identifier: cs.money
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Previously created sessions continue being valid after MFA activation

## Metadata

- HackerOne Report ID: 1185479
- Weakness: 
- Program: cs_money
- Disclosed At: 2021-05-18T16:04:45.514Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
Hi, team.
This is the same issue of #667739. Please take a look.

I found one issue related to your 2FA system on https://cs.money/security/

## Steps To Reproduce:

1. access the same account on https://cs.money/ in two devices
1. on device 'A' go to https://cs.money/security/ > complete all steps to activate the 2FA system
1. Now the 2FA is activated for this account
1. back to device 'B' reload the page
1. The session still active

## Impact

In this scenario when 2FA is activated the other sessions of the account are not invalidated.
2FA is required to login. I believe the expected and recommended behavior here is to terminate the other sessions> request a new login> request the 2FA code> so then give the account access again

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
