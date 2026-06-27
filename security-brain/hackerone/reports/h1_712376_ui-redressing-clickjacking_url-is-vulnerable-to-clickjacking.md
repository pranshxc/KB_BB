---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '712376'
original_report_id: '712376'
title: URL is vulnerable to clickjacking
weakness: UI Redressing (Clickjacking)
team_handle: mycrypto
created_at: '2019-10-11T19:07:32.361Z'
disclosed_at: '2019-10-17T17:41:13.078Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: etherscamdb.info
asset_type: URL
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# URL is vulnerable to clickjacking

## Metadata

- HackerOne Report ID: 712376
- Weakness: UI Redressing (Clickjacking)
- Program: mycrypto
- Disclosed At: 2019-10-17T17:41:13.078Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##i'm not sure if this vulnerability is in scope or not , kindly if you don't accept this report please close it as informative or allow me to self close it thanks in advance

##Summary:
URLs missing CSP headers they are vulnerable to clickjacking.

##Steps To Reproduce:
run the below code that i had attached
{F605393}

##Supporting Material/References:
https://hackerone.com/reports/337219

here is a refrence from owasp for more details : https://www.owasp.org/index.php/Clickjacking
you can find down
## Defending against Clickjacking
There are two main ways to prevent clickjacking:
Sending the proper Content Security Policy (CSP) frame-ancestors directive response headers that instruct the browser to not allow framing from other domains. (This replaces the older X-Frame-Options HTTP headers.)

##POC:
also this screenshot shows that csp header isn't implemented ( you can find the same when you visit
https://observatory.mozilla.org/analyze/etherscamdb.info
{F605394}

##Mitigation and fix:
implement csp header

also here is another link for more information about the fix :
https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Clickjacking_Defense_Cheat_Sheet.md

if you need any help please tell me i'd be happy to help out thanks in advance

## Impact

hackers embed the content your page within another page which may cause loss of reputation and trust as a result

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
