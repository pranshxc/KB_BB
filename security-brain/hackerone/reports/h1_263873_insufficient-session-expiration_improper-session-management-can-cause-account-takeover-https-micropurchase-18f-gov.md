---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '263873'
original_report_id: '263873'
title: Improper Session management can cause account takeover[https://micropurchase.18f.gov]
weakness: Insufficient Session Expiration
team_handle: gsa_bbp
created_at: '2017-08-28T00:59:34.431Z'
disclosed_at: '2019-07-30T15:18:29.700Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 33
tags:
- hackerone
- insufficient-session-expiration
---

# Improper Session management can cause account takeover[https://micropurchase.18f.gov]

## Metadata

- HackerOne Report ID: 263873
- Weakness: Insufficient Session Expiration
- Program: gsa_bbp
- Disclosed At: 2019-07-30T15:18:29.700Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I would like to report a vulnerability on https://micropurchase.18f.gov where I am able to reuse session cookie of a test user account i accessed through Github.
The problem is that the cookies stored on the browser are not getting expired after logging out from the platform and from Github as well.

Steps to Reproduce:
1. visit https://micropurchase.18f.gov
2. click on sign in through Github
3. Once you are logged in Then Use "BurpSuite" or any other Utility to get the cookies of that session (  "EditThisCookie" Chrome Extension can be used and in a Case of an  Attacker he can Use Any Sort Of cookie Stealing Script or Cookies Spoofing Utility to get his hands on cookies ) and grab the cookies of active User Session.
4.Then Logout of the Account from https://micropurchase.18f.gov .
5. Clear all Cookies related to https://micropurchase.18f.gov using [cookies manager+ extension]Then Inject Hijacked User Cookies so that you can get into the user session...
6. After the cookies been injected You will See That the main page showing account and logout parameters on the front end.

Attack Scenario :--  If The Attacker Got his Hands Upon Users Cookies he can Get Access To the User Account.An attacker can get the user session cookies by any means Session Spoofer, Cookie Stealer etc.As the user cookies are not expiring so an attacker can directly inject the stolen cookies of a victim in a request from browser and thus can have access to the victims account.

So expire the cookies once a user is logged out of the website.
POC:- I am providing a video poc :- https://youtu.be/uLFJUJ3CnQQ , its unlisted video.

Regards
sahil tikoo

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
