---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '846432'
original_report_id: '846432'
title: xss on bittorrent.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: btfs
created_at: '2020-04-10T13:08:07.499Z'
disclosed_at: '2020-05-11T23:13:16.464Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# xss on bittorrent.com

## Metadata

- HackerOne Report ID: 846432
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: btfs
- Disclosed At: 2020-05-11T23:13:16.464Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

hi team 
i realized xss bug on  headers.php.

https://www.bittorrent.com/scripts/site/headers.php?_=1586521900793&callback=<PAYLOAD>
https://www.bittorrent.com/scripts/social/get_tweet.php?_=1586521900791&callback=<PAYLOAD>
its works on IE browsers.

## Impact

fix them

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
