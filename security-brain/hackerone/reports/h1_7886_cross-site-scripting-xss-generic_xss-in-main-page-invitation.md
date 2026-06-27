---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7886'
original_report_id: '7886'
title: XSS in main page (invitation)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localize
created_at: '2014-04-17T19:03:01.617Z'
disclosed_at: '2014-04-18T01:12:10.779Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in main page (invitation)

## Metadata

- HackerOne Report ID: 7886
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localize
- Disclosed At: 2014-04-18T01:12:10.779Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

If a project name is saved with a XSS string such as: 
“><svg onload="prompt(/xss/);"><!--

and a translator visits and requests and invite,  it'll result in the xss executing in the main page, due to the fact that it shows your requests.

Screen:
http://prntscr.com/3awwuv

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
