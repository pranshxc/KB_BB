---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6794'
original_report_id: '6794'
title: The server supports only older protocols for HTTPS connections
weakness: Cryptographic Issues - Generic
team_handle: c2fo
created_at: '2014-04-10T08:24:59.115Z'
disclosed_at: '2014-05-15T20:58:02.685Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cryptographic-issues-generic
---

# The server supports only older protocols for HTTPS connections

## Metadata

- HackerOne Report ID: 6794
- Weakness: Cryptographic Issues - Generic
- Program: c2fo
- Disclosed At: 2014-05-15T20:58:02.685Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The webserver at `c2fo.com`, `198.58.120.159` only supports SSL 3.0 and TLS 1.0 for secure HTTP connections (see: test-results.png). While TLS 1.0 is more secure than SSL 3.0, subsequent versions of TLS, TLS 1.1 and TLS 1.2, are significantly more secure and fix many vulnerabilities present in SSL 3.0 and TLS 1.0.

I recommend enabling support for TLS 1.1 and TLS 1.2.  Because not all browsers and operating systems support these new versions, to ensure availability, SSL 3.0 and/or TLS 1.0 should not be disabled (for now).

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
