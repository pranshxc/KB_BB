---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '175766'
original_report_id: '175766'
title: Remote client memory corruption in ssl_add_clienthello_tlsext()
weakness: Code Injection
team_handle: ibb
created_at: '2016-10-14T14:15:56.506Z'
disclosed_at: '2016-12-30T13:16:26.253Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: OpenSSL (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- code-injection
---

# Remote client memory corruption in ssl_add_clienthello_tlsext()

## Metadata

- HackerOne Report ID: 175766
- Weakness: Code Injection
- Program: ibb
- Disclosed At: 2016-12-30T13:16:26.253Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

https://guidovranken.wordpress.com/2016/10/13/openssl-1-1-0-remote-client-memory-corruption-in-ssl_add_clienthello_tlsext/

OpenSSL is not treating this as a security vulnerability because 1) session tickets need to be enabled 2) request certificate status from server 3) an unrealistically large ALPN list set.

Reporting this for reputation points.

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
