---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '10829'
original_report_id: '10829'
title: CSRF in function "Set as primary" on  accounts page
weakness: Cross-Site Request Forgery (CSRF)
team_handle: coinbase
created_at: '2014-05-03T19:46:07.517Z'
disclosed_at: '2014-06-06T04:56:45.797Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF in function "Set as primary" on  accounts page

## Metadata

- HackerOne Report ID: 10829
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: coinbase
- Disclosed At: 2014-06-06T04:56:45.797Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I would like to report this CSRF vulnerability in coinbase on function "set as primary" for a account in accounts page. 

Steps:
1) Login to your coinbase account (which atleast has two accounts)
2) Go to "accounts" page and out of the two accounts click "set as primary" link for one of the accounts which is not primary.
3) Capturing the request in proxy, you will find that there are no anti CSRF token used for this function. 

Issue: Attacker simply send a link of a page to the victim with a iframe running something like this "https://coinbase.com/accounts/535e52d301c95bda2100005b/set_as_primary". When the victim will click the link of coinbase will get executed in the back without victims consent. 

NOTE: In the POC video attached, i have tried to show that for the delete account function there is an "authenticity token" sent but for set as primary function there is no token used, which might cause a CSRF on this.

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
