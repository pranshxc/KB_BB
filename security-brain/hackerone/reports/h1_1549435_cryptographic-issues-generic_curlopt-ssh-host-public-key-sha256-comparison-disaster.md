---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1549435'
original_report_id: '1549435'
title: CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256 comparison disaster
weakness: Cryptographic Issues - Generic
team_handle: curl
created_at: '2022-04-24T16:02:36.316Z'
disclosed_at: '2022-04-25T10:58:34.118Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cryptographic-issues-generic
---

# CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256 comparison disaster

## Metadata

- HackerOne Report ID: 1549435
- Weakness: Cryptographic Issues - Generic
- Program: curl
- Disclosed At: 2022-04-25T10:58:34.118Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
`CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256` base64 encoded host fingerprint is compared case-insensitive by accident. This means that it is technically possible (however still difficult) to create forged ssh host key that matches in this comparison.

The bug appears to have been introduced when adding `CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256`  support, and then copying the case insensitive comparison of the string for` CURLOPT_SSH_HOST_PUBLIC_KEY_MD5` (where it is appropriate since the MD5 fingerprint is a hex string).

This bug as added by commit https://github.com/curl/curl/commit/d1e7d9197b7fe417fb4d62aad5ea8f15a06d906c

## Impact

Host identify spoofing

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
