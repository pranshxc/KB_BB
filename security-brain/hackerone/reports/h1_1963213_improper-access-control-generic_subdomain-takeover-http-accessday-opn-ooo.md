---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1963213'
original_report_id: '1963213'
title: Subdomain takeover http://accessday.opn.ooo/
weakness: Improper Access Control - Generic
team_handle: omise
created_at: '2023-04-27T08:51:52.805Z'
disclosed_at: '2023-06-11T07:04:41.266Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 69
asset_identifier: www.opn.ooo
asset_type: URL
max_severity: high
tags:
- hackerone
- improper-access-control-generic
---

# Subdomain takeover http://accessday.opn.ooo/

## Metadata

- HackerOne Report ID: 1963213
- Weakness: Improper Access Control - Generic
- Program: omise
- Disclosed At: 2023-06-11T07:04:41.266Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I found unused accessday.opn.ooo subdomain was delegated to wix.com and not claimed.

##Steps To Reproduce:
- Visit http://accessday.opn.ooo/
- This domain pointing towards to WIX cdn, anyone can claim this subdomain

##Similar report:
https://hackerone.com/reports/1256389
https://hackerone.com/reports/996956
https://hackerone.com/reports/1183296

## Impact

An attacker can claim this subdomain and abused for specific purposes

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
