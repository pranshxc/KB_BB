---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '41856'
original_report_id: '41856'
title: HTML/XSS rendered in Android App of Crashlytics through fabric.io
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2014-12-25T09:40:56.422Z'
disclosed_at: '2015-02-18T18:38:02.252Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HTML/XSS rendered in Android App of Crashlytics through fabric.io

## Metadata

- HackerOne Report ID: 41856
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2015-02-18T18:38:02.252Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey hi,

While in fabric , the app name is rendered as HTML/XSS in android app of Crashlytics  like shown in the screenshot.

Steps to reproduce:
Create an app with the name of payload in my case i have used, "><img src=x>
under the following URL https://www.fabric.io/img-srcx-onerrorprompt03/android/apps/imgsrcxonerrorprompt0.myapplication/beta/releases/latest
(replace the app names wherever needed)
Send invitation to users to test the APP
users will get the invitation and will be forced to download the Crashlytics app,
once downloaded they will see the app name like in the screenshot.


Regards,
Karthik
Wesecureapp

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
