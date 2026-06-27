---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1200815'
original_report_id: '1200815'
title: Federated share accepting/declining is not logged in audit log
weakness: Business Logic Errors
team_handle: nextcloud
created_at: '2021-05-18T12:34:55.440Z'
disclosed_at: '2022-09-03T06:12:07.191Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Federated share accepting/declining is not logged in audit log

## Metadata

- HackerOne Report ID: 1200815
- Weakness: Business Logic Errors
- Program: nextcloud
- Disclosed At: 2022-09-03T06:12:07.191Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In relation to https://hackerone.com/reports/1177353

1. Enable the audit log
2. Share a file to a federated user
3. So far all looks good in the log
4. the recipient checks either accepts or declines the share
5.  There is no line regarding this in the logs.

## Impact

The audit log is used to get a full trail of the actions which is now incompletely. With possible important information.
It seems to be also listed on https://portal.nextcloud.com/article/using-the-audit-log-44.html
From my point of view a declined share is unshared again.

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
