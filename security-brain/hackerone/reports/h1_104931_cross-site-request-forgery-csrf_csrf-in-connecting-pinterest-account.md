---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '104931'
original_report_id: '104931'
title: CSRF in Connecting Pinterest Account
weakness: Cross-Site Request Forgery (CSRF)
team_handle: shopify
created_at: '2015-12-13T12:01:43.918Z'
disclosed_at: '2016-02-02T15:23:50.884Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF in Connecting Pinterest Account

## Metadata

- HackerOne Report ID: 104931
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: shopify
- Disclosed At: 2016-02-02T15:23:50.884Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The connect to Pinterest function is vulnerable to CSRF. This allows an attacker to connect his/her pinterest account to the victim's shopify. Even if the victim has already connected a pinterest account, this will allow the attacker to replace the existing connected pinterest account with the attacker's own pinterest account.


#PoC
Note: I have also attached screenshots showing each step
1. Victim(mshop2-2) already has Pinterest account connected.
2. Attacker(mshop3-2) doesn't have Pinterest account connected and attempts to connect a Pinterest account.
3. Attacker authorize the shopify app to connect to his Pinterest account.
4. Attacker intercepts the redirection back to `pinterest-commerce.shopifyapps.com` and drop the request. Attacker also captures the URL, e.g. `https://pinterest-commerce.shopifyapps.com/auth/pinterest/callback?code=d0c18854a3359866774d479614081453d235962f`
5. Attacker induces Victim to load the above captured URL. 
6. Victim's connected Pinterest account has been replaced with the attacker's Pinterest account.

#Possible Fixes
* Make use of the state parameter in OAuth, which is used to prevent CSRF, when connecting to Pinterest.

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
