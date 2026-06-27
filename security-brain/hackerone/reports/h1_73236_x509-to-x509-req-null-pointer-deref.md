---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '73236'
original_report_id: '73236'
title: X509_to_X509_REQ NULL pointer deref
team_handle: ibb
created_at: '2015-03-15T00:00:00.000Z'
disclosed_at: '2015-03-15T00:00:00.000Z'
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

# X509_to_X509_REQ NULL pointer deref

## Metadata

- HackerOne Report ID: 73236
- Weakness: 
- Program: ibb
- Disclosed At: 2015-03-15T00:00:00.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

X509_to_X509_REQ NULL pointer deref (CVE-2015-0288)
===================================================

Severity: Low

The function X509_to_X509_REQ will crash with a NULL pointer dereference if the certificate key is invalid. This function is rarely used in practice.

This issue affects all current OpenSSL versions: 1.0.2, 1.0.1, 1.0.0 and 0.9.8.

OpenSSL 1.0.2 users should upgrade to 1.0.2a
OpenSSL 1.0.1 users should upgrade to 1.0.1m.
OpenSSL 1.0.0 users should upgrade to 1.0.0r.
OpenSSL 0.9.8 users should upgrade to 0.9.8zf.

This issue was discovered by Brian Carpenter and a fix developed by Stephen Henson of the OpenSSL development team.

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
