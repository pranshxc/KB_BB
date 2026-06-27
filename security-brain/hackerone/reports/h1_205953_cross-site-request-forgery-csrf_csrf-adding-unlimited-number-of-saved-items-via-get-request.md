---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '205953'
original_report_id: '205953'
title: CSRF - Adding unlimited number of saved items via GET request
weakness: Cross-Site Request Forgery (CSRF)
team_handle: lyst
created_at: '2017-02-13T12:05:55.609Z'
disclosed_at: '2017-09-28T07:23:06.764Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF - Adding unlimited number of saved items via GET request

## Metadata

- HackerOne Report ID: 205953
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: lyst
- Disclosed At: 2017-09-28T07:23:06.764Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello, I have found a way of potentially adding thousands of items to the saved items list by using a GET request.

POC
-----------
```
GET /email-capture/stock-alert/93543518/?return_url=/email-capture/stock-alert/91703404/?return_url=/email-capture/stock-alert/89201857/ HTTP/1.1
Host: www.lyst.com
```

By adding a stock alert notification to an item, the respective item is automatically added in the saved list and because this is a GET request, there is no CSRF token/protection here.

IMPACT
-------
Because this is done via GET request it is very easy to add thousands of products in the target user account by making one or both of these:
1. Chain your internal redirect requests (shown in POC)
2. Simply embed 1000x 1px image that with the target link (of course different product id per image)

Because of the extreme volume of the added items, the attacker can make the target's save list simply unusable (he must then delete 1000 entries and NO ONE will do that). I think a lot of people are taking advantage of the list, so a CSRF here can have a pretty big/annoying impact and you could loose clients.

Video POC attached.

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
