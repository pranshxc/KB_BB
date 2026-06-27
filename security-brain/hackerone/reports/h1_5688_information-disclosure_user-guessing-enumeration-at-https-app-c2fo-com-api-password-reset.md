---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '5688'
original_report_id: '5688'
title: User guessing/enumeration at  https://app.c2fo.com/api/password-reset
weakness: Information Disclosure
team_handle: c2fo
created_at: '2014-04-02T21:25:51.623Z'
disclosed_at: '2014-05-19T12:03:17.921Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# User guessing/enumeration at  https://app.c2fo.com/api/password-reset

## Metadata

- HackerOne Report ID: 5688
- Weakness: Information Disclosure
- Program: c2fo
- Disclosed At: 2014-05-19T12:03:17.921Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there,

I noticed a small information leak which allows an attacker to check whether an email address is associated with an account. 

###Steps to reproduce:

1.  Send a POST-Request to the url https://app.c2fo.com/api/password-reset as the following example shows:

```
POST /api/password-reset HTTP/1.1
Host: app.c2fo.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 37

emailAddress=test%40internetwache.org
```

2. I registered an account with the email address, thus the server will respond with ```{"inReset":true}```, which means that the address is in use.

3. Now resend the request again, but with an invalid address like "foobar123@internetwache.org". The application will tell use the following: ```{"error":"invalid_email_address"}```. 

This way I can validate email addresses against your service.

###Suggested fix: 
You should always return a status message like: "If your email exists in our database, you'll receive a reset link". That way an attacker cannot distinguish between the two cases.

Thanks,
Sebastian

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
