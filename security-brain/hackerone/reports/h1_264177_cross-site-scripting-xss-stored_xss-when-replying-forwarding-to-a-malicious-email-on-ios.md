---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '264177'
original_report_id: '264177'
title: XSS when replying / forwarding to a malicious email on iOS
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2017-08-29T04:14:14.746Z'
disclosed_at: '2017-12-28T15:04:02.595Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: ru.mail.mail
asset_type: APPLE_STORE_APP_ID
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS when replying / forwarding to a malicious email on iOS

## Metadata

- HackerOne Report ID: 264177
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2017-12-28T15:04:02.595Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application
--
Mail.ru for iOS

Testing environment
--
iOS 10

Steps to reproduce
--
1) Send you a mail with something like this in the From field: =?utf-8?b?PHNjcmlwdD5hbGVydChkb2N1bWVudC5jb29raWUpPC9zY3JpcHQ+?=@pwnsdx.pw

Note: This is a base64 string of "<script>alert(document.cookie)</script>"

2) Try to forward or reply to that email.

Note: If you kill the app from the iOS multitask and run it again, the reply / forward will show again, executing one more time the JS code.

Actual results
--
JS alert with current cookies is shown

Expected results, security impact description and recommendations
--
Nothing happens

PoC, exploit code, screenshots, video, references, additional resources
--

Payload is: `From: =?utf-8?b?PHNjcmlwdD5hbGVydChkb2N1bWVudC5jb29raWUpPC9zY3JpcHQ+?=@pwnsdx.pw`

Video has been attached.

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
