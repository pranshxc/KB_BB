---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1400309'
original_report_id: '1400309'
title: '[https://shipit-sox-staging.shopifycloud.com] Presence of multiple vulnerabilities
  present in Ruby On Rails'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: shopify
created_at: '2021-11-15T07:16:46.210Z'
disclosed_at: '2022-04-16T17:19:48.676Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: '*.shopifycloud.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# [https://shipit-sox-staging.shopifycloud.com] Presence of multiple vulnerabilities present in Ruby On Rails

## Metadata

- HackerOne Report ID: 1400309
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: shopify
- Disclosed At: 2022-04-16T17:19:48.676Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://shipit-sox-staging.shopifycloud.com seems to be running 6.0.0 < rails < 6.0.3.2 which is prone to multiple vulnerabilities via csrf including open redirect, xss & rce as reported at https://hackerone.com/reports/904059

## Impact

presence of multiple vulnerabilities can cause wide variety of damage.

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
