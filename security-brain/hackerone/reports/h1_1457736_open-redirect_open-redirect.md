---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1457736'
original_report_id: '1457736'
title: Open Redirect
weakness: Open Redirect
team_handle: jetblue
created_at: '2022-01-21T22:38:46.870Z'
disclosed_at: '2023-01-29T18:03:59.462Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: '*.jetblue.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open Redirect

## Metadata

- HackerOne Report ID: 1457736
- Weakness: Open Redirect
- Program: jetblue
- Disclosed At: 2023-01-29T18:03:59.462Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The following URL is vulnerable to an open redirect (it will redirect to example.com):
https://█████?redirecturl=https://example.com
I hope you know the impact of open redirect and more info refer

## Impact

User can be redirect to malicious site.

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
