---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '860197'
original_report_id: '860197'
title: A staff without export customers permissions can still export customers CSV
  file
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2020-04-27T11:13:13.243Z'
disclosed_at: '2020-09-15T04:42:29.658Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# A staff without export customers permissions can still export customers CSV file

## Metadata

- HackerOne Report ID: 860197
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2020-09-15T04:42:29.658Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Steps To Reproduce:

1. Login as staff without export customers permissions but with customers permissions.
2. Go to customers pages, you can still export customers CSV file.

{F805311}
{F805312}
{F805313}

## Impact

A staff without export customers permissions can still export customers CSV file.

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
