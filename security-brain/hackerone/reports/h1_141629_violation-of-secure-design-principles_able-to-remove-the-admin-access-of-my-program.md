---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '141629'
original_report_id: '141629'
title: Able to remove the admin access of my program
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2016-05-28T06:11:41.112Z'
disclosed_at: '2016-07-06T12:49:10.426Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- violation-of-secure-design-principles
---

# Able to remove the admin access of my program

## Metadata

- HackerOne Report ID: 141629
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-07-06T12:49:10.426Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey Jobert,


There is a functional bug in hackerone, using which i am able to make the my program admin free.
This shouldn't be happen in the program because atleast one admin be there in program.

Request:
PUT /sasas/groups/12307 HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Referer: https://hackerone.com/sasas/groups/12307/members/edit
Content-Length: 157
Cookie: 
Connection: close

{"id":12307,"name":"Admin","team_members_count":2,"permissions":["user_management","program_management"],"immutable":true,"team_member_ids":[{"id":"17940"}]}


Thanks & Regards,
Pardeep Battu

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
