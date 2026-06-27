---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '143321'
original_report_id: '143321'
title: Unauthenticated CSRF(User can input any value for CSRF Token)
weakness: Cross-Site Request Forgery (CSRF)
team_handle: veris
created_at: '2016-06-06T14:47:17.584Z'
disclosed_at: '2016-06-08T12:43:59.446Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Unauthenticated CSRF(User can input any value for CSRF Token)

## Metadata

- HackerOne Report ID: 143321
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: veris
- Disclosed At: 2016-06-08T12:43:59.446Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Veris,
I believe you have implemented `CSRF token` on the registration for a reason. In my research, I found that a user supplied CSRF Token would be accepted and even saved in the browser cookie and will be the set token on subsequent request. This report is limited to the `Register` and `Login` page anyway.
And most importantly, there is no verification of the `CSRF token` on the `server side` because if there is, the request shouldn't go through to talk of being saved in the browser cookie. The only verification I can see is if the inserted token is more than set 32 characters.

PoC:
- Navigate to https://sandbox.veris.in/portal/register/
- Fill the form and the captcha as required
- Using a proxy tool, intercept the request (I'm using Burp Proxy)
- Change the value of `csrftoken` in cookie field
- Copy the same input and paste in `csrfmiddlewaretoken`
- Forward the request
- You'll get a 200 OK response
i.e Request made successfull
- In the next request, change the value of `csrftoken` to the one used recently. 
- You could now check the value of cookie in the browser. 
- Bam! You found it.

I can provide a video proof if needed. I hope you understand

Thanks
Shuaib Oladigbolu

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
