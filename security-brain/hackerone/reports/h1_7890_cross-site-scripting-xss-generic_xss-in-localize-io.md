---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7890'
original_report_id: '7890'
title: XSS in Localize.io
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localize
created_at: '2014-04-17T19:11:16.087Z'
disclosed_at: '2014-04-18T04:22:43.534Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in Localize.io

## Metadata

- HackerOne Report ID: 7890
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localize
- Disclosed At: 2014-04-18T04:22:43.534Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

During signup I used "></code><svg/onload=prompt(1)> as my password.Just after pressing sign up I was forwarded to a new page,where that page was showing my username and asked to click to view my password.When I clicked the javascript executed.
Attachment: xss.png

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
