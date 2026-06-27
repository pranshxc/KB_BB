---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159526'
original_report_id: '159526'
title: Information leakage of private program
weakness: Information Disclosure
team_handle: security
created_at: '2016-08-15T18:57:30.206Z'
disclosed_at: '2016-08-18T11:36:10.436Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
tags:
- hackerone
- information-disclosure
---

# Information leakage of private program

## Metadata

- HackerOne Report ID: 159526
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2016-08-18T11:36:10.436Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello team,
I noticed an issue in `Directory` where information of a soft-launched program getting disclosed!

I made this request as an unauthecated user,
```http
GET /programs/search?query█████████&sort=published_at%3Adescending&page=1 HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-GB,bn;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
X-CSRF-Token: <redacted>
X-Requested-With: XMLHttpRequest
Referer: https://hackerone.com/directory?query█████████
Cookie: <redacted>
Connection: close
```

and partial response was,
```
{"id":1913,"url":"/██████████","name":"████","meta":{"bug_count":5,"minimum_bounty":100,"soft_launched":true},"about":"","handle":"██████████","profile_picture":"https://profile-photos.hackerone-user-content.com/production/████████","internet_bug_bounty":false}
```
███████

This issue also disclose the **Policy** of that program!
I've attached the policy as text.

####Reproducible Steps:
* Navigate to **[Directory](https://hackerone.com/directory)**
* Search ████
* Result will be,
█████████

You won't see the bug count, policy and base bounty on result. but if you capture the request on BURP response, you'll be able to harvest these information from there! 

Looking forward!

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
