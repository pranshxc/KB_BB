---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '423496'
original_report_id: '423496'
title: H1514 Bypass Wholesale account signup restrictions
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2018-10-13T20:31:59.294Z'
disclosed_at: '2019-06-07T09:46:08.885Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 45
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# H1514 Bypass Wholesale account signup restrictions

## Metadata

- HackerOne Report ID: 423496
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2019-06-07T09:46:08.885Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

By default, account registration is disabled on Shopify Wholesale, requiring customers to be manually invited:

> Wholesale account signup is disabled. Customers need to be manually invited from the Customers page.

This can be bypassed due to improper access controls in the invitation functionality, allowing an attacker without an invite access to the full Wholesale store.

## Steps To Reproduce:

  1. Configure Wholesale for two separate Shopify stores at https://wholesale.shopifyapps.com. Let Store A be the target store (jackstore-7 in my case) for which the attacker aims to gain access. Let Store B be the attacker's own store (jackstore-6 in my case).
  1. As Store B, create a product/price list and add at least one customer to Wholesale.
  1. Under the Wholesale Customers page (https://jackstore-6.myshopify.com/admin/apps/wholesale/admin/shops/7662/accounts), select a customer and generate an invite link. This link will be of the form `https://jackstore-6.wholesale.shopifyapps.com/accounts/invitation/accept?invitation_token=KqhsT8sWFbbEdxpHxHt7`.
  1. Replace the store domain in the link with Store A.
  1. Observe that the invitation token is still treated as valid for Store A, and an account can be registered.
  1. Upon registration, the user will have access to the entire Wholesale store:

{F360240}

## Impact

This allows an attacker to bypass account signup restrictions for Wholesale stores and join any store without being invited. This may include private products or documentation which a store wants to keep restricted only to invited users.

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
