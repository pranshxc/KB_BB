---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '943737'
original_report_id: '943737'
title: Arbitrary file read in Rocket.Chat-Desktop
team_handle: rocket_chat
created_at: '2020-07-27T12:12:21.429Z'
disclosed_at: '2022-02-06T19:36:37.488Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
---

# Arbitrary file read in Rocket.Chat-Desktop

## Metadata

- HackerOne Report ID: 943737
- Weakness: 
- Program: rocket_chat
- Disclosed At: 2022-02-06T19:36:37.488Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:** Rocket.Chat-Desktop is vulnerable to arbitrary file read.

## Releases Affected:

  * Rocket.Chat-Desktop-Client: < v3.0.0-develop

## Steps To Reproduce (by setting up a malicious server):

1. Go to `Administration » Layout » Custom Scripts » Custom Script for Logged In Users`
1. Insert the following script `window.open('file://c:/windows/system32/drivers/etc/hosts').eval('alert(document.body.innerText);');`
1. Click `Save changes`
1. Open Rocket.Chat-Desktop and connect to the server
1. A new window and an alert containing the contents of `c:/windows/system32/drivers/etc/hosts` will pop up.

## Suggested mitigation

  * Set `popups` to `false` [[`src » component » electron » WebViewComponent.js (line 16)`](https://github.com/RocketChat/Rocket.Chat.Electron/blob/develop/src/components/electron/WebViewComponent.js)].

## Impact

Arbitrary file read in Rocket.Chat-Desktop

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
