---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '50776'
original_report_id: '50776'
title: A user can edit comments even after video comments are disabled
weakness: Privilege Escalation
team_handle: vimeo
created_at: '2015-03-10T09:12:26.084Z'
disclosed_at: '2015-03-11T14:37:33.636Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- privilege-escalation
---

# A user can edit comments even after video comments are disabled

## Metadata

- HackerOne Report ID: 50776
- Weakness: Privilege Escalation
- Program: vimeo
- Disclosed At: 2015-03-11T14:37:33.636Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A user can escalate privileges and edit his previous comments, when comments are disabled for a video.

Steps to verify:
1. Log into vimeo.com as Alice. Upload a video (say, video id - 118026546) and allow anyone to leave comments for that video .
2. Login as Bob and navigate to the video URL - https://vimeo.com/118026546.
3. Leave a comment. Edit that comment and capture the request using burp proxy. Captured request looks like -

    POST /118026546 HTTP/1.1
    Host: vimeo.com
    [...]
    
    text=abcd&action=edit_comment&comment_id=12984882&token=[...]

4. From Alice account, change the video settings and do not allow anyone to comment.
5. From Bob account, access the video url (https://vimeo.com/118026546) and it displays 'Sorry,     comments have been disabled by the owner of this video' message. At this point Bob can't add new comments or edit previous comments. However, Bob can edit his previous comments by replaying the request captured in step 3.

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
