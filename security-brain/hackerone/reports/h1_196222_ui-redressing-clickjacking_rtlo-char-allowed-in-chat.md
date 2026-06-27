---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '196222'
original_report_id: '196222'
title: RTLO char allowed in chat
weakness: UI Redressing (Clickjacking)
team_handle: snapchat
created_at: '2017-01-06T10:04:23.151Z'
disclosed_at: '2017-02-28T19:44:57.677Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- ui-redressing-clickjacking
---

# RTLO char allowed in chat

## Metadata

- HackerOne Report ID: 196222
- Weakness: UI Redressing (Clickjacking)
- Program: snapchat
- Disclosed At: 2017-02-28T19:44:57.677Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey all,

There seems to be no filtering of strange unicode characters such as U+202E which is an Right-To-Left-Override.
I can send messages like "Hey check out my new song at example.com/song[rtlo]3pm.exe" and everyone would see the link as "example.com/songexe.mp3". 
Links that end with .exe are very suspicious but everyone would click on a link that ends with .mp3, filtering those characters would prevent clickjacking.
I tested this on the latest version of the Android App.

Thanks,
Marvin

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
