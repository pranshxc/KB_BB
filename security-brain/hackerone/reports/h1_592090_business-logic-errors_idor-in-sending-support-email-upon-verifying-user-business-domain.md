---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '592090'
original_report_id: '592090'
title: IDOR in sending support email upon Verifying user business domain
weakness: Business Logic Errors
team_handle: trustpilot
created_at: '2019-05-29T06:19:09.200Z'
disclosed_at: '2019-08-21T08:17:12.032Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 43
asset_identifier: '*api.trustpilot.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# IDOR in sending support email upon Verifying user business domain

## Metadata

- HackerOne Report ID: 592090
- Weakness: Business Logic Errors
- Program: trustpilot
- Disclosed At: 2019-08-21T08:17:12.032Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary**
Trustpilot Business is making sure that you own the domain you have registered before continuing the process so they set 5 choices on how to verify. But there's another one, which is through sending a support ticket. By this you can send message to a support and hope to help you out.

There is a bit problem in this process. 1.) The `email` parameter is letting you to send email to another user, which don't own. 2.) The `phoneNumber` parameter is controllable. You can add text upto 94 characters enough to fool a user.

**How to reproduce**
First you need to register a valid account. If you don't own a domain it's Ok. There's a way to bypass the check. Just intercept the post request on `https://api.trustpilot.com/v1/business-requests/signup?utm_source=sign_up_link&utm_medium=business_login_page&utm_campaign=login` and modify the `email` parameter to your preferred email. Once set, check your email and click the verify.

If you've follow above step, you will be redirected to `https://businessapp.b2b.trustpilot.com/#/claim/` and here's where the magic happens. On the bottom there's a link called `Fill out this form`. Fill up the form and intercept the request. The request looks like this:
```
POST /v1/private/business-users/5cee035f00bf83001b207d67/activation/support HTTP/1.1
Host: api.trustpilot.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://businessapp.b2b.trustpilot.com/
Content-Type: application/json;charset=utf-8
Authorization: Bearer [reducted]
ApiKey: [reducted]
Content-Length: 182
Origin: https://businessapp.b2b.trustpilot.com
Connection: close

{"name":"test","email":"[reducted]","domain":"","phoneNumber":". Please follow this link to verify https://e-corp.ord","message":"test. pls ignore","locale":"en-US"}
```

Final step is to modify the `email` and `phoneNumber` parameter. This is will send an email you a target user and let you add a malicious link in the email.



POC: F498456

## Impact

IDOR which leads a phishing email to target any users

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
