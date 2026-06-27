---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1198203'
original_report_id: '1198203'
title: Bootstrap library is vulnerable
weakness: Inclusion of Functionality from Untrusted Control Sphere
team_handle: sifchain
created_at: '2021-05-15T07:30:49.585Z'
disclosed_at: '2021-09-06T16:40:10.106Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- inclusion-of-functionality-from-untrusted-control-sphere
---

# Bootstrap library is vulnerable

## Metadata

- HackerOne Report ID: 1198203
- Weakness: Inclusion of Functionality from Untrusted Control Sphere
- Program: sifchain
- Disclosed At: 2021-09-06T16:40:10.106Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Summary:
The identified library bootstrap, version 4.0.0 is vulnerable
 Steps To Reproduce:
Please upgrade to the latest version of bootstrap.

 
## Supporting Material/References:

https://github.com/twbs/bootstrap/issues/28236
https://github.com/twbs/bootstrap/issues/20184

## Impact

XSS was possible in the tooltip or popover data-template, data-content and data-title attributes.

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
