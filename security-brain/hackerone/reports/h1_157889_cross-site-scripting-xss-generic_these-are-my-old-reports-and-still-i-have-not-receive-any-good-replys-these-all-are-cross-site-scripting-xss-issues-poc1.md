---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '157889'
original_report_id: '157889'
title: 'these are my old reports and still i have not receive any good replys, these
  all are Cross Site Scripting(XSS) issues: POC1: https://www.youtube.com/w'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-08-09T15:13:54.793Z'
disclosed_at: '2016-09-14T12:07:34.670Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# these are my old reports and still i have not receive any good replys, these all are Cross Site Scripting(XSS) issues: POC1: https://www.youtube.com/w

## Metadata

- HackerOne Report ID: 157889
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-09-14T12:07:34.670Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

these are my old reports and still i have not receive any good replys,
these all are Cross Site Scripting(XSS) issues:
POC1: https://www.youtube.com/watch?v=zpckM4AjeWk 
POC2: https://www.youtube.com/watch?v=L4h_WJfIdow
POC3: https://youtu.be/vWqVpPbn0AI ,
i am waiting for good reply...

[DETAILS]:
XSS(Cross Site Script)-Vulnerability:
President Cross Site Scriptting Vulnerability Exist on message for ad page via ad data such as title & Desscription.
Steps:
1-> open olx.com
2-> click on Submit a Free Ad
3-> now fill data in title and desscription "><img src="err" onerror="alert('President Cross Site Scriptting - XSS');">
4-> and fill complete form then click on Submit to save ad
5-> now you will see alert box with text 'President Cross Site Scriptting - XSS' because XSS.

XSS in search parameter:
view-source:https://www.olx.in/all-results/q-XSS/

Persistent XSS vulnerability in OLX:
https://youtu.be/vWqVpPbn0AI

https://www.youtube.com/watch?v=zpckM4AjeWk
https://www.youtube.com/watch?v=L4h_WJfIdow
https://youtu.be/vWqVpPbn0AI

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
