---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '122849'
original_report_id: '122849'
title: Stored XSS in https://checkout.shopify.com/
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2016-03-13T18:26:01.755Z'
disclosed_at: '2016-03-15T22:32:20.939Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in https://checkout.shopify.com/

## Metadata

- HackerOne Report ID: 122849
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2016-03-15T22:32:20.939Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**STEPS TO REPRODUCE**

1. Go to http://hardware.shopify.com/products/custom-gift-card?variant=976094353 and Design your own gift card.
2. Change file type to url on the upload field.
3. Add the payload `javascript:alert(document.domain);//https://cdn.shopify.com/s/files/1/0224/0965/uploads/1fc1042c960abdb2f35c0950900a7b2c.svg`
4. Then add the item to the cart and go to checkout.
5. On the checkout page click the Artwork File and the XSS will trigger.

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
