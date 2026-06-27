---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '168458'
original_report_id: '168458'
title: Stored XSS in https://productreviews.shopifyapps.com/proxy/v4/reviews/product
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2016-09-14T23:26:18.715Z'
disclosed_at: '2019-11-08T11:03:47.871Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in https://productreviews.shopifyapps.com/proxy/v4/reviews/product

## Metadata

- HackerOne Report ID: 168458
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2019-11-08T11:03:47.871Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi , I have found a stored XSS issue in `https://productreviews.shopifyapps.com`
#Details:
Going to `https://productreviews.shopifyapps.com/proxy/v4/reviews/product?product_id=8254331011&version=v4&shop=zh5403-attacker.myshopify.com&_=cache&callback=test` will show you the details of a product with the id `8254331011` in JSON format.
Having the `callback` parameter in the url will return `Content-Type:application/javascript` in the response headers, however, if the url does not contain that parameter, the response won't contain **Content-Type** header in the response so the browser will display the page as **text/html**. 
#PoC:
I have created a product with an XSS payload in the title and added the id in the url.
`https://productreviews.shopifyapps.com/proxy/v4/reviews/product?product_id=8254331011&version=v4&shop=zh5403-attacker.myshopify.com&_=cache&callback=test`

PS: This was originally found at `https://productreviews.shopifycdn.com/proxy/v4/reviews/product?product_id=8254331011&version=v4&shop=zh5403-attacker.myshopify.com&_=xxxxxxxx` but I found that it also works for `https://productreviews.shopifyapps.com`

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
