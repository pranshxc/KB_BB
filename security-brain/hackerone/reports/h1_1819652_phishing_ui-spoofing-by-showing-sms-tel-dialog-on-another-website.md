---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1819652'
original_report_id: '1819652'
title: 'UI spoofing by showing sms:/tel: dialog on another website'
weakness: Phishing
team_handle: brave
created_at: '2023-01-01T08:27:16.017Z'
disclosed_at: '2023-06-22T05:50:39.559Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: https://github.com/brave/brave-ios
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
- phishing
---

# UI spoofing by showing sms:/tel: dialog on another website

## Metadata

- HackerOne Report ID: 1819652
- Weakness: Phishing
- Program: brave
- Disclosed At: 2023-06-22T05:50:39.559Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
The dialog asking if you want to open the sms:/tel: link doesn't show the caller origin.
Also, unlike the JavaScript alert dialog, etc., it appears on the top screen even when another tab is active.
This can be used for UI spoofing attack to make it looks as if another site is displaying the dialog.

## Products affected: 

 * Brave for iOS (Version 1.45.2)

## Steps To Reproduce:

 * Visit https://csrf.jp/brave/sms.php
 * Tap "Click Me" button
 * google.com is opened in the new tab
 * Confirmation dialog for sms: link is shown on google.com

## Supporting Material/References:

  * See the demonstration movie I attached

## Impact

This can be used for UI spoofing attack to make it looks as if another site is displaying the dialog.

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
