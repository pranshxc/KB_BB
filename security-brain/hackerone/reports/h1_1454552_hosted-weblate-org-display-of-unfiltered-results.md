---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1454552'
original_report_id: '1454552'
title: hosted.weblate.org display of unfiltered results
team_handle: weblate
created_at: '2022-01-19T20:49:17.706Z'
disclosed_at: '2022-01-21T20:47:58.490Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: hosted.weblate.org
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# hosted.weblate.org display of unfiltered results

## Metadata

- HackerOne Report ID: 1454552
- Weakness: 
- Program: weblate
- Disclosed At: 2022-01-21T20:47:58.490Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

able to request all changes of everything not just sandbox when inserting this %'s in author username on this page.  https://hosted.weblate.org/changes/?project=sandbox&lang=en&user=%25%27s&start_date=&end_date=

## Impact

no filter on request feels like elevated permissions. lets you do the search even though it throws error.

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
