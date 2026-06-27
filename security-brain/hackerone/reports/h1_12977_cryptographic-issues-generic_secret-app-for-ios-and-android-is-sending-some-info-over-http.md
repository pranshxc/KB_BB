---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '12977'
original_report_id: '12977'
title: secret app for iOS and android is sending some info over HTTP
weakness: Cryptographic Issues - Generic
team_handle: secret
created_at: '2014-05-23T22:36:10.930Z'
disclosed_at: '2014-08-16T23:31:13.056Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cryptographic-issues-generic
---

# secret app for iOS and android is sending some info over HTTP

## Metadata

- HackerOne Report ID: 12977
- Weakness: Cryptographic Issues - Generic
- Program: secret
- Disclosed At: 2014-08-16T23:31:13.056Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

POC for android:

POST /metrics HTTP/1.1
Content-Type: application/json
User-Agent: Dalvik/1.6.0 (Linux; U; Android 4.2.2; google_sdk Build/JB_MR1.1)
Host: notify.bugsnag.com
Connection: Keep-Alive
Accept-Encoding: gzip
Content-Length: 468

{"device":{"id":"6a2be12c-db31-4a3b-9684-f4d5a3e7188a","model":"google_sdk","osVersion":"4.2.2","totalMemory":50331648,"apiLevel":17,"jailbroken":true,"manufacturer":"unknown","locale":"en_US","screenResolution":"728x480","screenDensity":1.5,"osName":"android"},"app":{"releaseStage":"production","packageName":"ly.secret.android","id":"ly.secret.android","version":"1"},"user":{"id":"6a2be12c-db31-4a3b-9684-f4d5a3e7188a"},"apiKey":"42062feb3044ef86b492c724ffc87691"}






POC for IOS:


POST /aas.do HTTP/1.1
Host: data.flurry.com
Proxy-Connection: keep-alive
Accept-Encoding: gzip, deflate
Content-Type: application/octet-stream
Accept-Language: en-us
Accept: */*
Pragma: no-cache
Content-Length: 294
Connection: keep-alive
User-Agent: Secret/3 CFNetwork/672.0.8 Darwin/14.0.0

{F+.QQWQYVHGXCQ4JFYX8HXW3$B51F061B-B2B4-4B61-8695-E9CE5D3772CF$DD8B763A-F256-46BB-A102-4F86171F0B9CÁd)6þ>Ø³@·ÇçØqÙF%4hF+.ß
scr.height480device.archarm32device.os.version7.0.4device.model.1	iPhone4,1	scr.width320âxõÑ





i attached POC images

please fix it by using HTTPS ( secure one )

best regards

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
