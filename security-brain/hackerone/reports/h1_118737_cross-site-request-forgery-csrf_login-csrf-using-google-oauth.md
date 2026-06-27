---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '118737'
original_report_id: '118737'
title: Login CSRF using Google OAuth
weakness: Cross-Site Request Forgery (CSRF)
team_handle: thisdata
created_at: '2016-02-25T12:13:35.037Z'
disclosed_at: '2016-03-08T04:24:08.763Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Login CSRF using Google OAuth

## Metadata

- HackerOne Report ID: 118737
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: thisdata
- Disclosed At: 2016-03-08T04:24:08.763Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

This bug is related to bug report [https://hackerone.com/reports/774] as this bug also allows a user to be logged in as the attacker. 

An attacker could exploit this bug as follows:

Attacker initiates Google OAuth process with thisdata
Attacker allows access to thisdata app
Attacker records and drops redirection to thisdata (in order not to consume token)
Attacker directs victim to /oauth/redirect?state={attacker's state}&code={attacker's code}
Victim is now logged in as attacker

state parameter is solution for this but in this case state parameter is not getting validated on server side.

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
