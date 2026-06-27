---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1102660'
original_report_id: '1102660'
title: staffOrderNotificationSubscriptionDelete Could Be Used By Staff Member With
  Settings Permission
weakness: Improper Authorization
team_handle: shopify
created_at: '2021-02-13T10:35:03.720Z'
disclosed_at: '2022-02-09T20:59:25.561Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authorization
---

# staffOrderNotificationSubscriptionDelete Could Be Used By Staff Member With Settings Permission

## Metadata

- HackerOne Report ID: 1102660
- Weakness: Improper Authorization
- Program: shopify
- Disclosed At: 2022-02-09T20:59:25.561Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The staff order notification should be under the control of staff members with `Order` permission but I found that the staff member with just `Settings` permission can also delete the order notifications using the GID

Steps to reproduce
- Login as a staff member with `Settings` permission
- Make this GraphQL call to `https://yoursubdomain.myshopify.com/admin/internal/web/graphql/core?operation=SwitcherNoStores`

```
{"query": "mutation{staffOrderNotificationSubscriptionDelete(staffOrderNotificationSubscriptionId:\"gid://shopify/StaffOrderNotificationSubscription/82867191864\"){userErrors{message}}} "}
```

- Note: you can find the `82867191864` id from `/admin/settings/notifications` as an admin account, in the `Staff order notifications` section, after adding a order notification and the id is in the URL

- The response you see should be `{"staffOrderNotificationSubscriptionDelete":{"userErrors":[]}}`, and this means you have deleted the subscription already

## Impact

The staff order notification should be under the control of staff members with `Order` permission but I found that the staff member with just `Settings` permission can also delete the order notifications using the GID

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
