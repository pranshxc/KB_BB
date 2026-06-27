---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1200989'
original_report_id: '1200989'
title: No admin audit entry for enabling/disabling 2FA
team_handle: nextcloud
created_at: '2021-05-18T13:57:33.348Z'
disclosed_at: '2021-06-16T08:40:24.869Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# No admin audit entry for enabling/disabling 2FA

## Metadata

- HackerOne Report ID: 1200989
- Weakness: 
- Program: nextcloud
- Disclosed At: 2021-06-16T08:40:24.869Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Related to https://hackerone.com/reports/1177353
When a user enables or disables 2FA there is no entry in the audit log.

## Impact

Especially for disabling it should probably be logged there. But account security related things should be in there.

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
