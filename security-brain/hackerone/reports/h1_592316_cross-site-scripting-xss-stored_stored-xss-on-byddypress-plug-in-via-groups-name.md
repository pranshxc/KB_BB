---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '592316'
original_report_id: '592316'
title: Stored XSS on byddypress Plug-in via groups name
weakness: Cross-site Scripting (XSS) - Stored
team_handle: wordpress
created_at: '2019-05-29T13:45:33.100Z'
disclosed_at: '2019-07-27T00:35:51.929Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 131
asset_identifier: BuddyPress Core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on byddypress Plug-in via groups name

## Metadata

- HackerOne Report ID: 592316
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: wordpress
- Disclosed At: 2019-07-27T00:35:51.929Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi, I found that there is a storage xss in another output group name, but this xss needs to press the key combination to trigger. Just create or modify the group information, set the group name to the following payload, 
```
<a href="accesskey=x onclick=alert(document .domain)//"></a>
```
and then access Group page, 
if you are macos need to press, 
shift+control+option+x,
if you are windows, 
you need to press shift+alt+x, 
then it will trigger xss
{F498582}

Don't forget to enable the group feature

## Impact

Rce via xss

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
