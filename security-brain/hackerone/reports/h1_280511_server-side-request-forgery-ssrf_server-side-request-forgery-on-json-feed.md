---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '280511'
original_report_id: '280511'
title: Server Side Request Forgery on JSON Feed
weakness: Server-Side Request Forgery (SSRF)
team_handle: infogram
created_at: '2017-10-19T14:22:14.085Z'
disclosed_at: '2017-12-06T10:18:15.005Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Server Side Request Forgery on JSON Feed

## Metadata

- HackerOne Report ID: 280511
- Weakness: Server-Side Request Forgery (SSRF)
- Program: infogram
- Disclosed At: 2017-12-06T10:18:15.005Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team, I would like to report SSRF issue.

#PoC:
1. Navigate to ```https://infogram.com/app/[user-project]```.
2. Click on edit logo fields and click on add JSON Data.
3. Enter ```[url][openport]``` response is ```Download failed```
4. Enter ```[url][closedport]``` response is ```Invalid data source```

#Fix:
Don't give permission to port related connections or use single error message.

Regards,
Mr.R3boot.

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
