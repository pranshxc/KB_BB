---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '226648'
original_report_id: '226648'
title: Unauthorized access to the slack channel via inside.gratipay.com/appendices/chat
weakness: Improper Authentication - Generic
team_handle: gratipay
created_at: '2017-05-06T22:47:32.498Z'
disclosed_at: '2017-05-09T13:41:58.518Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# Unauthorized access to the slack channel via inside.gratipay.com/appendices/chat

## Metadata

- HackerOne Report ID: 226648
- Weakness: Improper Authentication - Generic
- Program: gratipay
- Disclosed At: 2017-05-09T13:41:58.518Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

# Summary
It is possible to force send invites for gratipay slack channel to arbitary email ids with no bruteforce limit. This is done by modifying the `coc` parameter to `1` in the POST data sent from https://inside.gratipay.com/appendices/chat

# Description
Sending a post request with `coc` parameter set to `1` appears to be bypassing some validation that is being done in the server. Without the same, the server responds with `Woot. Check your email` to the requests. 

**Request**
```
POST /invite HTTP/1.1
Host: gratipay-slackin.herokuapp.com
Content-Type: application/json
Content-Length: 36

{"coc":1,"email":"dobum@alienware13.com"}
```

**Response**
```
HTTP/1.1 400 Bad Request
Server: Cowboy
Connection: keep-alive
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 93
Date: Sat, 06 May 2017 22:33:39 GMT
Via: 1.1 vegur

{"msg":"You have already been invited to Slack. Check for an email from feedback@slack.com."}
```

Even though the response is a `400 Bad Request`, an invite email is received from `"Slack" <feedback@slack.com>` with the subject `Paul Kuruvilla has invited you to join a Slack team`.
Whatever the validation may be, this allows invites to be forced sent to arbitary email ids with no brute force limit.

# Steps To Reproduce
 * Send the post data with an arbitary email id
 * An invite to the gratipay slack channel `gratipay.slack.com` will be received at that email account 

# Supporting References:
  * https://gratipay.slack.com/team/dobum

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
