---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '50829'
original_report_id: '50829'
title: A user can post comments on other user's private videos
weakness: Privilege Escalation
team_handle: vimeo
created_at: '2015-03-10T18:13:51.208Z'
disclosed_at: '2015-03-11T14:37:49.514Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- privilege-escalation
---

# A user can post comments on other user's private videos

## Metadata

- HackerOne Report ID: 50829
- Weakness: Privilege Escalation
- Program: vimeo
- Disclosed At: 2015-03-11T14:37:49.514Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It is possible for a user to post comments on other's private videos.

Steps to verify:
1. Log into www.vimeo.com as Alice and create a video (say, AliceVideo with id - 118026546) with 'Allow anyone to see my videos' setting.
2. Login as Bob and create an album (say, BobAlbum with album id 3295969). 
3. From Bob, navigate to the AliceVideo URL - https://vimeo.com/118026546. Click collections and add video to BobAlbum.
4. Navigate to BobAlbum and click the AliceVideo. The URL will looks like, https://vimeo.com/album/3295969/video/118026546
5. Add a new comment and capture the request using burp proxy. Captured request looks like,

    POST /118026546 HTTP/1.1
    Host: vimeo.com
    [...]

    text=test&action=add_comment&token=...&version=...&group_id=3295969&context_id=3295969&context_type=album&add_comment=Add%20a%20new%20comment

6. From Alice account, make AliceVideo as private (check 'only me'->'apply to all existing videos' setting).

7. From Bob account, access the AliceVideo URL (https://vimeo.com/album/3295969/video/118026546) and it displays 'permssion denied' message. At this point, Bob can't view the video or leave comments. However, Bob can post comments on the private video by replaying the request captured in step 5.

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
