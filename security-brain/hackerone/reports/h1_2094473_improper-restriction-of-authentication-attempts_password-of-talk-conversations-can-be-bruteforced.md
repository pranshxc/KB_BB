---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2094473'
original_report_id: '2094473'
title: Password of talk conversations can be bruteforced
weakness: Improper Restriction of Authentication Attempts
team_handle: nextcloud
created_at: '2023-08-03T07:54:04.356Z'
disclosed_at: '2023-11-12T08:15:39.910Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 27
asset_identifier: nextcloud/spreed
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Password of talk conversations can be bruteforced

## Metadata

- HackerOne Report ID: 2094473
- Weakness: Improper Restriction of Authentication Attempts
- Program: nextcloud
- Disclosed At: 2023-11-12T08:15:39.910Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Steps To Reproduce:

  1. Instead of sending a POST to the authentication endpoint, the password can be added as a parameter on the GET request of the frontpage.
  2. A failure will not log a bruteforce attempt, but a successful password will no longer bring up the login page

## Supporting Material/References:
Found while looking into https://support.nextcloud.com/#ticket/zoom/47814

## Impact

Brute force protection of public talk conversation passwords can be bypassed.

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
