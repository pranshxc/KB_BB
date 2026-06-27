---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '72331'
original_report_id: '72331'
title: XSS at Bulk editing ProductVariants
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-06-24T07:36:00.263Z'
disclosed_at: '2015-06-25T04:12:57.741Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS at Bulk editing ProductVariants

## Metadata

- HackerOne Report ID: 72331
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-06-25T04:12:57.741Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Steps to Reproduce:

1.Create a Product with Title and Description as ` "><img src=x onerror=prompt(133)>`
2. Now goto https://blahblah.myshopify.com/admin/products/inventory
3. Select the Product created at Step 1 and Click on Edit variants

and XSS will be triggered

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
