---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '14303'
original_report_id: '14303'
title: http://jetpack.me/ Self XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: automattic
created_at: '2014-05-31T20:19:55.730Z'
disclosed_at: '2014-07-08T10:00:24.281Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# http://jetpack.me/ Self XSS

## Metadata

- HackerOne Report ID: 14303
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: automattic
- Disclosed At: 2014-07-08T10:00:24.281Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there :)

I found a self XSS located at the front page of http://jetpack.me/, To reproduce this you have to scroll to the `Every feature!` part and search for `<img src=x onerror=alert(1)>` in the search engine.

Best regards,

Olivier Beg

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
