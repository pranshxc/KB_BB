---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6504'
original_report_id: '6504'
title: Session Fixation Found
team_handle: reddapi
created_at: '2014-04-08T12:53:23.015Z'
disclosed_at: '2014-04-20T14:29:30.957Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
---

# Session Fixation Found

## Metadata

- HackerOne Report ID: 6504
- Weakness: 
- Program: reddapi
- Disclosed At: 2014-04-20T14:29:30.957Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello reddapi,
iam saikiran a security researecher found a bug in your website...

Authot- Sai Kiran
bug-session fixation
Severity: Medium

Summary:

The application does not set a new Session ID in the cookie after what appears to be an authentication attempt by the user. If this was a successful login and the Session IDs are stored in cookies then this application is affected by Session Fixation vulnerability.

To reproduce this vulnerability

1.open chrome and download edit this cookie ad-don
2.now open https://www.reddapi.com/ and log in 
3.now goto edit this cookie addon and click export all cookies ...by clicking this we get the cookie copied in clipboard..
4.logout from your https://www.reddapi.com/ account...
5.if needed u can close and open your browser.
6.now again go to https://www.reddapi.com/ but dont login..just simply go to edit this cookie addon and click import a cookie and paste the code which we previously exported.
7.after pasting just refresh the page and thats done you are now logged into your account without login details...

problems faced

the problems face if the vulnerability exits are
1.anyone can easily hijack victims or users session and get into his account
2.cookie stealing is the best way the hacker can get into and account..it would not take more than 5min to steal someones cookie using php n all...
3.even friends can fool the victim and get him hacked..

Solution

Manage session properly.this problem is mainly faced because the session doesn't get expired or doesn't get closed when logout is pressed.each time the user logins the cookie must hold a unique different session id to proceed..

facebook,google,any many more sites overtook this site....

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
