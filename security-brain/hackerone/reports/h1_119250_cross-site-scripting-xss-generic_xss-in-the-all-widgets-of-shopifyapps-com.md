---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '119250'
original_report_id: '119250'
title: xss in the all widgets of shopifyapps.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2016-02-28T08:41:05.351Z'
disclosed_at: '2016-03-16T00:03:12.493Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# xss in the all widgets of shopifyapps.com

## Metadata

- HackerOne Report ID: 119250
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2016-03-16T00:03:12.493Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

i found xss in all widgets.shopifyapps.com/* (google dork:site:widgets.shopifyapps.com)
the parameter "padding" is vulnerable,xss payload - }%0a{}*{x:expression(alert(1))}%0a{

xss does work in inetrnet explorer browsers( for ie10,ie11 in compatibility mode) , for ie5,ie6,ie7

for ie8,ie9 javascript is disabled, the content of page to have a strings:
<!--[if IE 8]><html class="ie ie8 no-js" lang="en"> <![endif]-->
<!--[if IE 9 ]><html class="ie ie9 no-js"> <![endif]-->
<!--[if gt IE 9 ]><html class="ie gt-ie9 no-js"> <![endif]-->
 

how to reproduce:

1. to use ineternet explorer browser 10, for example
2. go to the page: 

https://widgets.shopifyapps.com/products/a-luv-u-pet-pink-geordie-card?shop=the-mag-shop.myshopify.com&style=artgallery&image-size=medium&border-color=%23af4fcc&padding=}%0a{}*{x:expression(alert(1))}%0a{&button-text=Buy+Now+in+The+Mag+shop&destination=product

3.  to use compatibility mode in ie10 (to use ie7 mode by default)
4. to see alert box with 1

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
