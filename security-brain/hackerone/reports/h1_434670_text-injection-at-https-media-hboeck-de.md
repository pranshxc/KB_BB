---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '434670'
original_report_id: '434670'
title: Text injection at https://media.hboeck.de
team_handle: hannob
created_at: '2018-11-06T02:59:55.828Z'
disclosed_at: '2019-03-22T17:16:27.256Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: invalid.hboeck.de
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Text injection at https://media.hboeck.de

## Metadata

- HackerOne Report ID: 434670
- Weakness: 
- Program: hannob
- Disclosed At: 2019-03-22T17:16:27.256Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Text injection possible at https://media.hboeck.de


if we craft url like this:

https://media.hboeck.de/?c=http://www.example.com

We can see the output on web app.

## Impact

Defacement of website by following crafted link

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
