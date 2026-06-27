---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15476'
original_report_id: '15476'
title: Session Token is not Verified while changing Account Setting's which Result
  In account Takeover
weakness: Cross-Site Request Forgery (CSRF)
team_handle: fanfootage
created_at: '2014-06-07T13:28:21.694Z'
disclosed_at: '2014-06-14T17:44:38.421Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Session Token is not Verified while changing Account Setting's which Result In account Takeover

## Metadata

- HackerOne Report ID: 15476
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: fanfootage
- Disclosed At: 2014-06-14T17:44:38.421Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Dear Team,

Step-by-step instructions on how to reproduce the problem:

It was found the application is vulnerable to CSRF attack.
To achieve the same,

Session Token is not Verified while changing Account Setting's which Result In account Takeover

Description:-

I have found that while changing Setting Session token is not verified .So an attacker can basically plot a CSRF attack which would change the default email of the user and this would led to account takeover.

POC:-

I have made proof of concept video of the same:-https://www.youtube.com/watch?v=oCpAu18ULQQ
The Above Video is Unlisted.

Regard :-
Shubham Gupta

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
