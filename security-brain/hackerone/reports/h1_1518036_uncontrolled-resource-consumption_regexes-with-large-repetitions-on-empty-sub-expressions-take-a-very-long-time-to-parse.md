---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1518036'
original_report_id: '1518036'
title: Regexes with large repetitions on empty sub-expressions take a very long time
  to parse
weakness: Uncontrolled Resource Consumption
team_handle: ibb
created_at: '2022-03-21T20:57:04.106Z'
disclosed_at: '2022-03-22T22:24:15.254Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: https://github.com/rust-lang/rust
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Regexes with large repetitions on empty sub-expressions take a very long time to parse

## Metadata

- HackerOne Report ID: 1518036
- Weakness: Uncontrolled Resource Consumption
- Program: ibb
- Disclosed At: 2022-03-22T22:24:15.254Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Rust's regex crate guarantees a linear time complexity with regex length for compilation of untrusted regexes. However, existing mitigations for known malicious regexes are based on memory usage and, as such, do not mitigate repetitions of empty sub-expressions. For example, the following payload triggers such an issue:

```re
(?:){4294967295}
```

This will cause the regex compiler to attempt to create 4294967295 instances of an empty sub-expression, which will ultimately allocate zero bytes and therefore bypass existing memory-based mitigations. This can be further weaponised to create an exponential time complexity with regex length by using repetitions of repetitions, e.g.:

```re
(?:){64}{64}{64}{64}{64}{64}
```

This payload would cause the regex compiler to attempt to create 64^6 instances of an empty sub-expression.

## Impact

An attacker can induce a CPU time-based denial of service with effectively infinite CPU time, which would cause the service to become entirely unavailable.

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
