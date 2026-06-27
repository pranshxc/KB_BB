---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8862'
original_report_id: '8862'
title: XSS in Stopthehacker support
weakness: Cross-site Scripting (XSS) - Generic
team_handle: stopthehacker
created_at: '2014-04-21T21:55:52.622Z'
disclosed_at: '2014-07-19T00:31:17.258Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in Stopthehacker support

## Metadata

- HackerOne Report ID: 8862
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: stopthehacker
- Disclosed At: 2014-07-19T00:31:17.258Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

1. go to http://www.stopthehacker.com/support/
2. input "><img src=x onerror=prompt(1)> in the search box (use firefox)
3. A prompt box will appear. XSSed.

Thank you sir.

Clifford

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
