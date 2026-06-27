---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '362601'
original_report_id: '362601'
title: A single user can subscribe a community multiple times
weakness: Business Logic Errors
team_handle: liberapay
created_at: '2018-06-06T02:16:48.591Z'
disclosed_at: '2018-06-07T20:15:19.109Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# A single user can subscribe a community multiple times

## Metadata

- HackerOne Report ID: 362601
- Weakness: Business Logic Errors
- Program: liberapay
- Disclosed At: 2018-06-07T20:15:19.109Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

There is no proper validation while subscribing for a community. A user can subscribe a single community multiple times.

Steps to recreate:
Step 1: Open any community
Step 2: Click on subscribe button
Step 3: Capture the POST request and submit it multiple times
Step 4: Check the subscription count

POST Request:
--------------------------------
POST /for/nocommunity/subscribe HTTP/1.1
Host: liberapay.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://liberapay.com/for/nocommunity
Cookie: __cfduid=d5a7372c0620f73d866bac0869443206a1528250205; csrf_token=hmxFrGGb7FULfeeMuDIIamnotahacker; session="163767:1:VTi89XOnmnZWYLXMBlE8G_a_8gZCZAz5"
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 43

csrf_token=hmxFrGGb7FULfeeMuDIIamnotahacker

Response:
--------------------
HTTP/1.1 302 Found
Date: Wed, 06 Jun 2018 02:11:26 GMT
Connection: close
[TRUNCATED]

## Impact

Any user can increase his/her community subscriber's count to any number.

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
