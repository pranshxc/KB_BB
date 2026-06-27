---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2094785'
original_report_id: '2094785'
title: Cargo not respecting umask when extracting crate archives
team_handle: ibb
created_at: '2023-08-03T15:30:18.444Z'
disclosed_at: '2023-08-15T18:15:38.372Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: https://github.com/rust-lang/rust
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Cargo not respecting umask when extracting crate archives

## Metadata

- HackerOne Report ID: 2094785
- Weakness: 
- Program: ibb
- Disclosed At: 2023-08-15T18:15:38.372Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Cargo did not properly protect files in the cargo registry. When an archive contained files which were marked as globally writeable, they would be unpacked as-is and retain their global writeability. This is CWE-278 (not available in HackerOne).

This was discovered as part of a (personal) routine file permissions check:

```sh
find / ! -type l -perm -002 -exec ls -alhd {} \;
```

## Impact

A local attacker may inject arbitrary code into the cached files present in the cargo registry. This, in turn, allows for a local attacker to act as the targeted user (when the user compiles the modified code) or to poison prebuilt binaries built by that user and thus have arbitrary code execution against downstream users (supply chain attack).

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
