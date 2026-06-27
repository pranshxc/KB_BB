---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '140432'
original_report_id: '140432'
title: configure a redirect URI for Facebook OAuth
weakness: Improper Authentication - Generic
team_handle: gratipay
created_at: '2016-05-23T08:09:16.903Z'
disclosed_at: '2016-06-17T06:42:09.412Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- improper-authentication-generic
---

# configure a redirect URI for Facebook OAuth

## Metadata

- HackerOne Report ID: 140432
- Weakness: Improper Authentication - Generic
- Program: gratipay
- Disclosed At: 2016-06-17T06:42:09.412Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey,

Its me again. since the Login with Facebook doesnt have a dedicated directory like gratipay.com/facebook/callback it is possible to still steal access tokens.

https://www.facebook.com/dialog/oauth?response_type=code&client_id=144124902390407&redirect_uri=https://gratipay.com/~attacka/&scope=public_profile%2Cemail%2Cuser_friends&state=mjemgKNb0s24lbEqBcyVqDEVNoYDYs

As you can see it will send the token to my profile (/~attacka) and my profile points to example.com, if the user clicks on that link the referrer header will send tokenz (obviously lol)

gratipay also imports pictures from 3rd parties, forexample my img src is from ls.googleusercontent.com which means it will also leak the access_tokens to there.

Fix: add the redirect uri like: https://www.gratipay.com/facebook/callback so users have no way to tamper with it.

Thanks,
P

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
