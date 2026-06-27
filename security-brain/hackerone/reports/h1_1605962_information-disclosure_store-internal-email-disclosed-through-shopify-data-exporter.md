---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1605962'
original_report_id: '1605962'
title: store internal email disclosed through shopify-data-exporter
weakness: Information Disclosure
team_handle: shopify
created_at: '2022-06-18T15:12:34.390Z'
disclosed_at: '2022-09-15T19:21:56.713Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- information-disclosure
---

# store internal email disclosed through shopify-data-exporter

## Metadata

- HackerOne Report ID: 1605962
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2022-09-15T19:21:56.713Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hey Shopify,

When a store install ```shopify-data-exporter``` app to export various data of the store a link is sent to the store internal email. This internal email is disclosed via the below request to anyone 
```json
GET /?shop=your_store.myshopify.com HTTP/2
Host: shopify-data-exporter.shopifycloud.com
```
{F1779393}

## Shops Used to Test:
[xentest11.myshopify.com]

## Relevant Request IDs:
[54bb78a050a2fddbc3ae360ff72d1d3e]

## Steps To Reproduce:

  1.  Install ```shopify-data-exporter``` in your store (```https://apps.shopify.com/data-exporter-tax-compliance```)
  2.  After installing the app just add your store link in ```shop``` parameter in the above shown request
  3. In the response check for  ```data-recipient``` attribute. It exposes the internal store email.

## Impact

Store internal email disclose to anyone in ```shopify-data-exporter.shopifycloud.com?shop=``` via ```data-recipient``` attribute

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
