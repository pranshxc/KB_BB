---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1987062'
original_report_id: '1987062'
title: Password reset endpoint is not brute force protected
weakness: Improper Restriction of Authentication Attempts
team_handle: nextcloud
created_at: '2023-05-13T19:17:02.587Z'
disclosed_at: '2023-07-21T06:14:00.426Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 42
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Password reset endpoint is not brute force protected

## Metadata

- HackerOne Report ID: 1987062
- Weakness: Improper Restriction of Authentication Attempts
- Program: nextcloud
- Disclosed At: 2023-07-21T06:14:00.426Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Oversight of https://github.com/nextcloud/security-advisories/security/advisories/GHSA-v243-x6jc-42mp (https://hackerone.com/reports/1841665, but I can't judge the content there as it is not yet public).

In any case. The whole lostpassword flow is now annotated with bruteforce protection. Except the endpoint that actually matters. https://github.com/nextcloud/server/blob/master/core/Controller/LostController.php#L226-L229

An attacker can still happily try to brute force the token. Without getting throttled.

## Impact

The lostpassword flow is without actual bruteforce protection.

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
