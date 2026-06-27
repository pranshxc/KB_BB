---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '767770'
original_report_id: '767770'
title: Private objects exposed through project import
weakness: Insecure Direct Object Reference (IDOR)
team_handle: gitlab
created_at: '2020-01-03T16:39:54.149Z'
disclosed_at: '2022-06-07T14:16:30.343Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 106
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Private objects exposed through project import

## Metadata

- HackerOne Report ID: 767770
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: gitlab
- Disclosed At: 2022-06-07T14:16:30.343Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary
This is a bypass of https://hackerone.com/reports/743953 , the current fix is blocking all "_ids" attributes. However an attacker could still set attributes like `issue_ids` by indrectly settings the field within the `attributes` field it self:
```
# project.json
    "attributes": {
        "issue_ids": [ 29279725 ],
        "description": "Set from attributes[description]"
    },
```

### Steps to reproduce

1. Import the attached tarball.
2. Check issues tab

The other parts of the report are mostly same as those I mentioned in https://hackerone.com/reports/743953 , I decide to write a new report considering the impact to gitlab.com.

## Impact

With this ability to modify relations between objects, an attacker could end up with accessing random resources of other users by traversing the incremental ID space.

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
