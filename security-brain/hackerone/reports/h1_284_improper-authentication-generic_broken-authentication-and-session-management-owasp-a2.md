---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '284'
original_report_id: '284'
title: Broken Authentication and session management OWASP A2
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2013-11-07T13:27:06.643Z'
disclosed_at: '2014-01-09T14:36:45.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
tags:
- hackerone
- improper-authentication-generic
---

# Broken Authentication and session management OWASP A2

## Metadata

- HackerOne Report ID: 284
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2014-01-09T14:36:45.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description:
Session management issue in https://www.hackerone.com

Cookies are used to maintain session of the particular user and they should expire once the user logs out of his hackerone account.In secure web application,Cookies immediately expire once the user logs out of his account.

But this is not happening in the case of hackerone same cookies can be used again and again  to open the session of the victim.
Extensions required and Browser Version:
Google chrome
Version 26.0.1410.64 m

Edit this cookie extension

Steps to reproduce the issue:
=======================
1) Create a Hackerone account and log in into the newly created account or you can use your existing account as well.
2) Copy the cookies using Edit this cookie extension when you are logged in using "Import Cookies" option of the extension.
3) Now log out from your Hackerone account and save the cookies in the Notepad file.
4) After 6 hrs or 8 hrs copy the same cookies in your Chrome using the same extension and you will be logged into your account.The cookies are not getting expired once the user logs out of his account.

Benefits :)

Suppose if a XSS vulnerability is exploited in the web application (there is not any )  the hacker can use same cookies again and again to open the session of the victim but what if there are new cookies when the victim logs out from his account on the other end the hacker session also expires.

Please have a look,
Looking forward to hear from you.
Best Regards,
Anand Prakash 
https://www.twitter.com/sehacure

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
