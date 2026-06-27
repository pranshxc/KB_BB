---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '738072'
original_report_id: '738072'
title: XSS on product comments in transfers
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2019-11-15T06:24:31.708Z'
disclosed_at: '2019-12-09T19:55:32.859Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS on product comments in transfers

## Metadata

- HackerOne Report ID: 738072
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2019-12-09T19:55:32.859Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

summery: 

You are able to copy and paste stored XSS code into the comment section of a product in the transfers tab and receive the error.

Reproduce:

1. Create a product with the name '"'><img src=x onerror=alert(domain.domain)>'
2. add a transfer with that product
3. now go back to the product use the code button and type the same code for the title . '"'><img src=x onerror=alert(domain.domain)>'
4. you will get a XSS pop-up however ignore it. as soon as you get here you need to get out of the code setting and into the normal text and copy the the little piece of code with the image.
5. delete the code that we put in the html for the XSS.
6. go back to transfers and paste the code that we copied there
7. error

## Impact

steal cookie

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
