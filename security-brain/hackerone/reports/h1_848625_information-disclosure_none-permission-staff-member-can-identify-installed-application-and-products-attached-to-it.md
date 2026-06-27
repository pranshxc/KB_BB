---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '848625'
original_report_id: '848625'
title: None permission staff member can identify installed application and products
  attached to it
weakness: Information Disclosure
team_handle: shopify
created_at: '2020-04-13T16:26:29.444Z'
disclosed_at: '2020-04-21T21:17:40.603Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# None permission staff member can identify installed application and products attached to it

## Metadata

- HackerOne Report ID: 848625
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2020-04-21T21:17:40.603Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,
To see if a store has application installed and which products its configured the staff member should have application permission otherwise nothing is visible but i found a way that let none permission staff member to identify if the store has installed Digital Downloads and if the application configured on a particular products.

POC:
1)Create two user A and B, login to A and create a store, test.myshopify.com
2)Add user B as staff member to test.myshopify.com with no permission.
3)From user A, go test.myshopify.com and create two product called Tt and PP
4)Install Digital Downloads for this store and configure Tt to this app.
5)Login back to user B and create an independent store, test100.myshopify.com and install Digital Downloads on this store.
6)Now go to user A store (test.myshopfy.com) and click app and click Digital downlands and right click on the product, you will get below urli
https://delivery.shopifyapps.com/products/3785077260000
7)Copy paste to this url from user B account (login as user B) and you can see that a message as below.
Digital Downloads/Tt
This indicate that Digital Downloads is installed on test.myshopfy.com store (which this user has 0 permission) and configured on the product Tt.
8)If you user the same url with PP product id, nothing is shown

User B can get products ids via source page of user A store as user B is staff member even though none permission 

view-source:https://test.myshopify.com/products/tt

<script id="__st">var __st={"a":2616790000,"offset":-14400,"reqid":"fff-bbb-ccc-bbb-qqq","pageurl":"test-myshopify.com\/products\/tt","u":"184d9400000a","p":"product","rtyp":"product","rid":3785077260000};</script>

## Impact

This is an information disclosure, none permission member staff should not know which application is installed and what product is configured for this application.

Please find the screen shots

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
