---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '347567'
original_report_id: '347567'
title: XSS in "explore-keywords-dropdown" results.
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: zomato
created_at: '2018-05-04T17:16:05.673Z'
disclosed_at: '2018-05-09T18:06:18.659Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS in "explore-keywords-dropdown" results.

## Metadata

- HackerOne Report ID: 347567
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: zomato
- Disclosed At: 2018-05-09T18:06:18.659Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It seems that people have exploited this vulnerability before on this website, however, it remains unpatched, so here I am reporting the vulnerability.

A XSS vulnerability exists when a restaurant or dish is created with a malicious name. The title of the dish or restaurant is not properly filtered by the web application. Any code in the dish or restaurant name is executed on the client.

DEMO: https://www.zomato.com/kingman-ks/restaurants, search for: single quote, double quote, GT angle bracket. '">

## Impact

An attacker could achieve XSS and inject hooks into the web browser (e.g. BeEF)

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
