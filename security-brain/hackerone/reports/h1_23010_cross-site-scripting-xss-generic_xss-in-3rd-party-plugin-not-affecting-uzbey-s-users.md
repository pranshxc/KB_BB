---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '23010'
original_report_id: '23010'
title: XSS in 3rd party plugin (not affecting Uzbey's users)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uzbey
created_at: '2014-08-08T04:07:20.039Z'
disclosed_at: '2014-11-02T19:39:23.192Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in 3rd party plugin (not affecting Uzbey's users)

## Metadata

- HackerOne Report ID: 23010
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uzbey
- Disclosed At: 2014-11-02T19:39:23.192Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Uzbey currently using a 3rd party solution from sharethis.com to share user's album.

It is possible to use this function as a medium to attack sharethis.com's users that using Uzbey service.

1- Create album using XSS payload
2- Share the album using Email function (letter icon)
3- XSS will execute.

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
