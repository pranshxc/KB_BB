---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1200810'
original_report_id: '1200810'
title: Admin audit is not properly logging unsetting of expiration date
team_handle: nextcloud
created_at: '2021-05-18T12:31:10.126Z'
disclosed_at: '2021-07-15T19:13:34.255Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Admin audit is not properly logging unsetting of expiration date

## Metadata

- HackerOne Report ID: 1200810
- Weakness: 
- Program: nextcloud
- Disclosed At: 2021-07-15T19:13:34.255Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In relation to https://hackerone.com/reports/1177353

1. Enable the audit log
2. Share a file
3. Set and expiration date

So far all looks good in the log

4. Unset the the expiration date.
5. See a pretty useless log line

## Impact

The audit log is used to get a full trail of the actions which is now incompletely. With possible important information.
It seems to be also listed on https://portal.nextcloud.com/article/using-the-audit-log-44.html

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
