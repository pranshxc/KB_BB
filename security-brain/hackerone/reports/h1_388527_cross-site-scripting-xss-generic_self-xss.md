---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '388527'
original_report_id: '388527'
title: Self xss
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2018-07-30T16:06:47.936Z'
disclosed_at: '2020-04-05T10:26:43.041Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Self xss

## Metadata

- HackerOne Report ID: 388527
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2020-04-05T10:26:43.041Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I found self xss your main domain.

I m sending details and I attached poc video.

Pls open 

https://nextcloud.com/about/

Use burp suite and active intercept.

Refresh this url.

And pls add this payload your url.

></title>"><script>alert(205)</script>'"><marquee><h1>nextcloud.com</h1></marquee>


Pls click intercept off and page refreshing.

Now you see xss alert.

## Impact

https://github.com/dxa4481/XSSJacking

Exploit and Impact kit for self xss

Regards.

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
