---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1091380'
original_report_id: '1091380'
title: '[h1-2102] Partner''s team member with no permission can retrieve services
  financial data'
weakness: Improper Authorization
team_handle: shopify
created_at: '2021-01-31T19:37:32.092Z'
disclosed_at: '2021-04-08T19:40:09.370Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: partners.shopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authorization
---

# [h1-2102] Partner's team member with no permission can retrieve services financial data

## Metadata

- HackerOne Report ID: 1091380
- Weakness: Improper Authorization
- Program: shopify
- Disclosed At: 2021-04-08T19:40:09.370Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Details
Unfortunately, I wasn't able to properly validate the following report as I could not get access the my partner's services option (event is ending in a few hours) and that access is manually given (https://help.shopify.com/en/partners/selling-services). However, given the observed behaviour, I assume there's a high probability of this being a missing permission check.

Within a partner's organization, financial datas are gated by the **View financials** permission. However, I observed that a staff with no permission is able to retrieve **Services** financial.

### Steps to reproduce
#### Partner's organization owner
1. Create a Partner's account on https://partners.shopify.com
1. Invite a team member with no permissions (go to **Teams > Invite staff member**, select no permission and complete the invite)

#### Partner's staff member with no permission
1. Accept the invite and log-in to the partner's dashboard
1. In the upper right corner, click on the notification bell image and intercept the GraphQL request being made to https://partners.shopify.com/:id/api/graphql
1. Update the payload to the following:
```
{
   "query":"{ serviceMetrics { totalEarnings { amount } } }"
}
```

As a result, you will be returned the financial data:
```
{
   "data":{
      "serviceMetrics":{
         "totalEarnings":{
            "amount":"0.0"
         }
      }
   }
}
```
Assuming that this property should be gated by the **View financials** permission,  I should have received an access denied there instead of an amount (being `0.00` in my case as there's no data).

## Impact

Staff with no permissions, specifically the **View financials** is able to access **Services** financial data

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
