---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '429679'
original_report_id: '429679'
title: POST-based XSS on apps.shopify.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2018-10-27T14:27:47.837Z'
disclosed_at: '2019-03-14T10:50:42.120Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 67
asset_identifier: apps.shopify.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# POST-based XSS on apps.shopify.com

## Metadata

- HackerOne Report ID: 429679
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2019-03-14T10:50:42.120Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Shopify team! I found a post-based XSS which may be shared to other users and occurs in firefox, IE, Edge.

How to reproduce:
1. at partners.shopify.com go to apps -> choose one -> more actions -> create shopify app store listing
2. you will get redirected to url with ?signature parameter. Full copy whole URL.
3. as App name specify </script><svg onload=alert()>
4. in incognito tab open URL copied in step 2
5. click Preview changes

How to fix: 

Sanitize parameters which are getting inserted in <script> tag.

## Impact

POST-based XSS in firefox/ie/edge. probably safari too

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
