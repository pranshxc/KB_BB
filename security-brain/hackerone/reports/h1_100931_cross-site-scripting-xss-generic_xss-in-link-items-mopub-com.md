---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '100931'
original_report_id: '100931'
title: xss in link items (mopub.com)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2015-11-22T09:05:00.282Z'
disclosed_at: '2016-07-05T19:16:40.424Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# xss in link items (mopub.com)

## Metadata

- HackerOne Report ID: 100931
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2016-07-05T19:16:40.424Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

1)go link items and select text,tile
2)enter image and give click url as javascript://%0a%0dalert(document.cookie)
3)xss pop's up 
it is not a self xss because admin can invite many people to his inventory and there sessions can be hijacked.
regards
prashanth 
dups team :)

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
