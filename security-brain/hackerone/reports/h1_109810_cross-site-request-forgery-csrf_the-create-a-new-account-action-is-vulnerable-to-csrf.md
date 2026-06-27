---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '109810'
original_report_id: '109810'
title: The 'Create a New Account' action is vulnerable to CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: coinbase
created_at: '2016-01-10T21:00:17.524Z'
disclosed_at: '2016-07-24T03:40:39.513Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# The 'Create a New Account' action is vulnerable to CSRF

## Metadata

- HackerOne Report ID: 109810
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: coinbase
- Disclosed At: 2016-07-24T03:40:39.513Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

The request to create an account wallet doesn't validate if the request is originating from the user itself with the help of an anti-CSRF token. 

Step 1: Craft an HTML page with request to create a wallet in your accounts page. 
https://www.coinbase.com/accounts > New Account > Wallet

Step 2: Open the HTML page in a tab of the browser where a user is already logged in to coinbase. It can be observed that a wallet is created.

PS: In some browsers this may not work. It should be noted that it is not because the application doesn't have a proper CSRF mitigation mechanism, rather the parameter utf8 is improperly rendered.

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
