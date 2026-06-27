---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '413442'
original_report_id: '413442'
title: '[chatws25.stream.highwebmedia.com] - Reflected XSS in c parameter'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: chaturbate
created_at: '2018-09-24T16:31:10.710Z'
disclosed_at: '2018-09-26T12:15:35.623Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: '*.highwebmedia.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [chatws25.stream.highwebmedia.com] - Reflected XSS in c parameter

## Metadata

- HackerOne Report ID: 413442
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: chaturbate
- Disclosed At: 2018-09-26T12:15:35.623Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Found that `chatws25.stream.highwebmedia.com` is vulnerable to reflected XSS in `c` parameter, we can verify it with following URL, it is also a Cloudflare filter bypass:

https://chatws25.stream.highwebmedia.com/ws/007/tgpraolp/htmlfile?c=███

```
https://chatws25.stream.highwebmedia.com/ws/007/tgpraolp/htmlfile?c=███████
```

{F350412}

## Impact

One of the most common XSS attack vectors is to hijack legitimate user accounts by stealing their session cookies.

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
