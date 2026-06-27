---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '216151'
original_report_id: '216151'
title: Use-after-free in _asyncio_Future_remove_done_callback
weakness: Use After Free
team_handle: ibb
created_at: '2017-03-26T04:18:18.622Z'
disclosed_at: '2019-11-12T09:00:49.248Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: Python (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- use-after-free
---

# Use-after-free in _asyncio_Future_remove_done_callback

## Metadata

- HackerOne Report ID: 216151
- Weakness: Use After Free
- Program: ibb
- Disclosed At: 2019-11-12T09:00:49.248Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

http://bugs.python.org/issue28963

Callbacks could be removed from a list while it was iterated, leading to an out of bounds access. A fix for this bug is now in the CPython repository.

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
