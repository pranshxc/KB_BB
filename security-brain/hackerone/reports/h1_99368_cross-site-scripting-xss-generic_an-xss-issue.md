---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '99368'
original_report_id: '99368'
title: an xss issue
weakness: Cross-site Scripting (XSS) - Generic
team_handle: algolia
created_at: '2015-11-12T21:24:00.281Z'
disclosed_at: '2016-05-22T15:05:16.841Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# an xss issue

## Metadata

- HackerOne Report ID: 99368
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: algolia
- Disclosed At: 2016-05-22T15:05:16.841Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

i found an xss issue here :
https://www.algolia.com/explorer#?index=test&tab=ranking
i tried to put  an xss payload ("><img src=x onerror=alert(0)>)
in index > ranking> so i put the xss payload in Ranking formula then hit save ...when it is being saved the xss payload is being stored that upon Indices xss payload executed
p.s please screen shot

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
