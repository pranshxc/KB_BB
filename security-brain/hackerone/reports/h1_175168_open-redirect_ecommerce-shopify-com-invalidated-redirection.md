---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '175168'
original_report_id: '175168'
title: '[ecommerce.shopify.com] Invalidated redirection'
weakness: Open Redirect
team_handle: shopify
created_at: '2016-10-11T16:47:52.126Z'
disclosed_at: '2016-12-04T15:57:02.684Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- open-redirect
---

# [ecommerce.shopify.com] Invalidated redirection

## Metadata

- HackerOne Report ID: 175168
- Weakness: Open Redirect
- Program: shopify
- Disclosed At: 2016-12-04T15:57:02.684Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

**Endpoint :** https://ecommerce.shopify.com/auth/shopify?shop=[victim_shop].myshopify.com&return_to=/////example.com

Suppose, victim has not linked his shop with ecommerce.shopify.com portal then an attacker can redirect him on an external website after linking or rejecting. 

**Steps to reproduce :**

1. Get logged in as admin in your shop and ecommerce.shopify.com
2. Open this link : https://ecommerce.shopify.com/auth/shopify?shop=[your-shop].myshopify.com&return_to=/////example.com
3. If you are logged in then **Link These Accounts** button and **No thanks** link will be shown.
4. Click on **Link Account** button or **No thanks** link.
5. You will be redirected on https://example.com instead of ecommerce.shopify.com
6. Done

Again, your shop should not be linked to ecommerce.shopify.com.

**Suggested Fix :** Use more stronger regular expression at this endpoint

Best regards,
Shailesh

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
