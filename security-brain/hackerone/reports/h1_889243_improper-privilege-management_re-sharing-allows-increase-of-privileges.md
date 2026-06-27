---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '889243'
original_report_id: '889243'
title: Re-Sharing allows increase of privileges
weakness: Improper Privilege Management
team_handle: nextcloud
created_at: '2020-06-02T11:23:03.692Z'
disclosed_at: '2020-09-28T09:19:36.857Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 91
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-privilege-management
---

# Re-Sharing allows increase of privileges

## Metadata

- HackerOne Report ID: 889243
- Weakness: Improper Privilege Management
- Program: nextcloud
- Disclosed At: 2020-09-28T09:19:36.857Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

- User A shares a file/folder to user B with re-sharing permission, but readonly
- User B shares this file/folder to User C (Needs the shareapi_default_permissions set to 1 (all checkmarks off in admin panel))
- User B can add write permissions for the share to User C (User C may also be anonymous using a link)
- User C gets write access and can edit existing files

## Impact

User can get write permission on read-only shared files/folders.

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
