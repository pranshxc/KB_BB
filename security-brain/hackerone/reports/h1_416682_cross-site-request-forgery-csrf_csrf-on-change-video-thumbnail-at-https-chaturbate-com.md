---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '416682'
original_report_id: '416682'
title: CSRF on change video thumbnail at https://chaturbate.com
weakness: Cross-Site Request Forgery (CSRF)
team_handle: chaturbate
created_at: '2018-10-01T06:42:31.826Z'
disclosed_at: '2018-10-07T01:42:30.963Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF on change video thumbnail at https://chaturbate.com

## Metadata

- HackerOne Report ID: 416682
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: chaturbate
- Disclosed At: 2018-10-07T01:42:30.963Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi

I noticed Changing video thumbnail option have the workflow with GET request and there is lack of csrf token on changing video thumbnail option,so if attacker somehow able to obtain the thumbnail_id of victim's video then it can help attacker to inducing victim to change video thumbnail.

Vulnerable Request:

GET /photo_videos/video/thumbnail/video_id/?thumb=thumbnail_id HTTP/1.1
Host: chaturbate.com

Steps to reproduce:

setup:-
Video A :- an  uploaded video on victim's account.
video_id :- id of video A from victim's account
thumbnail_id :- id of any thumbnail from video A.

1. Configure the upper setup along with this url https://chaturbate.com/photo_videos/video/thumbnail/video_id/?thumb=thumbnail_id
2. Feed the configured url to victim(as setup in step 1)
3. Wait 5-9 minutes.
4. Open your bio tab.
5. Check, the video thumbnail will successfully get changed.

With Best Regards

## Impact

Attacker can induce victim to change video's thumbnail.

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
