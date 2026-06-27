---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '230234'
original_report_id: '230234'
title: '[mercantile.wordpress.org] Reflected XSS via AngularJS Template Injection'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: wordpress
created_at: '2017-05-20T13:56:49.092Z'
disclosed_at: '2017-06-14T18:35:23.938Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [mercantile.wordpress.org] Reflected XSS via AngularJS Template Injection

## Metadata

- HackerOne Report ID: 230234
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: wordpress
- Disclosed At: 2017-06-14T18:35:23.938Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

By injecting a crafted AngularJS payload into the `search` endpoint on the WordPress Swag Store, it was possible to achieve reflected XSS further to resolved report #221893.

I came across a potential exploitation vector after noticing that a search query for `{{2*2}}` returned `4` in the site title response.

## Conditions Verified In
* Firefox 52.0.3 – stable
* Safari 10.1 – stable

## Proof of Concept URL
```
https://mercantile.wordpress.org/search/{{constructor.constructor('alert(document.domain)')()}}
```

## Screenshot

{F186517}

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
