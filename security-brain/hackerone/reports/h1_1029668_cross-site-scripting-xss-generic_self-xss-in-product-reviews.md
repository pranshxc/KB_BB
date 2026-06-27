---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1029668'
original_report_id: '1029668'
title: Self xss in product reviews
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2020-11-09T00:54:42.273Z'
disclosed_at: '2020-11-19T23:29:16.179Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 29
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Self xss in product reviews

## Metadata

- HackerOne Report ID: 1029668
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2020-11-19T23:29:16.179Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1、install app `Product Reviews`
{F1070556} 

2、Open a product and write a review

3、Press F12 on the keyboard，Change the type of email to text.

4、Write in email`"><img src=a onerror=alert(1)>123@sdf.com`.
{F1070565}

5、Write other required fields，then submit.
{F1070566}

## Impact

Self xss

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
