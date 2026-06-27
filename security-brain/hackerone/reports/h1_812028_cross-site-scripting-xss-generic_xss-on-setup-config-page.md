---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '812028'
original_report_id: '812028'
title: xss on setup config page
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2020-03-06T08:56:57.544Z'
disclosed_at: '2021-02-14T16:21:26.534Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# xss on setup config page

## Metadata

- HackerOne Report ID: 812028
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2021-02-14T16:21:26.534Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Nextcloud version: 18.0.1
In setup config page，setting `mysql Username` with payload`<script>alert(1)</script>`, and set others. F739076
then submit . F739077
this gif will show poc: F739069

## Impact

This is because the code does not filter dangerous characters. so dangerous characters need to be escaped.

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
