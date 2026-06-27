---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '826026'
original_report_id: '826026'
title: Use-After-Free In IPV6_2292PKTOPTIONS leading To Arbitrary Kernel R/W Primitives
weakness: Use After Free
team_handle: playstation
created_at: '2020-03-21T16:40:38.626Z'
disclosed_at: '2020-07-06T19:12:54.099Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 715
asset_identifier: PlayStation 4
asset_type: HARDWARE
max_severity: critical
tags:
- hackerone
- use-after-free
---

# Use-After-Free In IPV6_2292PKTOPTIONS leading To Arbitrary Kernel R/W Primitives

## Metadata

- HackerOne Report ID: 826026
- Weakness: Use After Free
- Program: playstation
- Disclosed At: 2020-07-06T19:12:54.099Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary

Due to missing locks in option `IPV6_2292PKTOPTIONS` of `setsockopt` , it is possible to race and free the `struct ip6_pktopts ` buffer, while it is being handled by `ip6_setpktopt`. This structure contains pointers (`ip6po_pktinfo`) that can be hijacked to obtain arbitrary kernel R/W primitives. As a consequence, it is easy to have kernel code execution. This vulnerability is reachable from WebKit sandbox and is available in the latest FW, that is 7.02.

## Attachment

Attached is a Proof-Of-Concept that achieves a Local Privilege Escalation on FreeBSD 9 and FreeBSD 12.

## Impact

- In conjunction with a WebKit exploit, a fully chained remote attack can be achieved.
- It is possible to steal/manipulate user data.
- Dump and run pirated games.

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
