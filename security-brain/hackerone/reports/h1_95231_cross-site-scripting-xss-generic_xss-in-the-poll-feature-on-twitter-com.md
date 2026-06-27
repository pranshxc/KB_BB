---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '95231'
original_report_id: '95231'
title: XSS in the "Poll" Feature on Twitter.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2015-10-22T20:50:19.221Z'
disclosed_at: '2016-08-12T16:48:07.800Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in the "Poll" Feature on Twitter.com

## Metadata

- HackerOne Report ID: 95231
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2016-08-12T16:48:07.800Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I have found an XSS on the "Poll" feature on Twitter.com. 

Payload Example:
`<img src=x onerror=alert(1)>`

Screenshot: I have attached a screenshot in this submission in order to demonstrate the issue.

Best,
Mazin

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
