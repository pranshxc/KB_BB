---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1596918'
original_report_id: '1596918'
title: Brute force protections don't work
weakness: Privacy Violation
team_handle: nextcloud
created_at: '2022-06-10T11:34:48.223Z'
disclosed_at: '2022-09-03T06:25:26.022Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# Brute force protections don't work

## Metadata

- HackerOne Report ID: 1596918
- Weakness: Privacy Violation
- Program: nextcloud
- Disclosed At: 2022-09-03T06:25:26.022Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Most of the brute force protections don't actually throttle() the response and so they are not logging negative attempts

Search for functions with the `@BruteForceProtection` annotation and check that they call `throttle()` on the response at least conditionally.

## Impact

Brute force protection is not throttling any requests:
https://github.com/nextcloud/server/blob/b70c6a128fe5d0053b7971881696eafce4cb7c26/lib/private/AppFramework/Middleware/Security/BruteForceMiddleware.php#L78-L82

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
