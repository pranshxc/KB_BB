---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '449818'
original_report_id: '449818'
title: Is the 504 Gateway Time-out error ok?
weakness: Uncontrolled Resource Consumption
team_handle: infogram
created_at: '2018-11-26T13:42:33.286Z'
disclosed_at: '2018-11-28T11:47:30.761Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Is the 504 Gateway Time-out error ok?

## Metadata

- HackerOne Report ID: 449818
- Weakness: Uncontrolled Resource Consumption
- Program: infogram
- Disclosed At: 2018-11-28T11:47:30.761Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Link: https://infogram.com/api/merge/auth/google/?redirect_to=123&token=gulHMyL6-1H0Am4zXa4H7j0DWomPdnKPhZOk&redirect_to=123 it gives 504 after a long time! Is it normal? It can be used for DOS! I use two redirect_to= if I use just one redirect_to= it gives the response fastly! https://infogram.com/api/merge/auth/google/?redirect_to=123&token=gulHMyL6-1H0Am4zXa4H7j0DWomPdnKPhZOk

## Impact

DOS?

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
