---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6697'
original_report_id: '6697'
title: No Captcha or rate limit on Login Page
weakness: Improper Authentication - Generic
team_handle: reddapi
created_at: '2014-04-09T11:22:33.026Z'
disclosed_at: '2014-04-23T15:21:13.049Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-authentication-generic
---

# No Captcha or rate limit on Login Page

## Metadata

- HackerOne Report ID: 6697
- Weakness: Improper Authentication - Generic
- Program: reddapi
- Disclosed At: 2014-04-23T15:21:13.049Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello ReddApi Security Team,

#Vulnerability Detail's:- 
Login page can be brute forced due to lack of captcha or backoff

#Impact:- 
An attacker can bruteforce for a particular username and can get a possibly a account takeover.

#POC:-
I have made a proof of concept video of the same:- https://www.youtube.com/watch?v=zX0jXkMqiCo
The above video is unlisted.

#Countermeasure:- Implement a Captcha

With Regard's
Aditya Agrawal

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
