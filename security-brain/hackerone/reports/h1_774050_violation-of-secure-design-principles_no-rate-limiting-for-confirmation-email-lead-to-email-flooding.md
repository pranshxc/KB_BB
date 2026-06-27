---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '774050'
original_report_id: '774050'
title: No rate limiting for confirmation email lead to email flooding
weakness: Violation of Secure Design Principles
team_handle: yelp
created_at: '2020-01-14T01:07:21.554Z'
disclosed_at: '2020-02-11T23:06:34.377Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- violation-of-secure-design-principles
---

# No rate limiting for confirmation email lead to email flooding

## Metadata

- HackerOne Report ID: 774050
- Weakness: Violation of Secure Design Principles
- Program: yelp
- Disclosed At: 2020-02-11T23:06:34.377Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Description: 
There is no rate limiting implemented in sending the confirmation email. Thus, attacker can use this vulnerability to bomb out the email inbox of the victim.
### Affected URL: 
```
https://biz.yelp.com/welcome/resend_confirmation
```
with POST method
### Details:
1. Login to biz.yelp.com
2. Go to https://biz.yelp.com/messaging/xxxxxxxxxxxxxxx/inbox, it should look like this {F683815}
3. Press Re-send email then capture the request, it should like this

```
POST /welcome/resend_confirmation HTTP/1.1
Host: biz.yelp.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://biz.yelp.com/messaging/xxxxxxxxxxxxxxxxxxxxxxxxxxx/inbox
Content-Type: application/x-www-form-urlencoded
Content-Length: 129
Origin: https://biz.yelp.com
Connection: close
Cookie: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Upgrade-Insecure-Requests: 1

csrftok=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&return_url=%2Fmessaging%2Foj517fznD2Gw2v5CUUIw_Q%2Finbox
```
4. Send the captured request to Intruder and repeat the request in loop
5. Check the email, your email will be flooded by yelp confirmation email {F683818}
### How to fix:
Rate limiting should be implemented

## Impact

Email Flooding

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
