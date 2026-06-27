---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '50884'
original_report_id: '50884'
title: Bypass pin(4 digit passcode on your android app)
weakness: Privilege Escalation
team_handle: whisper
created_at: '2015-03-11T04:36:09.341Z'
disclosed_at: '2015-04-12T02:24:32.481Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- privilege-escalation
---

# Bypass pin(4 digit passcode on your android app)

## Metadata

- HackerOne Report ID: 50884
- Weakness: Privilege Escalation
- Program: whisper
- Disclosed At: 2015-04-12T02:24:32.481Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

i have found that this activities are exported
** Package: sh.whisper **
  sh.whisper.WMainActivity
  sh.whisper.WWhisperBrowserActivity
  sh.whisper.WRelatedActivity
  sh.whisper.WDiscoverActivity
  sh.whisper.WCategoryFeedActivity
  sh.whisper.WSettingsActivity
    Parent Activity: sh.whisper.WMainV4Activity
  sh.whisper.WShareActivity
  sh.whisper.WQuickCreateActivity
    Parent Activity: sh.whisper.WMainV4Activity
  sh.whisper.WUserActivity
  sh.whisper.WNotificationsActivity
  sh.whisper.WInboxActivity
  sh.whisper.WParseDeepLinkActivity
  sh.whisper.WAddGroupActivity

whisper android app have a 4 digits PIN that can be set by the user to protect from unauthorized access if the phone is lost(protection for user's inbox and notification) , but   **sh.whisper.WNotificationsActivity**
  and **sh.whisper.WInboxActivity** are exported ,so any android app can called these activities to bypass the **4-digit code**

watch this video on have i bypass the 4-digit code 

** references**
http://cwe.mitre.org/data/definitions/926.html

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
