---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1214158'
original_report_id: '1214158'
title: Ratelimits do not apply to OCS DataResponse
weakness: Improper Restriction of Authentication Attempts
team_handle: nextcloud
created_at: '2021-06-01T12:10:56.746Z'
disclosed_at: '2021-08-11T09:14:01.884Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Ratelimits do not apply to OCS DataResponse

## Metadata

- HackerOne Report ID: 1214158
- Weakness: Improper Restriction of Authentication Attempts
- Program: nextcloud
- Disclosed At: 2021-08-11T09:14:01.884Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Using `$response->throttle()` on a DataResponse doesn't work as it is being transformed by BaseResponse into a OCS response. This response does not propagate any throttled setting.

## Impact

Ratelimits on OCS DataResponse not functional.

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
