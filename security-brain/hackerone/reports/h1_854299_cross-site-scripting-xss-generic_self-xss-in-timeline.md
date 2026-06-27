---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '854299'
original_report_id: '854299'
title: Self XSS in Timeline
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2020-04-20T14:46:56.815Z'
disclosed_at: '2020-08-25T17:04:37.224Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Self XSS in Timeline

## Metadata

- HackerOne Report ID: 854299
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2020-08-25T17:04:37.224Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Copy the url `javascript:` XSS payload to any Timeline, then click url will trigger XSS.

{F796167}
{F796161}

I previously reported a storefront url XSS at #841361, then admin copy the url to Timeline is possibly.

## Impact

Self XSS

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
