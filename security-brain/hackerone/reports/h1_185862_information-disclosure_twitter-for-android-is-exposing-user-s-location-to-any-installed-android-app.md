---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '185862'
original_report_id: '185862'
title: Twitter for android is exposing user's location to any installed android app
weakness: Information Disclosure
team_handle: x
created_at: '2016-11-27T18:58:48.072Z'
disclosed_at: '2017-01-13T17:48:00.938Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
tags:
- hackerone
- information-disclosure
---

# Twitter for android is exposing user's location to any installed android app

## Metadata

- HackerOne Report ID: 185862
- Weakness: Information Disclosure
- Program: x
- Disclosed At: 2017-01-13T17:48:00.938Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I have noticed that while a user is using the location feature in twitter's android application twitter is sending the user's location to all other locally installed applications without verifying the possible (malicious) receivers (By sending a broadcast). As a poc I have created an application (attached) which asks for no permissions from android and is just listening to location broadcasts sent by twitter. You can see both the application's apk and its code attached.
I have also created a poc video which shows how to use it - I have used an android emulator but it can also be used by a real device. Here is the video: https://vimeo.com/193261287 pass is: twittergps121
It can be seen in the video that the moment twitter asks for(and receives) gps signal - my malicious application is receiving it due to twitter forwarding this location - also my app has no permissions assigned.

Note: I am sending the coordinates to my emulator manually - but on a real device which allows twitter to use  location it is sent automatically.

Vulnerable code
===
This is happening because of the following lines in your app's code: 
```
paramLocation = new Intent("com.twitter.library.geo.LOCATION_CHANGED").putExtra("com.twitter.library.geo.LOCATION_EXTRA", paramLocation);
this.c.sendBroadcast(paramLocation);
```
Some variable names might be wrong due to obfuscation but the idea remains - you should probably add permission to the broadcast.

Implications
===
Any malicious application installed on a user's device can track the user's location without any permissions if the user is allowing twitter to access his location.

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
