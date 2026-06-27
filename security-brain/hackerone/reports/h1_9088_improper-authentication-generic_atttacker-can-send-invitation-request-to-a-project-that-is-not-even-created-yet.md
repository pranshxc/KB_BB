---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9088'
original_report_id: '9088'
title: Atttacker can send "Invitation Request" to a Project that is not even created
  yet!
weakness: Improper Authentication - Generic
team_handle: localize
created_at: '2014-04-22T14:20:27.581Z'
disclosed_at: '2014-04-23T04:58:59.487Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Atttacker can send "Invitation Request" to a Project that is not even created yet!

## Metadata

- HackerOne Report ID: 9088
- Weakness: Improper Authentication - Generic
- Program: localize
- Disclosed At: 2014-04-23T04:58:59.487Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hei,
How you doing ?

just found another bug on **Invitation Process**.
This one is really interesting!

With this bug, Attacker can send **invitation request** to a project that is even not created yet :p

POC
------

Process is same as other two issues that i reported earlier,
* Just send an **Invitation Request" to a private Project and use the POST Data to reproduce (with Live HTTP Header or any other Request Repeater).

POST : https://www.localize.im/projects/[Project ID]
>
Host: www.localize.im
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Referer: https://www.localize.im/projects/[ID]
Cookie: PHPSESSID=hp7c6gvbb93nu4o29tim85s3o5
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 95

> CSRFToken=[TOKEN]&requestInvitation[repositoryID]=[ID]

Here, suppose ID of last Project created on Localize is `9a` , now as localize application normally works, next ID will be `9b` .. (i can be wrong here)
with Live HTTP Header, You can Send Requests to project that is not even created till now.. all you have to do is just change the ID parameter to `9b` `9c` `9d` `9e` `9f` more and more and send request.
Now when Project with ID `9b` `9c` `9d` `9e` `9f` will get created, doesn't matter this project is `PUBLIC` or `PRIVATE` (because of that bug i reported earlier), there will be an "Invitation Request" awaiting for confirmation.

Hope you will fix this one soon as possible..

Regards and Best Wishes,
FaisaL Ahmed

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
