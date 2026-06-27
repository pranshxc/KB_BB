---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '361647'
original_report_id: '361647'
title: Reflective XSS at olx.ph
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: olx
created_at: '2018-06-04T11:28:05.430Z'
disclosed_at: '2018-09-23T10:02:18.729Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflective XSS at olx.ph

## Metadata

- HackerOne Report ID: 361647
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: olx
- Disclosed At: 2018-09-23T10:02:18.729Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I would like to report a reflective  XSS  at [https://www.olx.ph](https://www.olx.ph).

## Steps to reproduce
* Visit the following link: [https://www.olx.ph/all-results?q=car&utm_source=Opt_Homepage_Var_0&utm_medium=Search&utm_campaign=toto%27-alert(document.domain)-%27](https://www.olx.ph/all-results?q=car&utm_source=Opt_Homepage_Var_0&utm_medium=Search&utm_campaign=toto%27-alert(document.domain)-%27)
* An XSS should pop-up

{F305078}

## Technical Details
The paramter ```utm_campaign``` don't escape single quote ```'``` that's why the following payload to work: 
```
'-alert(document.domain)-'
```
Please note that the parameter value is  reflected  29 times, 4 times inside JS code, variables were using single quotes.

{F305079}
{F305080}

## Mitigation
Correctly escape and sanitize user input.

## Impact

Session Hijacking and everything related / controlled by JS that could lead to account takeover...

## XSS with cookie:

{F305082}

Best,
Taha Ibrahim DRAIDIA

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
