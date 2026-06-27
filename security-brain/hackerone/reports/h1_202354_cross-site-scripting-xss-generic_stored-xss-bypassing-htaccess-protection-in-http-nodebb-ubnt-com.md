---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '202354'
original_report_id: '202354'
title: Stored XSS / Bypassing .htaccess protection in http://nodebb.ubnt.com/
weakness: Cross-site Scripting (XSS) - Generic
team_handle: ui
created_at: '2017-01-31T13:34:43.035Z'
disclosed_at: '2017-09-28T07:23:26.659Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS / Bypassing .htaccess protection in http://nodebb.ubnt.com/

## Metadata

- HackerOne Report ID: 202354
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: ui
- Disclosed At: 2017-09-28T07:23:26.659Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

While I was looking at your renewn SSL certificated, I have noticed the following link : http://nodebb.ubnt.com/

I have seen that this link was protected by htaccess password, but I have decided to run a nmap scan. By running the following :

```
sudo nmap -sSV -p- 104.131.159.88 -oA stage_ph -T4
```

one of the open ports was this : `4567/tcp open   tram?`

And, to my surprise the ip `104.131.159.88:4567`, as well as `http://nodebb.ubnt.com:4567/` were available from internet and unprotected.

Here, I have found a nodeBB instance and I have managed to create a persisted XSS by using the  upload API, that does not properly sanitize the file names and automatically sets wrong mime types. 

Normally, it seems that the user is allowed to upload only images, but the stored XSS was possible by injecting malicious html in the exif data and changing the file name to .html.

I have attached a video with the POC, as well as the exif image.

I have not managed to RCE, but it is also worth noting that uploading the file with the .php extension and writing php content using exif IS possible.

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
