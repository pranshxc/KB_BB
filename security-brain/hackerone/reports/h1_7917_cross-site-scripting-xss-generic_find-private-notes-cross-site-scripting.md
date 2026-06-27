---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7917'
original_report_id: '7917'
title: Find, private notes Cross-site scripting.
weakness: Cross-site Scripting (XSS) - Generic
team_handle: respondly
created_at: '2014-04-17T20:19:20.280Z'
disclosed_at: '2014-04-21T16:30:41.842Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Find, private notes Cross-site scripting.

## Metadata

- HackerOne Report ID: 7917
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: respondly
- Disclosed At: 2014-04-21T16:30:41.842Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi.

When I go to the find page and insert a `private note`, with as content : `<img src='x' onerror='alert(4)'` it will execute directly.

As preview :
1.) http://prntscr.com/3axvz5
2.) http://prntscr.com/3axw3k

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
