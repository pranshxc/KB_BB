---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '67132'
original_report_id: '67132'
title: XSS at Bulk editing products
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-06-10T08:15:22.843Z'
disclosed_at: '2015-06-17T15:04:22.964Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS at Bulk editing products

## Metadata

- HackerOne Report ID: 67132
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-06-17T15:04:22.964Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

after following above the steps in #67125 goto  Bulk editing products:

for me the url was:
 https://img-src-x-onerror-prompt1-24.myshopify.com/admin/bulk?resource_name=Product&edit=variants.sku%2Cvariants.price%2Cvariants.compare_at_price&message=&return_to=%2Fadmin%2Fproducts&ids=1151578433

it is also vulnerable to xss
(Change the requierd fields in above url according to your shop)

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
