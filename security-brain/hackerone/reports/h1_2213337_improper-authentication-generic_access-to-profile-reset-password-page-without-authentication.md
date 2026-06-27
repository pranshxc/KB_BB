---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2213337'
original_report_id: '2213337'
title: access to profile & reset password page without authentication
weakness: Improper Authentication - Generic
team_handle: tennessee-valley-authority
created_at: '2023-10-17T16:41:29.309Z'
disclosed_at: '2023-11-30T15:46:17.739Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 62
asset_identifier: '*.tva.gov'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# access to profile & reset password page without authentication

## Metadata

- HackerOne Report ID: 2213337
- Weakness: Improper Authentication - Generic
- Program: tennessee-valley-authority
- Disclosed At: 2023-11-30T15:46:17.739Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
Hi team,
when i checking https://valleyconnect.tva.gov i see we are login! and in top of page see : Hello, null. and we can access to some internal page like  Reset Password.
                       

## Steps To Reproduce:
1. go to https://valleyconnect.tva.gov
2. click on [reset passwod menu](https://valleyconnect.tva.gov/password-rules)

## Tips
by default we are login in portal and we can get status code 200 from below  Api :
```
GET /customapi/v1/user/getbasicprofileinfo HTTP/2
Host: valleyconnect.tva.gov
```

response is :
```
HTTP/2 200 OK
Content-Type: application/json; charset=utf-8

"{\"username\":null,\"email\":null,\"orgId\":null,\"hasRemoteAssistanceGrant\":false}"
```
we can access to favorites too:
```
GET /customapi/v1/user/getuserfavorites 
```

response is :
```
HTTP/2 200 OK
Date: Tue, 17 Oct 2023 14:45:02 GMT

""
```

## Supporting Material/References:

  * {F2780981}
  * {F2780983}

## Impact

Improper Authentication leads to access to internal page like reset password and profile page.

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
