---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1172205'
original_report_id: '1172205'
title: Insufficient session expiration in the **com.shopify.ping** android app
weakness: Insufficient Session Expiration
team_handle: shopify
created_at: '2021-04-22T13:18:10.413Z'
disclosed_at: '2021-11-26T06:02:18.709Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 60
asset_identifier: Shopify Mobile Applications
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- insufficient-session-expiration
---

# Insufficient session expiration in the **com.shopify.ping** android app

## Metadata

- HackerOne Report ID: 1172205
- Weakness: Insufficient Session Expiration
- Program: shopify
- Disclosed At: 2021-11-26T06:02:18.709Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It was identified that despite a logout action will be taken by the user at the com.shopify.ping application, the authentication token is not invalidated which allows fully recovery of the initially acquired session. More specifically, after the user provides the required credentials, an **access_token** will be fetched from the server at accounts.shopify.com/oauth/token. After establishing a session and by selecting logout from the corresponding control, the application will send the following DELETE request:

```
DELETE /api/v1/logout HTTP/1.1
authorization: Bearer atkn_**********************************
Host: accounts.shopify.com
Connection: close
Cookie: __cfduid=***********; _y=***************; _shopify_y=***************; request_method=POST
User-Agent: okhttp/3.12.12
```

The server will reply as follows:

```
{"error":"Missing Logout Token Hint"}
```
And will cancel the invalidation process, as the token will still be valid on a subsequent request (e.g.):

```
GET /oauth/userinfo HTTP/1.1
Accept-Encoding: gzip, deflate
authorization: Bearer ***************
....
```
REPLY:
```
{"sub":"...","email":".....@gmail.com","email_verified":true,"family_name":"Doe","given_name":"....","locale":"en","name":".... ...","nickname":".....","updated_at":.....,"zoneinfo":"....","tfa_enabled":false}
```

## Impact

An application should always revoke an access token by the time that the end user choses to Log Off from a session. Keeping a token active, while the user is not aware of it imposes a big risk, since by the time that an unauthorised entity fetches it, may recover a fully "functional" session.

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
