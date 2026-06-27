---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1825472'
original_report_id: '1825472'
title: 'speedtest.8x8.com: Enabled Directory Listing'
weakness: Information Exposure Through Directory Listing
team_handle: 8x8
created_at: '2023-01-07T07:58:59.255Z'
disclosed_at: '2023-03-28T01:27:31.054Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: '*.8x8.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-exposure-through-directory-listing
---

# speedtest.8x8.com: Enabled Directory Listing

## Metadata

- HackerOne Report ID: 1825472
- Weakness: Information Exposure Through Directory Listing
- Program: 8x8
- Disclosed At: 2023-03-28T01:27:31.054Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Directory listing can be found at 2 of `8x8.com` subdomains:-
- https://speedtest.8x8.com
- https://speedtest-uswest1.8x8.com

## Impact

An attacker can see the whole directory structure of a particular directory, which can reveal sensitive information.

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
