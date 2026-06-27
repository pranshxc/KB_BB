---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '667739'
original_report_id: '667739'
title: Previously created sessions continue being valid after MFA activation
weakness: Improper Access Control - Generic
team_handle: grammarly
created_at: '2019-08-05T15:49:02.756Z'
disclosed_at: '2019-08-19T15:25:48.612Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 155
asset_identifier: account.grammarly.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Previously created sessions continue being valid after MFA activation

## Metadata

- HackerOne Report ID: 667739
- Weakness: Improper Access Control - Generic
- Program: grammarly
- Disclosed At: 2019-08-19T15:25:48.612Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

I found one issue related to your 2FA system on https://account.grammarly.com/security

POC

1 access the same account on https://account.grammarly.com in two devices
2 on device 'A' go to https://account.grammarly.com/security > complete all steps to activate the 2FA system

Now the 2FA is activated for this account

3 back to device 'B' reload the page

The session still active

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
