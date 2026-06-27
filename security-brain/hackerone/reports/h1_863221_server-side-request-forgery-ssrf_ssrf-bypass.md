---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '863221'
original_report_id: '863221'
title: SSRF bypass
weakness: Server-Side Request Forgery (SSRF)
team_handle: concretecms
created_at: '2020-04-30T13:38:41.988Z'
disclosed_at: '2021-10-04T15:53:07.833Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: https://github.com/concrete5/concrete5
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF bypass

## Metadata

- HackerOne Report ID: 863221
- Weakness: Server-Side Request Forgery (SSRF)
- Program: concretecms
- Disclosed At: 2021-10-04T15:53:07.833Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

This simply describes a bypass for report at https://hackerone.com/reports/243865, using a decimal notation encoded IP address (0177.0.0.1
) currently bypasses the limitations in place for localhost.
crayons (re-submitting report including "magic" string)
Concrete5 version used is 8.5.2

## Impact

Interacting with local services, impact may vary depending on services actually exposed.

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
