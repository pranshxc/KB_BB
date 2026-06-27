---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1724016'
original_report_id: '1724016'
title: Download permissions can be changed by resharer
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2022-10-06T06:49:36.714Z'
disclosed_at: '2023-02-24T07:33:41.050Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 45
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Download permissions can be changed by resharer

## Metadata

- HackerOne Report ID: 1724016
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2023-02-24T07:33:41.050Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The new feature in NC 25 to limit downloads also for internal shares is meant to force users to use secure view. So documents are watermarked and what not.

Assume a company wide share. People can share files from it to others but they can't be downloaded. For simplicity

* user1 shares a folder with reshare permissions but without download permissions to user2. Assume this is a share with ID 10
* user2 shares that folder with user3, this is a share with ID 11

This all works as expected

Now user2 simply does a PUT

```
curl -u user2:pass 'https://SERVER/ocs/v2.php/apps/files_sharing/api/v1/shares/11' -X PUT -H "OCS-APIREQUEST: true" -H 'Content-Type: application/json' --data-raw '{"permissions":"17","attributes":"[{\"scope\":\"permissions\",\"key\":\"download\",\"enabled\":true}]"}'
```

And there you go. No more pesky secure view. Just easy downloads for user3.

## Impact

Secure view for internal shares is useless if also reshare permissions are given.

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
