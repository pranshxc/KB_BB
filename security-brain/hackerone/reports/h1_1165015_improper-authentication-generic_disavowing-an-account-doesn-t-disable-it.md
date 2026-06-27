---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1165015'
original_report_id: '1165015'
title: Disavowing an account doesn't disable it
weakness: Improper Authentication - Generic
team_handle: liberapay
created_at: '2021-04-14T14:03:39.309Z'
disclosed_at: '2021-05-07T07:43:28.971Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Disavowing an account doesn't disable it

## Metadata

- HackerOne Report ID: 1165015
- Weakness: Improper Authentication - Generic
- Program: liberapay
- Disclosed At: 2021-05-07T07:43:28.971Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello security team, while I testing your website, I found improper email verification while sign-up 
liberapay.com. 

Steps to reproduce:
1) Go to https://liberapay.com.
2) Create new account with any email.
3) You will receive  an email verification to the given email.
4) Open that email and click "No, it wasn't me". There will be a message "You have successfully disavowed having connected your email address to this Liberapay account.".
5) Now come to the liberapay.com in browser and reload the page. (It should not allow the user to continue with that account)

But you can see, there is no changes with the site and you can continue with that account.

## Impact

Attacker can create an account with anyone's email without verifying.

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
