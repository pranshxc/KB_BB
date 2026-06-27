---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1338781'
original_report_id: '1338781'
title: User files is disclosed when someone called while the screen is locked
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2021-09-13T19:57:30.684Z'
disclosed_at: '2022-03-14T15:41:56.047Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: com.nextcloud.talk2
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- information-disclosure
---

# User files is disclosed when someone called while the screen is locked

## Metadata

- HackerOne Report ID: 1338781
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2022-03-14T15:41:56.047Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
User files in the server is disclosed while the screen is locked when someone called. 

## Steps To Reproduce:
[add details for how we can reproduce the issue]

1.) Make 2 Accounts, Lets call them Account A and Account B
2.) Using Account A login to (https://nextcloud/apps/spreed/)
3.) Using Account B login to NextCloud Talk App in your Phone and Lock the Screen
4.) Using Account A call Account B
5.) Using Account B accept the call and click the Message or SMS icon in the bottom left
6.) Attach a file and Press share from your nextcloud server
7.) You can see the user files

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

████

## Impact

A malicious attacker can see the user files by calling the phone while the screen is locked.

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
