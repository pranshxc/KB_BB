---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7882'
original_report_id: '7882'
title: XSS in main page
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localize
created_at: '2014-04-17T18:56:21.793Z'
disclosed_at: '2014-04-18T01:15:06.995Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in main page

## Metadata

- HackerOne Report ID: 7882
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localize
- Disclosed At: 2014-04-18T01:15:06.995Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

If a project name is saved with a XSS string such as: 
“><svg onload="prompt(/xss/);"><!--

and a translator visits it, it'll result in the xss executing in the main page, due to the fact that it shows your recent visits.

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
