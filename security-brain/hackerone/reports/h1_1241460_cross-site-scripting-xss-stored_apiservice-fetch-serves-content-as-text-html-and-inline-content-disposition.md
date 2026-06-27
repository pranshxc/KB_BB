---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1241460'
original_report_id: '1241460'
title: ApiService#fetch serves content as text/html and inline Content-Disposition
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nextcloud
created_at: '2021-06-22T18:28:28.878Z'
disclosed_at: '2021-08-11T09:22:56.033Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: nextcloud/text
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# ApiService#fetch serves content as text/html and inline Content-Disposition

## Metadata

- HackerOne Report ID: 1241460
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nextcloud
- Disclosed At: 2021-08-11T09:22:56.033Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

https://github.com/nextcloud/text/blame/0bc7c3300607d57ee512dbf61497daec23961a12/lib/Service/ApiService.php#L109-L120

## Impact

XSS

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
