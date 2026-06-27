---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1305766'
original_report_id: '1305766'
title: There is no rate limit for SME REGISTRATION PORTAL
weakness: Improper Authentication - Generic
team_handle: mtn_group
created_at: '2021-08-15T08:24:59.479Z'
disclosed_at: '2022-09-19T05:41:27.495Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: mtngbissau.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# There is no rate limit for SME REGISTRATION PORTAL

## Metadata

- HackerOne Report ID: 1305766
- Weakness: Improper Authentication - Generic
- Program: mtn_group
- Disclosed At: 2022-09-19T05:41:27.495Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
The speed limit for the https://mtngbissau.com/registo/ endpoint has not been implemented.
## Steps To Reproduce:
1. Go to the https://mtngbissau.com/registo/
2.  fill out the Registration form
3. Send request to Intruder.
4. Set your payloads and start attack.
5. There is no rate-limit.

## Impact

Attacker can register false n-number of request which lead to DDos attack.

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
