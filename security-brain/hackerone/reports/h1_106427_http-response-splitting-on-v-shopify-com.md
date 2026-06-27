---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '106427'
original_report_id: '106427'
title: HTTP-Response-Splitting on v.shopify.com
team_handle: shopify
created_at: '2015-12-22T09:03:44.475Z'
disclosed_at: '2016-01-17T19:20:36.568Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
---

# HTTP-Response-Splitting on v.shopify.com

## Metadata

- HackerOne Report ID: 106427
- Weakness: 
- Program: shopify
- Disclosed At: 2016-01-17T19:20:36.568Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I discovered a HTTP-Response-Splitting issue on v.shopify.com

Steps to reproduce:
Call the following URL in any browser and catch the response ( e.g. with burp )
https://v.shopify.com/last_shop?shop=krankopwnz.myshopify.com%0d%0aContent-Length:%200%0d%0a%0d%0aHTTP/1.1%20200%20OK%0d%0aContent-Type:%20text/html%0d%0aContent-Length:%2019%0d%0a%0d%0a<html>deface</html>

When you look at screenshot 1 in attachments, you can see that the response contains 2 headers.

According to OWASP, this could be used for " Cross-User Defacement, Cache Poisoning, Cross-site Scripting (XSS) and Page Hijacking." ( https://www.owasp.org/index.php/HTTP_Response_Splitting )

You could convince victims via social engineering to click the provided link, which can contain a cloned login-page of shopify for example. If he sits behind a proxy, which caches the responses the following users will see your evil login-page when calling that address.

A fix would be to disallow line-breaks and any non printable characters in the "shop"-parameter

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
