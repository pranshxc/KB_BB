---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '172403'
original_report_id: '172403'
title: Python 2.7 32-bit JSON encoding heap corruption
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-09-27T13:20:03.357Z'
disclosed_at: '2019-10-13T13:01:19.623Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
asset_identifier: Python (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# Python 2.7 32-bit JSON encoding heap corruption

## Metadata

- HackerOne Report ID: 172403
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-10-13T13:01:19.623Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.python.org/issue28284
https://hg.python.org/cpython/rev/9375c8834448

Among other things this vulnerability will be triggered when JSON-encoding a dict with a very large key:
```
python -c 'import json; json.dumps({chr(0x22)*0x2AAAAAAB:0})'
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
