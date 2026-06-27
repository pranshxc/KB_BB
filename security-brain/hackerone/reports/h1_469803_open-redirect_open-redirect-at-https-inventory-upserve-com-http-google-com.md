---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '469803'
original_report_id: '469803'
title: Open redirect at https://inventory.upserve.com/http://google.com/
weakness: Open Redirect
team_handle: upserve
created_at: '2018-12-18T22:35:48.534Z'
disclosed_at: '2019-06-07T11:24:28.766Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 162
asset_identifier: inventory.upserve.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open redirect at https://inventory.upserve.com/http://google.com/

## Metadata

- HackerOne Report ID: 469803
- Weakness: Open Redirect
- Program: upserve
- Disclosed At: 2019-06-07T11:24:28.766Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The following URL is vulnerable to an open redirect (it will redirect to stanko.sh):

https://inventory.upserve.com/http://stanko.sh/

## Impact

Users could get redirected to malicious domain.

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
