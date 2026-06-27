---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '56779'
original_report_id: '56779'
title: XSS on ecommerce.shopify.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-04-16T19:50:58.471Z'
disclosed_at: '2015-09-06T20:25:01.310Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on ecommerce.shopify.com

## Metadata

- HackerOne Report ID: 56779
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-09-06T20:25:01.310Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello! I would like to report about XSS on ecommerce.shopify.com domain.

Here is a PoC that gives You alert box with "123" content: https://ecommerce.shopify.com/grader?url=imdb.jurgens.lv

This Ecommerce Store Grader Tool gives You a list of sources of image tags that should have "alt" attribute on tested website (screenshot "where.png"). So, on Your website (imdb.jurgens.lv in my case), You can create <img> tag with the "src" attribute value "111<img src=1 onerror=alert(123)>". Then put link to Your website to this Grader Tool and after that it will show You error block "Some of the images on your homepage are missing ALT tags." which will contain Your <img> tag "src" attribute with embed <img> tag there.

You can see full example of source on http://imdb.jurgens.lv

Generally, this vulnerability exists because of no filtering in shown "src" attributes.

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
