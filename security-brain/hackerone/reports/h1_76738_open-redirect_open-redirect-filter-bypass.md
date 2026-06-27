---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '76738'
original_report_id: '76738'
title: Open redirect filter bypass
weakness: Open Redirect
team_handle: zaption
created_at: '2015-07-19T10:59:20.289Z'
disclosed_at: '2015-08-24T16:58:58.952Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- open-redirect
---

# Open redirect filter bypass

## Metadata

- HackerOne Report ID: 76738
- Weakness: Open Redirect
- Program: zaption
- Disclosed At: 2015-08-24T16:58:58.952Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi  , 

An open redirect is an application that takes a parameter and redirects a user to the parameter value without any validation. This vulnerability is used in phishing attacks to get users to visit malicious sites without realizing it.

its possible to bypass your redirect filter using : 
https://www.zaption.com/logout?returnTo=///evil.com/

`HTTP/1.1 302 Moved Temporarily
Access-Control-Allow-Origin: 
Cache-Control: private, must-revalidate
Content-Type: text/html; charset=utf-8
Date: Sun, 19 Jul 2015 10:55:48 GMT
Location: ///evil.com
P3P: CP="Zaption does not have a P3P policy. See privacy policy at http://zapt.io/privacy"
Pragma: no-cache
Vary: Accept, Accept-Encoding
Content-Length: 78
Connection: keep-alive

<p>Moved Temporarily. Redirecting to <a href="///evil.com">///evil.com</a></p>`

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
