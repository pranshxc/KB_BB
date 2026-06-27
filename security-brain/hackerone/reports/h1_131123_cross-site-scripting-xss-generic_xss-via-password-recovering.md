---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '131123'
original_report_id: '131123'
title: XSS via password recovering
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-04-15T15:27:55.012Z'
disclosed_at: '2016-07-26T00:34:42.868Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS via password recovering

## Metadata

- HackerOne Report ID: 131123
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-07-26T00:34:42.868Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

I found that xss can be executed if we provide xss payload as a password in Uber during password recovery.

Steps to follow:

1) Goto https://login.uber.com/forgot-password
2) Enter email and submit
3) Open the recover link you got
4) Enter Set password: <script>alert(document.domain);</script> and submit it
5) Click Show password

 XSS Executed.

Video and screenshot added

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
