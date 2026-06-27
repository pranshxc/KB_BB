---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1690510'
original_report_id: '1690510'
title: the complete server installation path is visible in cloud/user endpoint
weakness: Improper Removal of Sensitive Information Before Storage or Transfer
team_handle: nextcloud
created_at: '2022-09-03T17:44:27.658Z'
disclosed_at: '2023-03-30T09:14:16.107Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-removal-of-sensitive-information-before-storage-or-transfer
---

# the complete server installation path is visible in cloud/user endpoint

## Metadata

- HackerOne Report ID: 1690510
- Weakness: Improper Removal of Sensitive Information Before Storage or Transfer
- Program: nextcloud
- Disclosed At: 2023-03-30T09:14:16.107Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

https://github.com/nextcloud/server/issues/33883


When doing a GET request on `/ocs/v1.php/cloud/user?format=json` the server returns user data, including one containing the full local server path:

```
            "storageLocation": "/home/bohwaz/www/tmp/nextcloud/data/bohwaz",
```

This is not a big security issue (as you need to be logged-in to get that response), but this is data that an attacker shouldn't be able to know easily.

This happens on a brand new install after using the web installer.

## Impact

Sensitive internal info

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
