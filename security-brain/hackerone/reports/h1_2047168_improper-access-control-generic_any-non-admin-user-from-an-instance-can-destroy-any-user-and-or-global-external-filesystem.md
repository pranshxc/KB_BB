---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2047168'
original_report_id: '2047168'
title: Any (non-admin) user from an instance can destroy any (user and/or global)
  external filesystem
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2023-07-02T15:13:30.256Z'
disclosed_at: '2023-08-10T09:50:03.738Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Any (non-admin) user from an instance can destroy any (user and/or global) external filesystem

## Metadata

- HackerOne Report ID: 2047168
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2023-08-10T09:50:03.738Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

There is no verification of the ownership and/or its type when deleting a user-manager external storage. 
Meaning anyone on a Nextcloud instance can destroy any (user, global) external filesystem.
The attacker does not need to have access to the external storage.
The options 'Allow users to mount external storage does not need to be enabled.

When executing the DELETE request on /apps/files_external/userstorages/<storage_id> [1], the app will:
- only check that the mount exists in database, without any condition based on the type of the storage and/or its owner [2]
- remove all data from database related to the storage based on its id. [3]

[1] https://github.com/nextcloud/server/blob/master/apps/files_external/lib/Controller/UserStoragesController.php#L234
[2]  https://github.com/nextcloud/server/blob/master/apps/files_external/lib/Service/DBConfigService.php#L67
[3] https://github.com/nextcloud/server/blob/master/apps/files_external/lib/Service/DBConfigService.php#L274


## Steps To Reproduce:

- From an admin session, create a new external storage.
- From a non-admin session, send a DELETE request to `/apps/files_external/userstorages/<storage_id>`, replace `storage_id` by the correct id (integer) of the storage.
- From an admin session, the created external storage is not listed anymore.

## Impact

Filesystem can be unmounted by anyone, I have no clue how this was not reported earlier.

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
