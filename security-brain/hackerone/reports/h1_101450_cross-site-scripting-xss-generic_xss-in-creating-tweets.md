---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '101450'
original_report_id: '101450'
title: XSS in creating tweets
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-11-24T12:34:34.454Z'
disclosed_at: '2015-12-03T22:02:26.038Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in creating tweets

## Metadata

- HackerOne Report ID: 101450
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-12-03T22:02:26.038Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I found an XSS while tweeting my product.
To reproduce:
* Create new tweet.
* Select any product.
* Input in message content `"><img src=x onerror=alert(document.domain)>
* XSS executes.
* Hit Publish. XSS also executes.



Cheers!

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
