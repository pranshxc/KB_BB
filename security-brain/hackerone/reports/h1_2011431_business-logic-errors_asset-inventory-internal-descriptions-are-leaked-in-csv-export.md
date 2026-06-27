---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2011431'
original_report_id: '2011431'
title: Asset Inventory Internal Descriptions are leaked in CSV export
weakness: Business Logic Errors
team_handle: security
created_at: '2023-06-02T20:51:17.449Z'
disclosed_at: '2023-07-12T06:50:57.834Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 63
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Asset Inventory Internal Descriptions are leaked in CSV export

## Metadata

- HackerOne Report ID: 2011431
- Weakness: Business Logic Errors
- Program: security
- Disclosed At: 2023-07-12T06:50:57.834Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

Hey team,

I was looking at the new Asset Inventory functionality and it looks like as a program I can set an Internal asset description

███

This internal description is meant to be private and can't be seen on the scope page: (https://hackerone.com/█████). 

However, if you export the CSV then it leaks this internal description information

**Description:**

### Steps To Reproduce

1. Navigate to https://hackerone.com/██████████
2. Click the Export to CSV button
3. In the CSV you should see `Internal Description For ES` next to the █████████████ scope item

## Impact

Programs are assuming this asset information is indeed internal and may be storing sensitive information such as internal paths/credentials/etc in this description.

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
