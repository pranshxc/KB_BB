---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1392511'
original_report_id: '1392511'
title: HackerOne Staging uses Production data for testing
weakness: Privacy Violation
team_handle: security
created_at: '2021-11-05T17:15:10.674Z'
disclosed_at: '2021-11-05T20:52:15.780Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 58
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# HackerOne Staging uses Production data for testing

## Metadata

- HackerOne Report ID: 1392511
- Weakness: Privacy Violation
- Program: security
- Disclosed At: 2021-11-05T20:52:15.780Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Today I received an email related to smart rewards from HackerOne. This included staging environment details, such as:

```
sender: no-reply+staging@hackerone.com
Privacy / Terms links pointing to domain: https://www.enorekcah.com/...
``` 

This basically tells us that HackerOne is using hacker data (real users) in their lower environment (STAGING). Usually this should be avoided and production data should not be copied into lower environments -> using live data for testing.

See attachment which holds a copy of received email: ████

## Impact

Privacy issues related to customer/hacker data in HackerOne.

Cheers!
@tk0

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
