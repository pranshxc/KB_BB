---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '945990'
original_report_id: '945990'
title: Safe Redirect Bypass
weakness: Security Through Obscurity
team_handle: x
created_at: '2020-07-28T20:49:16.256Z'
disclosed_at: '2020-09-10T16:57:59.560Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 94
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- security-through-obscurity
---

# Safe Redirect Bypass

## Metadata

- HackerOne Report ID: 945990
- Weakness: Security Through Obscurity
- Program: x
- Disclosed At: 2020-09-10T16:57:59.560Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

**Summary:**
The url below bypasses the safe redirect and redirects directly to the malicious website.
`http://evil.org/%00`

The reason for this may be the fix in the report #921286.

**Steps:**
Tweet the url below:
`http://evil.org/%00`

Thanks!
@cyanpiny

## Impact

The attacker can direct the victim directly, bypassing the safe redirect to the website.

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
