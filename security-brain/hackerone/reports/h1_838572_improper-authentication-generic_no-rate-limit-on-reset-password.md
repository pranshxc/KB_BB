---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '838572'
original_report_id: '838572'
title: No Rate Limit On Reset Password
weakness: Improper Authentication - Generic
team_handle: stagingdoteverydotorg
created_at: '2020-04-04T00:43:29.186Z'
disclosed_at: '2020-07-17T20:29:24.832Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 32
asset_identifier: staging.every.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# No Rate Limit On Reset Password

## Metadata

- HackerOne Report ID: 838572
- Weakness: Improper Authentication - Generic
- Program: stagingdoteverydotorg
- Disclosed At: 2020-07-17T20:29:24.832Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
A rate limiting algorithm is used to check if the user session (or IP address) has to be limited based on the information in the session cache. In case a client made too many requests within a given time frame, HTTP servers can respond with status code 429: Too Many Requests. (wikipedia)
I just realize that on the reset password page, the request has no rate limit which then can be used to loop through one request.

## Steps To Reproduce:

  1. Go to https://staging.every.org/resetPassword , enter the email then click reset password
  2. Intercept this request in burp suite

POST /dbconnections/change_password HTTP/1.1
Host: login.every.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0
Accept: */*
Accept-Language: id,en-US;q=0.7,en;q=0.§3§
Accept-Encoding: gzip, deflate
Content-Type: application/json
Auth0-Client: eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS4xMS4xIn0=
Content-Length: 130
Origin: https://every.org
Connection: close
Referer: https://every.org/resetPassword

{"client_id":"1bT892TGga38o0GFw5EusmGnV9b3kjCq","email":"YOUREMAILADDRESS@gmail.com","connection":"Username-Password-Authentication"}

  3. Send it to the intruder and repeat it by 50 times
  4. You will get 200 OK status
  5. I already attached the PoC video too if you don't understand my explanation

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]
https://hackerone.com/reports/751604
https://hackerone.com/reports/441161
https://hackerone.com/reports/280534

## Suggested fix
Use CAPTCHA verification if many request sent.

## Impact

Trouble to the users on the website because huge email bombing can be done by the attackers within seconds.

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
