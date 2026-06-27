---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '257376'
original_report_id: '257376'
title: Missing Restriction On String Size
weakness: Memory Corruption - Generic
team_handle: weblate
created_at: '2017-08-07T14:45:19.791Z'
disclosed_at: '2017-09-16T13:39:10.730Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: hosted.weblate.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- memory-corruption-generic
---

# Missing Restriction On String Size

## Metadata

- HackerOne Report ID: 257376
- Weakness: Memory Corruption - Generic
- Program: weblate
- Disclosed At: 2017-09-16T13:39:10.730Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Similar to [#223454](https://hackerone.com/reports/223454), there is no string size restriction on `project` parameter which is sent directly to the server.  

**URL:** https://hosted.weblate.org/hosting/
**PoC:** `poc1.png` and `poc2.png`

Shall you need any more info notify me,

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
