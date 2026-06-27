---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '513137'
original_report_id: '513137'
title: Request vulnerable to CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: phabricator
created_at: '2019-03-21T12:33:42.910Z'
disclosed_at: '2019-03-22T13:21:49.561Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 5
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Request vulnerable to CSRF

## Metadata

- HackerOne Report ID: 513137
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: phabricator
- Disclosed At: 2019-03-22T13:21:49.561Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

There are 4 instances of this issue:
[+] /dashboard/panel/render/12/
[+] /dashboard/panel/render/22/
[+] /dashboard/panel/render/4/
[+] /dashboard/panel/render/6/

Issue background ==>
Cross-site Request Forgery (CSRF) is an attack which forces an end user to execute unwanted actions on a web application to which he/she is currently authenticated. With a little help of social engineering (like sending a link via email / chat), an attacker may trick the users of a web application into executing actions of the attacker's choosing. A successful CSRF exploit can compromise end user data and may allow an attacker to perform an account hijack. If the targeted end user is the administrator account, this can compromise the entire web application.

Issue remediation ==>
The application should implement anti-CSRF tokens into all requests that perform actions which change the application state or which add/modify/delete content. An anti-CSRF token should be a long randomly generated value unique to each user so that attackers cannot easily brute-force it.

It is important that anti-CSRF tokens are validated when user requests are handled by the application. The application should both verify that the token exists in the request, and also check that it matches the user's current token. If either of these checks fails, the application should reject the request.

## Impact

Cross-site Request Forgery (CSRF) is an attack which forces an end user to execute unwanted actions on a web application to which he/she is currently authenticated. With a little help of social engineering (like sending a link via email / chat), an attacker may trick the users of a web application into executing actions of the attacker's choosing. A successful CSRF exploit can compromise end user data and may allow an attacker to perform an account hijack. If the targeted end user is the administrator account, this can compromise the entire web application.

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
