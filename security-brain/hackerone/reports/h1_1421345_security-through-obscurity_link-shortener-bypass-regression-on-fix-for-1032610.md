---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1421345'
original_report_id: '1421345'
title: 'Link-shortener bypass (regression on fix for #1032610)'
weakness: Security Through Obscurity
team_handle: x
created_at: '2021-12-09T11:51:54.192Z'
disclosed_at: '2022-12-12T17:39:00.725Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- security-through-obscurity
---

# Link-shortener bypass (regression on fix for #1032610)

## Metadata

- HackerOne Report ID: 1421345
- Weakness: Security Through Obscurity
- Program: x
- Disclosed At: 2022-12-12T17:39:00.725Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Report #1032610, entitled

> Chained open redirects and use of Ideographic Full Stop defeat Twitter's approach to blocking links

was [closed as _Resolved _ about six months ago](https://hackerone.com/reports/1032610#activity-12095285).

However, a regression on the fix for the vulnerability in question seems to have occurred, and the bug is reproducible with the exact same payload.

## Impact

Refer to [#1032610](https://hackerone.com/reports/1032610#user-content-impact).

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
