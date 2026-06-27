---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '130889'
original_report_id: '130889'
title: Reflected XSS in scores.ubnt.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: ui
created_at: '2016-04-14T19:43:14.557Z'
disclosed_at: '2016-08-11T12:41:57.736Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS in scores.ubnt.com

## Metadata

- HackerOne Report ID: 130889
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: ui
- Disclosed At: 2016-08-11T12:41:57.736Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Parameter p in https://scores.ubnt.com/form.html?uid=1&p=airFiber is vulnerable to XSS. If a user logs in at https://account.ubnt.com/login and visits https://scores.ubnt.com/form.html?uid=1&p=airFiber"><script>alert(document.cookie);</script>, a message box will be presented with his cookie. Attached is a POC (xss-scores-chrome.png). 

Vulnerable code of https://scores.ubnt.com/form.html is also attached (xss-vuln-code.png), where it is visible that product  (parameter p) is included without proper input validation. 

This vulnerability can be used to steal cookies (session data) from authenticated users  as also for phishing attacks. It can be exploited by  sending a malicious link to users or posting this link to a forum. 

As UBNT implements SSO, this can be very dangerous. 

To mitigate this vulnerability, consider the following:

*output encoding of all special characters
*input validation of data suplied from users

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
