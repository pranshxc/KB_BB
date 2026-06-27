---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1154003'
original_report_id: '1154003'
title: Ratelimiting can be bypassed using IPv6 subnets
weakness: Improper Restriction of Authentication Attempts
team_handle: nextcloud
created_at: '2021-04-07T01:26:34.268Z'
disclosed_at: '2021-07-01T18:02:41.444Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Ratelimiting can be bypassed using IPv6 subnets

## Metadata

- HackerOne Report ID: 1154003
- Weakness: Improper Restriction of Authentication Attempts
- Program: nextcloud
- Disclosed At: 2021-07-01T18:02:41.444Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Nextcloud hardcodes IPv6 subnets to /128.
End users get at least a /64 subnet (more than the whole IPv4 address space!), most providers assign even larger subnets like /48.
The subnet is used to block bruteforce attempts [3] and rate limiting [4]. An attacker can easily generate random addresses from the assigned /48 subnet to bypass these protections.
Nextcloud should block at least /64 subnets or even better dynamically change the size of the subnet depending on the amount of suspect requests coming from a larger subnet, maybe up to /32.

[1] https://github.com/nextcloud/server/blob/f12fab23db3529c34f620789f345f5e5e841c06a/lib/private/Security/Normalizer/IpAddress.php#L107-L110
[2] https://www.ripe.net/publications/docs/ripe-552#assignment
[3] https://github.com/nextcloud/server/blob/f12fab23db3529c34f620789f345f5e5e841c06a/lib/private/Security/Bruteforce/Throttler.php#L132
[4] https://github.com/nextcloud/server/blob/f12fab23db3529c34f620789f345f5e5e841c06a/lib/private/Security/RateLimiting/Limiter.php#L84

## Impact

bruteforce protection and rate limiting are basically useless for IPv6 targets.

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
