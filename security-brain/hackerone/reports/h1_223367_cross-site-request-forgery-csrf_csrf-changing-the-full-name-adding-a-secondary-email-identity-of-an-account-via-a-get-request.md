---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223367'
original_report_id: '223367'
title: CSRF - Changing the full name / adding a secondary email identity of an account
  via a GET request
weakness: Cross-Site Request Forgery (CSRF)
team_handle: weblate
created_at: '2017-04-24T10:33:08.048Z'
disclosed_at: '2017-06-02T19:08:34.670Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF - Changing the full name / adding a secondary email identity of an account via a GET request

## Metadata

- HackerOne Report ID: 223367
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: weblate
- Disclosed At: 2017-06-02T19:08:34.670Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

SUMMARY
----------
Hello, I have found a CSRF request via the activation email that will change the full name of the targeted account. This vulnerability exists if the attacker registers a new account and then gives his activation link to someone else. If the victim uses the received activation link while he is logged in his account the attacker's email will be added as a secondary email and the main full name will be changed.

POC
-------
I have attached the POC as a video where you can see all the steps.

IMPACT
------
Medium - high impact IMO. Changing the name may not be such a big deal, but adding a secondary email identity may turn into something more dangerous.

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
