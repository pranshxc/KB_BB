---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '423454'
original_report_id: '423454'
title: H1514 Stored XSS on Wholesale sales channel allows cross-organization data
  leakage
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2018-10-13T18:45:38.462Z'
disclosed_at: '2019-11-01T20:49:19.323Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# H1514 Stored XSS on Wholesale sales channel allows cross-organization data leakage

## Metadata

- HackerOne Report ID: 423454
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2019-11-01T20:49:19.323Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

There exists a stored XSS vulnerability via the Wholesale sales channel at https://wholesale.shopifyapps.com. This allows an attacker who shares one shop with an account owner to access the Wholesale sales channel of any shop belonging to the owner.

## Steps To Reproduce:

  1. Visit https://wholesale.shopifyapps.com and add the Wholesale integration to your account.
  1. Navigate to the Wholesale sales channel at https://your-store.myshopify.com/admin/apps/wholesale.
  1. Navigate to create a new price list import.
  1. Modify the sample CSV file at https://help.shopify.com/manual/sell-online/wholesale/channel/price-lists-customers/import-prices/sample-csv-sku.csv to include the SKU of one of your shop's products.
  1. Upload the CSV file.
  1. After creating the price list, modify the price list and intercept the request to `POST /admin/shops/x/price_lists/x`.
  1. Modify the `price_list[csv_file_name]` parameter to include an XSS payload, such as `sample-csv-sku.csv"-alert(document.domain)-"`.
  1. Navigate back to the newly created price list. Observe that when visiting the page, the XSS payload will fire on the embedded domain `https://wholesale.shopifyapps.com`:

    {F360186}

  1. As this domain is shared across shops, this can be exploited to access the Wholesale information of any store a user has access to.

## Impact

An attacker with the `Apps` permission who shares one shop with an owner of multiple stores (e.g. via Shopify partners) can exploit this vulnerability to gain access to the Wholesale sales channel of any shop belonging to the owner.

As stated when authenticating with Wholesale:

> Wholesale will be able to access data such as customer names, e-mail addresses, phone numbers, physical addresses, geolocations, IP addresses, and browser user agents.

As a result, this allows access to extensive customer information, as well as the ability to modify any Wholesale information.

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
