---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1675014'
original_report_id: '1675014'
title: Profile of disabled user stays accessible
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2022-08-19T19:36:52.526Z'
disclosed_at: '2022-11-26T06:53:30.529Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Profile of disabled user stays accessible

## Metadata

- HackerOne Report ID: 1675014
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2022-11-26T06:53:30.529Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Userprofiles of disabled users keep staying accessible. on DOMAIN/u/USERID
This is quite undesirable as this user has no way to clear or modify this data in case they do not want it exposed anymore.
I'd assume profiles of disabled users would not be visible to ensure they can always be in control of their own data.

## Impact

exposure of user info that they can't control anymore.

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
