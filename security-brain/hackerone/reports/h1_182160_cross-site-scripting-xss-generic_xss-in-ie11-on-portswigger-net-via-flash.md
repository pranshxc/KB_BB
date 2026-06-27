---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '182160'
original_report_id: '182160'
title: XSS in IE11 on portswigger.net via Flash
weakness: Cross-site Scripting (XSS) - Generic
team_handle: portswigger
created_at: '2016-11-14T21:07:33.860Z'
disclosed_at: '2016-11-30T16:32:07.216Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 33
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in IE11 on portswigger.net via Flash

## Metadata

- HackerOne Report ID: 182160
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: portswigger
- Disclosed At: 2016-11-30T16:32:07.216Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Portswigger Security Team,

There is a reflective XSS vulnerability in portswigger.net. The flash file `https://portswigger.net/burp/tutorials/video-js/video-js.swf` is from an old video.js library (version 3.2.0) which is vulnerable to XSS.
This XSS will be blocked by CSP instruction `object-src https://portswigger.net/knowledgebase/papers/;` but it will execute on browsers that don't enforce this CSP like Internet Explorer 11.

POC link : https://portswigger.net/burp/tutorials/video-js/video-js.swf?readyFunction=alert%28document.domain%2b'%20XSSed!'%29

POC instructions :
- Open the POC link in Internet Explorer 11 with flash active
- The javascript payload executes in `https://portswigger.net`
(Tested on Windows 10)

Mitigation :
To solve this issue, replace the old `https://portswigger.net/burp/tutorials/video-js` library with the updated video.js library from http://videojs.com/. It is also better to host any swf file on a sandbox subdomain.

Regards,

Enguerran @opnsec

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
