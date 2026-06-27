---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1536461'
original_report_id: '1536461'
title: Reflected  XSS on  https://wwwapps.ups.com/ctc/request?loc=
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: ups
created_at: '2022-04-10T04:56:21.799Z'
disclosed_at: '2022-07-05T12:03:29.500Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: '*.ups.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected  XSS on  https://wwwapps.ups.com/ctc/request?loc=

## Metadata

- HackerOne Report ID: 1536461
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: ups
- Disclosed At: 2022-07-05T12:03:29.500Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Summary:
=========
Detalis XSS
-----------
Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

## Steps To Reproduce:


  1. Go to Those Links.
https://wwwapps.ups.com/ctc/request?loc=a:%27%22/%3Ea%22%3E%3Caa%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3Een_AW&WT.svl=
 
##FIX
Filter input on arrival
Encode data on output
Use appropriate response headers
Content Security Policy.
These all are standards concepts for fix the XSS vulnerabilities.

## Impact

screenshot:
F1686701
POC:
F1686705

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
