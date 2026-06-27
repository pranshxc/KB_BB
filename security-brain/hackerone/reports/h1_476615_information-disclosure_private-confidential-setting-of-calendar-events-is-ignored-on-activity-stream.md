---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '476615'
original_report_id: '476615'
title: Private/confidential setting of calendar events is ignored on activity stream
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2019-01-08T16:10:21.614Z'
disclosed_at: '2019-06-27T08:45:58.518Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Private/confidential setting of calendar events is ignored on activity stream

## Metadata

- HackerOne Report ID: 476615
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2019-06-27T08:45:58.518Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

https://github.com/nextcloud/server/pull/13331

Events that are private should not generate events for other users
Events that are confidential should not leak the name to other users

## Impact

The details are leaked to other users

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
