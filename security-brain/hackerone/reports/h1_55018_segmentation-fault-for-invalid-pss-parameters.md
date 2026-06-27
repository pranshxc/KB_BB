---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '55018'
original_report_id: '55018'
title: Segmentation fault for invalid PSS parameters
team_handle: ibb
created_at: '2015-01-31T00:00:00.000Z'
disclosed_at: '2015-03-19T00:00:00.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: OpenSSL (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# Segmentation fault for invalid PSS parameters

## Metadata

- HackerOne Report ID: 55018
- Weakness: 
- Program: ibb
- Disclosed At: 2015-03-19T00:00:00.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The signature verification routines will crash with a NULL pointer dereference if presented with an ASN.1 signature using the RSA PSS algorithm and invalid parameters. Since these routines are used to verify certificate signature algorithms this can be used to crash any certificate verification operation and exploited in a DoS attack. Any application which performs certificate verification is vulnerable including OpenSSL clients and servers which enable client authentication.

This issue affects OpenSSL version: 1.0.2

OpenSSL 1.0.2 users should upgrade to 1.0.2a

This issue was was reported to OpenSSL on 31st January 2015 by Brian Carpenter and a fix developed by Stephen Henson of the OpenSSL development team.

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
