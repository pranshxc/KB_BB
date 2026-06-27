---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '423546'
original_report_id: '423546'
title: H1514 Wholesale customer without checkout permission can complete purchases
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2018-10-13T22:40:37.218Z'
disclosed_at: '2019-04-10T20:24:25.101Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# H1514 Wholesale customer without checkout permission can complete purchases

## Metadata

- HackerOne Report ID: 423546
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2019-04-10T20:24:25.101Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

By default, Shopify Wholesale customers are prevented from immediately checking out:

{F360280}

Instead, a store admin must approve each order before the customer can pay.

This restriction can be bypassed, allowing a customer to check out orders without prior approval. This also bypasses any maximum checkout amount that a store can set.

## Steps To Reproduce:

  1. As a Wholesale owner, ensure that a customer is disallowed from immediately checking out at https://your-store.myshopify.com/admin/apps/wholesale/admin/shops/x/accounts.
  1. As the customer, visit the Wholesale shop and fill your cart with products.
  1. Observe that the UI forces the user to submit a purchase order:

    {F360285}

  1. To bypass this restriction, intercept the request to `PUT /purchase_orders/submit` to submit the purchase order and change the url to `/purchase_orders/update_checkout`.
  1. Observe that executing the request will allow the customer to proceed through the checkout flow and place the order:

{F360296}

## Impact

This allows a customer to bypass manual approval restrictions for a Wholesale store and immediately check out.

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
