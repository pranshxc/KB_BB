---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '55064'
original_report_id: '55064'
title: Bypass Setup by External Activity Invoke
team_handle: faceless
created_at: '2015-04-06T13:46:33.673Z'
disclosed_at: '2015-05-09T20:22:48.258Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
---

# Bypass Setup by External Activity Invoke

## Metadata

- HackerOne Report ID: 55064
- Weakness: 
- Program: faceless
- Disclosed At: 2015-05-09T20:22:48.258Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Tool Used: Drozer
Operating System: Android Kitkat 4.4.2

Note: Make sure the application is running on the device connected to the system.

1. With the help of Drozer tool, list down the activities exported by the application using the following command:
    run app.activity.info -a im.delight.faceless

2.  Once, we have the list try to invoke the activity " im.delight.faceless.ActivityAdd" with the following command:
     run app.activity.start --component im.delight.faceless  im.delight.faceless.ActivityAdd
which will land to "Write Message" screen directly without entering any information in the setup (such as contact number). Now try to publish some text on the given screen and hit "Publish"

3. Now, the application will automatically redirect to a setup screen, after the completion of the setup, it can be viewed that the text that was being published without any authentication is being published with the registered number/user.

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
