---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1641088'
original_report_id: '1641088'
title: Last video frame is still sent after video is disabled in a call
weakness: Privacy Violation
team_handle: nextcloud
created_at: '2022-07-18T18:38:45.732Z'
disclosed_at: '2022-09-16T04:52:42.597Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: nextcloud/spreed
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# Last video frame is still sent after video is disabled in a call

## Metadata

- HackerOne Report ID: 1641088
- Weakness: Privacy Violation
- Program: nextcloud
- Disclosed At: 2022-09-16T04:52:42.597Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
When a participant is in a call and that participant disables the video rather than a black frame the last frame of the video will be sent. Similarly, if the video is disabled before joining the call the last frame of the video before joining the call will be sent.

The video is not directly visible in the Web UI, as the received video is initially disabled and only shown once some media is received. However, it may be briefly visible in the Android app, as the Android app has the opposite behaviour, it assumes that the received video is enabled and then disables it once the video state is received. The iOS app has not been checked.

In any case, as the frame is sent it can be accessed in the WebUI by assigning the track to a manually created video element, as described in the steps below.

## Steps To Reproduce:
- In a browser, start a call with a camera selected but video disabled
- In a private window, join the call as a participant without microphone nor camera selected
- In the console of the private window, paste:
```
videoElement = document.createElement('video')
document.body.appendChild(videoElement)
videoElement.srcObject = new MediaStream()
videoElement.srcObject.addTrack(OCA.Talk.SimpleWebRTC.webrtc.peers[0].pc.getReceivers()[1].track)
videoElement.style.zIndex = 10000000
videoElement.style.position = 'absolute'
videoElement.style.top = 0
videoElement.play()
```

## Impact

An attacker could see the last video frame of any participant who has video disabled but a camera selected.

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
