---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1784645'
original_report_id: '1784645'
title: Passcode bypass on Talk Android app
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2022-11-26T12:04:27.911Z'
disclosed_at: '2023-01-09T05:49:57.485Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: com.nextcloud.talk2
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# Passcode bypass on Talk Android app

## Metadata

- HackerOne Report ID: 1784645
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2023-01-09T05:49:57.485Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
It is possible to bypass the passcode protection in nextcloud android talk by clicking the notification of a message.

Talk App Android version: ```15.0.2 RC1```

## Steps To Reproduce:

1. Create two users
1. Using User A login it to the web interface while User B on Talk App Android
1. Using User B setup the passcode protection in settings
1. Using User A send a message to User B
1. Wait for the notification and click it

## Supporting Material/References:

█████

## Impact

To exploit this the attacker needs to have a physical access to the  target's device which makes it severity to medium. 
Due to the bypass of passcode an attacker is able to access the user's nextcloud files and view conversations.

████████

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
