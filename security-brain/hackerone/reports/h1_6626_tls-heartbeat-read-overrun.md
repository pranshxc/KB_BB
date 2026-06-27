---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6626'
original_report_id: '6626'
title: TLS heartbeat read overrun
team_handle: ibb
created_at: '2014-04-05T23:51:06.000Z'
disclosed_at: '2014-04-07T16:53:31.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: OpenSSL (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# TLS heartbeat read overrun

## Metadata

- HackerOne Report ID: 6626
- Weakness: 
- Program: ibb
- Disclosed At: 2014-04-07T16:53:31.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A missing bounds check in the handling of the TLS heartbeat extension can be used to reveal up to 64k of memory to a connected client or server.

Only 1.0.1 and 1.0.2-beta releases of OpenSSL are affected including 1.0.1f and 1.0.2-beta1.

Thanks for Neel Mehta of Google Security for discovering this bug and to Adam Langley <agl@chromium.org> and Bodo Moeller <bmoeller@acm.org> for preparing the fix.

Affected users should upgrade to OpenSSL 1.0.1g. Users unable to immediately upgrade can alternatively recompile OpenSSL with -DOPENSSL_NO_HEARTBEATS.

1.0.2 will be fixed in 1.0.2-beta2.

http://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=96db9023b881d7cd9f379b0c154650d6c108e9a3

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
