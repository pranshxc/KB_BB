---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '549831'
original_report_id: '549831'
title: External Storage - WebDAV - New user has access to storage from deleted user
  (same user-ID)
weakness: Insecure Storage of Sensitive Information
team_handle: nextcloud
created_at: '2019-04-28T18:30:08.036Z'
disclosed_at: '2021-02-14T16:24:44.764Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# External Storage - WebDAV - New user has access to storage from deleted user (same user-ID)

## Metadata

- HackerOne Report ID: 549831
- Weakness: Insecure Storage of Sensitive Information
- Program: nextcloud
- Disclosed At: 2021-02-14T16:24:44.764Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

* Delete existing user account "user3"
* Create new user account "user3"

Also reported on https://github.com/nextcloud/server/issues/15258

## Impact

Newly created user with same user-id of a deleted user has access to the configured external webdav storage from the deleted user.

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
