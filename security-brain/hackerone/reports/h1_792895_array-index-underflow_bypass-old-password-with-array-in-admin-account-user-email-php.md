---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '792895'
original_report_id: '792895'
title: bypass old password with array in /admin/account-user-email.php
weakness: Array Index Underflow
team_handle: revive_adserver
created_at: '2020-02-11T03:46:24.481Z'
disclosed_at: '2020-03-12T12:54:49.138Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
asset_identifier: https://github.com/revive-adserver/revive-adserver
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- array-index-underflow
---

# bypass old password with array in /admin/account-user-email.php

## Metadata

- HackerOne Report ID: 792895
- Weakness: Array Index Underflow
- Program: revive_adserver
- Disclosed At: 2020-03-12T12:54:49.138Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

### Short Description
- attacker maybe change email or password without enter old password with array param.
- version:revive-adserver-5.0.4
- os :window

### POC
{F712486}

## Impact

attacker maybe change email or password without enter old password

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
