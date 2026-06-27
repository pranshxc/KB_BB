---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '859806'
original_report_id: '859806'
title: Flash Based Reflected XSS on www.grouplogic.com/jwplayer/player.swf
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: acronis
created_at: '2020-04-26T17:33:38.251Z'
disclosed_at: '2021-04-13T13:24:03.004Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 84
asset_identifier: Other Acronis Domains
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Flash Based Reflected XSS on www.grouplogic.com/jwplayer/player.swf

## Metadata

- HackerOne Report ID: 859806
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: acronis
- Disclosed At: 2021-04-13T13:24:03.004Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello there,
I hope you are well!

Steps:
1. Open firefox.
2. Go to http://www.grouplogic.com/jwplayer/player.swf?playerready=alert(document.domain) 
You will see xss alert.

## Impact

Reflected XSS

Regards,
@mygf

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
