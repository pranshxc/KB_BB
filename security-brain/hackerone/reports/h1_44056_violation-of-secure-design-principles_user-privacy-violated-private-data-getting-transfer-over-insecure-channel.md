---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '44056'
original_report_id: '44056'
title: USER PRIVACY VIOLATED (PRIVATE DATA GETTING TRANSFER OVER INSECURE CHANNEL
  )
weakness: Violation of Secure Design Principles
team_handle: vimeo
created_at: '2015-01-16T16:30:42.220Z'
disclosed_at: '2015-01-20T23:40:02.007Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# USER PRIVACY VIOLATED (PRIVATE DATA GETTING TRANSFER OVER INSECURE CHANNEL )

## Metadata

- HackerOne Report ID: 44056
- Weakness: Violation of Secure Design Principles
- Program: vimeo
- Disclosed At: 2015-01-20T23:40:02.007Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Team ,

##Description : 
this report is about how a users private data is getting exploded over insecure channel .
while testing the iOS App of Vimeo , i am analyzing all the traffics and came to know the video which is uploaded in my account and which privacy setting is private only is getting exposed over HTTP via domain __pdl.vimeocdn.com__ .
i saw my own uploaded video is getting requested from that domain over HTTP .
so in this way many users private video can be exposed by attacker easily .

##POC Pic 1 : http://sd.uploads.im/2QiSa.png
##POC Pic 2 : http://sd.uploads.im/1DE3d.png

##Live POC : http://pdl.vimeocdn.com/62464/681/324557087.mp4?token=1421434056_e5acc7620a33be45549043758a368cb1 (Over HTTP)

##Fix : 
strictly enable HTTPS for all .


Thank You
Geekboy :)

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
