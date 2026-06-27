---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2234736'
original_report_id: '2234736'
title: Session Doesn't expire after 2fa and also other session can change passsword
weakness: Improper Access Control - Generic
team_handle: sidefx
created_at: '2023-11-01T06:29:49.307Z'
disclosed_at: '2024-03-02T17:43:09.917Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 67
asset_identifier: '*.sidefx.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Session Doesn't expire after 2fa and also other session can change passsword

## Metadata

- HackerOne Report ID: 2234736
- Weakness: Improper Access Control - Generic
- Program: sidefx
- Disclosed At: 2024-03-02T17:43:09.917Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team,
I found one issue related to your 2FA system on https://sidefx.com
## Steps To Reproduce:
Login to the Same account in 2 different browser
Now on 1st browser go to https://sidefx.com/profile and complete the all steps of 2fa and Enable it | 2FA activated
Now go to another session or 2nd browser and reload the page.
The account doesn't logout session is still alive.
and now change the password on 2nd browser (which doesn't have 2fa enabled) 
BOOM!

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
