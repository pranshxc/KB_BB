---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '381553'
original_report_id: '381553'
title: HTML Injection with XSS possible
weakness: Cross-site Scripting (XSS) - Stored
team_handle: imgur
created_at: '2018-07-14T05:07:50.017Z'
disclosed_at: '2021-04-29T21:15:42.346Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 54
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# HTML Injection with XSS possible

## Metadata

- HackerOne Report ID: 381553
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: imgur
- Disclosed At: 2021-04-29T21:15:42.346Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi, I found HTML Injection on imgur.com 

Description:
I couldn't get xss but i was able to include videos on my profile and also i was able to redirect users to malicious websites

POC (HTML injection):
go to https://12test.imgur.com (you don't need to login) and you will see external videos and you will see image click on it and you will redirect to http://evil.com,
note that this test page attacker page could be more normal to user,
remeber that it's stored so it will show up when any user viste profile

Suggested fix:
Sanitize all input fields on this page.

## Impact

attacker could redirect users and then execute xss and control them easily, also could include his videos to get views

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
