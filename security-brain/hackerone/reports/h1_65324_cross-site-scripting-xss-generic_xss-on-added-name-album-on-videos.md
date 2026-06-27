---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '65324'
original_report_id: '65324'
title: XSS on added name album on videos.
weakness: Cross-site Scripting (XSS) - Generic
team_handle: vkcom
created_at: '2015-06-01T22:03:00.035Z'
disclosed_at: '2015-06-26T14:07:55.756Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on added name album on videos.

## Metadata

- HackerOne Report ID: 65324
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: vkcom
- Disclosed At: 2015-06-26T14:07:55.756Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi

Steps to reproduce:

First go to :  https://vk.com/video
Next click on Add a Video
After add a video from youtube and on title Field Insert TEST XSS
And click save.
Next after this go to https://vk.com/video again and you will see video  with the name TEST XSS
Click above TEST XSS and you will for https://vk.com/video?z=video307088553_171482428%2Falbum307088553 
Now scroll and you will see word : Added with a right , put mouse above this and create album 

In folder name field insert this xss payload:

"><img src=x onerror=prompt(1)>
And click save.
Now video will be added to this album
Now go with the mouse above added word and click on added word.
And xss will be executed.
Ty :)

Works on google chrome :  43.0.2357.81 m

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
