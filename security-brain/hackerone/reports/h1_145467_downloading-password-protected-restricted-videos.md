---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145467'
original_report_id: '145467'
title: Downloading password protected / restricted videos
team_handle: vimeo
created_at: '2016-06-17T16:40:05.223Z'
disclosed_at: '2016-09-05T13:37:39.122Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 41
tags:
- hackerone
---

# Downloading password protected / restricted videos

## Metadata

- HackerOne Report ID: 145467
- Weakness: 
- Program: vimeo
- Disclosed At: 2016-09-05T13:37:39.122Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Using: https://vimeo.com/api/atv/clip/VideoID it is possible to get the title, description & download the file regardless on any privacy settings (this includes both setting the video to 'Only me' and using a password)

For proof using my own video: https://vimeo.com/171116158 which has the password *gazza_hacker1* (as shown in the screenshot) - all testing was done in a separate browser to avoid already being authenticated

Metadata page: https://vimeo.com/api/atv/clip/171116158/

<key>title</key>
<string>Proof of access</string>
<key>subtitle</key>
<string>by aaaa aaaa</string>
...
<key>summary</key>
<string>
Viewing metadata and subsequently downloading of this video without entering password proves that this is a vulnerability
</string>

In order to download the video, the *play* xml file with signature is used:

<key>event-handlers</key>
<dict>
<key>action</key>
<string>load-url</string>
<key>parameters</key>
<dict>
<key>url</key>
<string>
https://vimeo.com/api/atv/clip/171116158/play?signature=4537ede998fa162e9d9ea1c7c9dcfd88ac3092df&timestamp=1466180664
</string>

Which when visited, contains the URL where the file can be downloaded: 

<key>media-url</key>
<string>
https://vimeo-prod-src-std-eu.storage.googleapis.com/videos/550779256?GoogleAccessId=GOOGHOVZWCHVINHSLPGA&Expires=1466184013&Signature=5RHxaH9oQogEKeUQ3NaDtVU%2FBNU%3D
</string>


**P.S:** The above link may have expired by the time this report is viewed; replicating the steps starting from https://vimeo.com/api/atv/clip/171116158/ will allow it to be downloaded. In addition, depending on the browser, it may simply be named *550779256* when it is downloaded. It is in fact an mp4 file and if renamed such (or playback is attempted) you will see this is the same video.

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
