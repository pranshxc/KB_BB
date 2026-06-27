---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '158434'
original_report_id: '158434'
title: (BYPASS) Open redirect and XSS in supporthiring.shopify.com
weakness: Cross-Site Request Forgery (CSRF)
team_handle: shopify
created_at: '2016-08-11T11:28:42.427Z'
disclosed_at: '2016-11-21T13:24:43.798Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 36
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# (BYPASS) Open redirect and XSS in supporthiring.shopify.com

## Metadata

- HackerOne Report ID: 158434
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: shopify
- Disclosed At: 2016-11-21T13:24:43.798Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

The users can be redirected to some other site which is in control of the attacker from 

Vulnerable parameter: path=

You have a protection here at path= but it bypass the parameter if you add a double slash, like %2F%2F.

Let's say user is attacker asked victim to came to this page: :
http://supporthiring.shopify.com/apps/locksmith/resource/pages/gauntlet-challenge?&path=%2F%2Fevil.com

Victim will be see a 404 error page and after 2 seconds he will be redirected to: https://evil.com

These can be controlled by the attacker and used in other attacks

Works in all browsers!!

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
