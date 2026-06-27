---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '12617'
original_report_id: '12617'
title: Account hijacking possible through ADB backup feature
weakness: Information Disclosure
team_handle: faceless
created_at: '2014-05-20T12:50:12.427Z'
disclosed_at: '2014-05-21T08:22:49.384Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# Account hijacking possible through ADB backup feature

## Metadata

- HackerOne Report ID: 12617
- Weakness: Information Disclosure
- Program: faceless
- Disclosed At: 2014-05-21T08:22:49.384Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It was found that if an attacker had access to an unlocked phone, they could take any data from the application's sandbox through ADB's backup feature.

Normally ADB backup allows applications to be backed up to the cloud. This means that if a user replaces or wipes their phone, they can restore app settings.

This feature is on by default and needs to be explicitly disabled in the manifest
<application allowBackup="false"

If enabled (or not explicitly disabled), then the backup feature can also be used over USB (details here: http://nelenkov.blogspot.co.uk/2012/06/unpacking-android-backups.html). This means that the shell user, which can not normally access files in the sandboxes of applications, can read and write to them.

In the case of the Faceless Android app, it meant that if an attacker had access to an unlocked android device, then they could recover all the files from Faceless' sandbox to their PC. This includes the im.delight.faceless_preferences.xml file which holds the username and password

This could then be restored to another device, allowing for account cloning.

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
