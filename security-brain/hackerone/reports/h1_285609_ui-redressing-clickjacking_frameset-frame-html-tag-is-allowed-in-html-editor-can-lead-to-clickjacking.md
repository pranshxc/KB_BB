---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '285609'
original_report_id: '285609'
title: Frameset(Frame) html tag is allowed in html editor.(can lead to clickjacking)
weakness: UI Redressing (Clickjacking)
team_handle: khanacademy
created_at: '2017-11-02T11:36:15.558Z'
disclosed_at: '2018-02-14T16:36:31.535Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- ui-redressing-clickjacking
---

# Frameset(Frame) html tag is allowed in html editor.(can lead to clickjacking)

## Metadata

- HackerOne Report ID: 285609
- Weakness: UI Redressing (Clickjacking)
- Program: khanacademy
- Disclosed At: 2018-02-14T16:36:31.535Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Sir/Mam ,
I was using the html editor in computer programming section , which allowed me to design a webpage. When i use the iframe tag , object tag and embed tag it show me the message that these tags are not allowed for security reasons(may be cause of clickjacking attack or something) but when i used frameset n frame tag it does not showed any message and allows them. 
The  X-frame option is set to same-origin. So, it allowed to load the user setting page in a frameset tag , (i also recorded the video too)which can lead to clickjacking attack. If there is restriction on iframe , object n embed tag then there should also be restriction on frameset(frame). 
P.S:The poc video is also attached below.

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
