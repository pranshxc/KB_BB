---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1081406'
original_report_id: '1081406'
title: Open redirect in ck.php and lg.php
weakness: Open Redirect
team_handle: revive_adserver
created_at: '2021-01-19T12:51:23.297Z'
disclosed_at: '2021-01-20T11:04:49.610Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
asset_identifier: https://github.com/revive-adserver/revive-adserver
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open redirect in ck.php and lg.php

## Metadata

- HackerOne Report ID: 1081406
- Weakness: Open Redirect
- Program: revive_adserver
- Disclosed At: 2021-01-20T11:04:49.610Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

An opportunity for open redirects has been available by design since the
early versions of Revive Adserver's predecessors in the impression and
click tracking scripts to allow third party ad servers to track such
metrics when delivering ads. Historically the display advertising
industry has considered that to be a feature, not a real vulnerability.

The lg.php and ck.php delivery scripts are subject to open redirect via
either dest, oadest and/or ct0 parameters.

## Impact

Users seeing a trustworthy domain could be redirected to a malicious URL without realising.

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
