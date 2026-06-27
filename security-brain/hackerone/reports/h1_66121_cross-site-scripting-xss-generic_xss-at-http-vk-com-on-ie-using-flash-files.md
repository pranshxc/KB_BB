---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '66121'
original_report_id: '66121'
title: XSS at http://vk.com on IE using flash files
weakness: Cross-site Scripting (XSS) - Generic
team_handle: vkcom
created_at: '2015-06-05T09:56:45.013Z'
disclosed_at: '2015-10-30T12:23:19.628Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS at http://vk.com on IE using flash files

## Metadata

- HackerOne Report ID: 66121
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: vkcom
- Disclosed At: 2015-10-30T12:23:19.628Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Steps**

+ Open the below url in **Internet Explorer**
 
```
http://vk.com/swf/photo_uploader_lite.swf?h=h?&onMouseOver=document.write(window.location.hash.substr(1))#<script>alert(document.domain)</script>
```

+ Just hover your mouse over the page.

**Minor Observations**

+ No "X-Content-Type-Options: nosniff" header allows IE to play the flash file directly whereas other browsers present download dialog as the content type served is **application/zip**.
+ No X-Frame options will allow this attack to be placed inside an iframe and run stealthily.
+ Other flash files such as **http://vk.com/swf/CaptureImg.swf** will also be vulnerable in a similar fashion.

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
