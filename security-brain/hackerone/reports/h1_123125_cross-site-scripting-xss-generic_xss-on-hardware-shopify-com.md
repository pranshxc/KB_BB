---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '123125'
original_report_id: '123125'
title: XSS on hardware.shopify.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2016-03-15T01:03:38.664Z'
disclosed_at: '2016-04-09T00:03:05.637Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on hardware.shopify.com

## Metadata

- HackerOne Report ID: 123125
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2016-04-09T00:03:05.637Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This is stored vulnerability for all your users, not only registered or signed in.

Vulnerable parameter: properties[builder_id] at *.shopify.com/cart/add
The vulnerability is in array levels. When you try something like 
properties[builder_id][second_parameter]=value,
you will see many corrupted tags in HTML because 2-level array will return as 
"builder_id":{"second_parameter ":"value"} instead of "builder_id":"shapp_options_421549285_1455208671885" in cart.js

So you could inject your code in tr,div,a,insert  tags. All you need - is redirect a victim to special url. For example, you cold try this: properties[builder_id][%20onmouseover%3dalert(1)%20]=value 
Script will strike when victim will move a coursor over product.

Here is a link with your cookies in a harware store for example:
http://hardware.shopify.com/cart/add?&id=1106494145&iPad%20Stand=1120276481&Cash%20Drawer=1120176153&Receipt%20Printer=1120166789&attributes[cart_exists]=true&properties[builder_id][%20onmouseover%3dalert(document.cookie)%20]=shapp_options_421549285_1455208671885&properties[master_builder][]=1&properties[test]=test&properties[value]=11&add

I recommend you to check incoming parameters for arrays like here:
http://php.net/manual/en/function.is-array.php

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
