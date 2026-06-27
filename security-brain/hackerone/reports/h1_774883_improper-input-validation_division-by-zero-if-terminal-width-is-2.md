---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '774883'
original_report_id: '774883'
title: Division by zero if terminal width is 2
weakness: Improper Input Validation
team_handle: curl
created_at: '2020-01-14T17:44:31.429Z'
disclosed_at: '2021-02-08T07:53:40.195Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-input-validation
---

# Division by zero if terminal width is 2

## Metadata

- HackerOne Report ID: 774883
- Weakness: Improper Input Validation
- Program: curl
- Disclosed At: 2021-02-08T07:53:40.195Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
In fly() there will be a division by zero if progress bar width is 2.

That can happen if terminal width is 2.

## Steps To Reproduce:
This script crash:
stty rows 10 cols 2 ; curl --progress-bar somefile > temp

## Impact

I believe that if it's possible to set terminal width for a service, then that service will not be able to curl.

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
