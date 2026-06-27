---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '950700'
original_report_id: '950700'
title: Reflected XSS in https://www.█████/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-08-04T07:51:25.491Z'
disclosed_at: '2020-09-29T20:33:43.160Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 23
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in https://www.█████/

## Metadata

- HackerOne Report ID: 950700
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2020-09-29T20:33:43.160Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Security Team,
I would like to report the XSS vulnerability on your system.
Steps To Reproduce:
Visit the following POC link and move your mouse allover index page: 
https://www.████/(Z(%22onmouseover=alert%60%60%20%22))/████████/█████.aspx

1. Tested on firefox browser:

███████
2.Tested on google chrome browser:

█████████

## Impact

An XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim, or for phishing attacks.

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
