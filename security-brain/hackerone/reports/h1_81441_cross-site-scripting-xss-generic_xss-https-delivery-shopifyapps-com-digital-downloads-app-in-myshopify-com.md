---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '81441'
original_report_id: '81441'
title: XSS https://delivery.shopifyapps.com/  (Digital Downloads App  in myshopify.com)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-08-09T20:12:25.508Z'
disclosed_at: '2015-08-24T22:29:00.454Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS https://delivery.shopifyapps.com/  (Digital Downloads App  in myshopify.com)

## Metadata

- HackerOne Report ID: 81441
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-08-24T22:29:00.454Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello
Installing the Digital Downloads App in *.myshopify.com
1-install the app  https://apps.shopify.com/digital-downloads
2-select product and click Add Digital Attachment 
3-click to upload file and upload file with name <svg onload=alert(1)>
the code  <svg onload=alert(1)> will execute XSS

<span class="file-name"><strong>Success:</strong> <svg onload="alert(1)"/></span>

tested in firefox

Hadji Samir

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
