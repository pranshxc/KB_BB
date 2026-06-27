---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1434276'
original_report_id: '1434276'
title: Information disclosure through django debug mode
weakness: Information Exposure Through Debug Information
team_handle: mtn_group
created_at: '2021-12-22T20:15:59.573Z'
disclosed_at: '2022-09-05T22:56:33.593Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: mtn.co.sz
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-exposure-through-debug-information
---

# Information disclosure through django debug mode

## Metadata

- HackerOne Report ID: 1434276
- Weakness: Information Exposure Through Debug Information
- Program: mtn_group
- Disclosed At: 2022-09-05T22:56:33.593Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Your domain https://szezvzorilla.mtn.co.sz was disclosing information throught django debug mode enable.

## Steps To Reproduce:
Visit https://szezvzorilla.mtn.co.sz/NON_EXISTING_PATH/
You will the information of debugging


## Supporting Material/References:
{F1555934}
  * [attachment / reference]

## Impact

Information disclosure

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
