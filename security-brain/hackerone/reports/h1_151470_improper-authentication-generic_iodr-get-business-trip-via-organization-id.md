---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '151470'
original_report_id: '151470'
title: '[IODR] Get business trip via organization id'
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2016-07-15T08:44:23.434Z'
disclosed_at: '2016-08-15T20:21:09.014Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- improper-authentication-generic
---

# [IODR] Get business trip via organization id

## Metadata

- HackerOne Report ID: 151470
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2016-08-15T20:21:09.014Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Uber,
I found issue on https://business.uber.com/server/organizations/[id]/trips2?per_page=15&requestAtStart=&requestAtStop=&count=true

Step to reproduce:
1. Get https://business.uber.com/server/organizations/[your_organization_id]/trips2?per_page=15&requestAtStart=&requestAtStop=&count=true
2. Chang to victim organization If valid id, it will return result, but if not it will show error with internal state 

```
{"error":{"name":"TchannelUnexpectedError","fullType":"tchannel.unexpected","type":"tchannel.unexpected","message":"Unexpected Error: 'validation_error.must_be_a_valid_uuid_v4'","isErrorFrame":true,"codeName":"UnexpectedError","errorCode":5,"originalId":2,"remoteAddr":"10.160.14.41:21306"}}
```
In `employee_invites`, it return 403.
As previous I report #151465 , I can get organization id or just enum it ( very difficult).

Best regards,
Severus

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
