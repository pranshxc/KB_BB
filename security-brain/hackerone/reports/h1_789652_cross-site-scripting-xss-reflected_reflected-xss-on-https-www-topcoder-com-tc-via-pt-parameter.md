---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '789652'
original_report_id: '789652'
title: Reflected-XSS on https://www.topcoder.com/tc via pt parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: topcoder
created_at: '2020-02-05T23:29:12.057Z'
disclosed_at: '2020-09-04T19:53:55.302Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: www.topcoder.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected-XSS on https://www.topcoder.com/tc via pt parameter

## Metadata

- HackerOne Report ID: 789652
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: topcoder
- Disclosed At: 2020-09-04T19:53:55.302Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Summary:
I Found an XSS(Reflected) at the URL mentioned 
and the injected parameter is: pt
Steps To Reproduce:
1-go to this URL [https://www.topcoder.com/tc?module=ReviewBoard&pt=1]
$$you will recognize that is parameter (pt) is reflecting its value into the page
2- try injecting this parameter with HTML tags or XSS payloads 
the payloads I used 
1-for HTML Injection = <a+href="https://bing.com">LINK</a>
2-for XSS = <script>confirm(1)</script>

## Impact

XSS can be used for :
1- Cookie stealing 
2- Pishing attacks
3- URL redirection 
etc....

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
