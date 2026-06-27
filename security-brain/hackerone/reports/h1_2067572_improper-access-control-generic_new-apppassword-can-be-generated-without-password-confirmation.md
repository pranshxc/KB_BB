---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2067572'
original_report_id: '2067572'
title: New AppPassword can be generated without password confirmation
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2023-07-12T19:28:02.996Z'
disclosed_at: '2023-08-10T07:20:18.566Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# New AppPassword can be generated without password confirmation

## Metadata

- HackerOne Report ID: 2067572
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2023-08-10T07:20:18.566Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is protection on https://github.com/nextcloud/server/blob/master/apps/settings/lib/Controller/AuthSettingsController.php#L122 that you must have recently entered your password to be able to generate a new AppPassword. However if an attacker would obtain access to your system (say you forgot to lock it when taking a quick bathroom break).

They can abuse a route to just obtain this. ```https://SERVER/ocs/v2.php/core/getapppassword```
Probably without you ever noticing.

## Impact

The password confirmation to generate an app password is effectively useless as it is trivial to bypass.

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
