---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1210450'
original_report_id: '1210450'
title: 1-byte heap buffer overflow in DNS resolver
weakness: Off-by-one Error
team_handle: ibb
created_at: '2021-05-27T10:32:41.592Z'
disclosed_at: '2021-08-27T00:07:05.588Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
asset_identifier: Nginx (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- off-by-one-error
---

# 1-byte heap buffer overflow in DNS resolver

## Metadata

- HackerOne Report ID: 1210450
- Weakness: Off-by-one Error
- Program: ibb
- Disclosed At: 2021-08-27T00:07:05.588Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Official announcement: http://mailman.nginx.org/pipermail/nginx-announce/2021/000300.html

A security issue in nginx resolver was identified, which might allow an
attacker to cause 1-byte memory overwrite by using a specially crafted
DNS response, resulting in worker process crash or, potentially, in
arbitrary code execution (CVE-2021-23017).

The issue only affects nginx if the "resolver" directive is used in
the configuration file.  Further, the attack is only possible if an
attacker is able to forge UDP packets from the DNS server.

The issue affects nginx 0.6.18 - 1.20.0.
The issue is fixed in nginx 1.21.0, 1.20.1.

Patch for the issue can be found here:

http://nginx.org/download/patch.2021.resolver.txt

Thanks to Luis Merino, Markus Vervier, Eric Sesterhenn, X41 D-Sec GmbH.

## Impact

Crash or, potentially,  arbitrary code execution.

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
