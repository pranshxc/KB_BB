---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '62861'
original_report_id: '62861'
title: Bulk Discount App in myshopify.com exposes http://bulkdiscounts.shopifyapps.com
  vulnerable to XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-05-18T14:34:45.258Z'
disclosed_at: '2015-07-23T16:45:06.222Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Bulk Discount App in myshopify.com exposes http://bulkdiscounts.shopifyapps.com vulnerable to XSS

## Metadata

- HackerOne Report ID: 62861
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-07-23T16:45:06.222Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Installing the Bulk Discount App in *.myshopify.com (which requires  a paid basic plan) makes the bulkdiscounts.shopifyapps.com vulnerable to XSS due to non sanitized input in products and collections.

POC:

1. Enter a product name or a collection such as "><img src=x onerror=prompt(document.domain)> and save it.
2. Install the Shopify BulkDiscounts App
3. Go to Apps -> Shopify BulkDiscounts
4. Click on "Create One now" or "New Discount Set"

Due to improper sanitization XSS occurs in the shopifyapps.com domain !!

Thanks

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
