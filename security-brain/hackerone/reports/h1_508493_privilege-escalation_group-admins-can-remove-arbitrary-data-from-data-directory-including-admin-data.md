---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '508493'
original_report_id: '508493'
title: Group admins can remove arbitrary data from "data" directory (including admin
  data)
weakness: Privilege Escalation
team_handle: nextcloud
created_at: '2019-03-12T15:48:46.756Z'
disclosed_at: '2019-08-12T15:15:22.336Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Group admins can remove arbitrary data from "data" directory (including admin data)

## Metadata

- HackerOne Report ID: 508493
- Weakness: Privilege Escalation
- Program: nextcloud
- Disclosed At: 2019-08-12T15:15:22.336Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Steps to reproduce:

1. Create a new user and make him an admin of an arbitrary group
2. Log in as this new user
3. Create a new user "files_external", "appdata_{random-data}", ..
4. Delete this user

Result: The data/files_external / data/appdata{..} folder is removed.

Solution: Prevent creation of users if data/{new-user-uid} is either
a file or a folder. In addition, prevent deletion of users where the
user data directory (data/{user}) contains other files and folders
than "files" (where the user data is stored).

## Impact

Group admin can remove arbitrary data from "data" directory

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
