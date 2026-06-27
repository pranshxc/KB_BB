---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '413759'
original_report_id: '413759'
title: Race condition at create new Location
weakness: Business Logic Errors
team_handle: shopify
created_at: '2018-09-25T03:20:18.368Z'
disclosed_at: '2018-10-05T04:49:12.421Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Race condition at create new Location

## Metadata

- HackerOne Report ID: 413759
- Weakness: Business Logic Errors
- Program: shopify
- Disclosed At: 2018-10-05T04:49:12.421Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

User can bypas restriction and create more ctore location, than maximum depends store plan. Intercept request and send it multiple at once. See screensots
F350687 - requests
F350688 - results
I created 12 store location when 4 possible

## Impact

Bypass the limitations of the billing plan

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
