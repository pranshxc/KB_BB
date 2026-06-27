---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2429894'
original_report_id: '2429894'
title: 'Libuv: Improper Domain Lookup that potentially leads to SSRF attacks'
weakness: Server-Side Request Forgery (SSRF)
team_handle: ibb
created_at: '2024-03-21T18:47:15.142Z'
disclosed_at: '2024-03-29T22:54:22.421Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 67
asset_identifier: https://github.com/libuv/libuv
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Libuv: Improper Domain Lookup that potentially leads to SSRF attacks

## Metadata

- HackerOne Report ID: 2429894
- Weakness: Server-Side Request Forgery (SSRF)
- Program: ibb
- Disclosed At: 2024-03-29T22:54:22.421Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I recently encountered a challenge in a CTF competition that led me to discover a vulnerability within Node.js, present in all versions after v10. Upon further investigation and code debugging, it became apparent that the vulnerability originated from its direct dependency, `libuv`.

I submitted a report to the Node.js team via HackerOne, and they subsequently connected me with the libuv team. This collaboration resulted in the identification and resolution of the vulnerability, now recorded as CVE-2024-24806.

## Impact

This vulnerability could allow an attacker to craft payloads that results in **SSRF** attacks and **Internal API Access**. Full explanation of vulnerability, PoC and sample scenarios are provided within the original report:
https://github.com/libuv/libuv/security/advisories/GHSA-f74f-cvh7-c6q6

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
