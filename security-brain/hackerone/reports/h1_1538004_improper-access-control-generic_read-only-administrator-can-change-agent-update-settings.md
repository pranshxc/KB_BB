---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1538004'
original_report_id: '1538004'
title: Read-only administrator can change agent update settings
weakness: Improper Access Control - Generic
team_handle: acronis
created_at: '2022-04-11T20:34:30.992Z'
disclosed_at: '2022-08-10T09:38:40.191Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: beta-cloud.acronis.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Read-only administrator can change agent update settings

## Metadata

- HackerOne Report ID: 1538004
- Weakness: Improper Access Control - Generic
- Program: acronis
- Disclosed At: 2022-08-10T09:38:40.191Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Gents,
+ While testing `eu2-cloud.acronis.com` I found that read-only administrators are able to update agents just by editing the HTML!

### Steps to reproduce:
1. Please login at https://eu2-cloud.acronis.com/mc/
2. From Users, invite a new user with Read-only administrator role.
3. From Read-only administrator account navigate to "Agents Update" https://eu2-cloud.acronis.com/mc/app;group_id=*******/settings/agents-update
4. Inspect element -> search for `readonly`.
5. Change the value from `readonly="true"` to `readonly="false"`.
6. Edit, update and save.
7. Now open the "Agents Update" page from the company administrator account, you will be able to see the changes!

### Proof of concept:
+ {F1688988}

## Impact

Read-only administrator is able to edit and "Agents Update"

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
