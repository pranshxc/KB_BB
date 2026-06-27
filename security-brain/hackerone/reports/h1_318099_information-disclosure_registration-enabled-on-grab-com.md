---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '318099'
original_report_id: '318099'
title: Registration enabled on ███grab.com
weakness: Information Disclosure
team_handle: grab
created_at: '2018-02-21T06:45:22.310Z'
disclosed_at: '2018-02-28T05:16:59.947Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 29
asset_identifier: '*.grab.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Registration enabled on ███grab.com

## Metadata

- HackerOne Report ID: 318099
- Weakness: Information Disclosure
- Program: grab
- Disclosed At: 2018-02-28T05:16:59.947Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
An attacker can register an account on the `█████████grab.com` service, and access information from the service


**Description:** 
While logging in via Google accounts is prohibited, an attacker can register an account through the `/login/create` endpoint, as per the below request
```
POST /login/create HTTP/1.1
Host: █████grab.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://███grab.com/
Authorization: Bearer null
Content-Type: application/json
Content-Length: 61
Cookie: G_ENABLED_IDPS=google; G_AUTHUSER_H=0
Connection: close

{"userid":"█████","password":"██████"}
```


This can then be used to log in via the `/login` endpoint ,as in the following request:
```
POST /login HTTP/1.1
Host: █████grab.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://█████grab.com/
Authorization: Bearer null
Content-Type: application/json
Content-Length: 61
Cookie: G_ENABLED_IDPS=google; G_AUTHUSER_H=0
Connection: close

{"userid":"██████","password":"████"}
```
which returns a valid token. F265433

This token can be used to access some of the endpoints, such as
`/api/find/users`, as in the following request: F265434

## Impact

An attacker can access information in the system such as registered users. The application appears to be newly developed, and as such little information is stored currently.

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
