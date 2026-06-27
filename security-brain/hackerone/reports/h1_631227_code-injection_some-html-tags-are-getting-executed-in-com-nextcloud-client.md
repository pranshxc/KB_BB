---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '631227'
original_report_id: '631227'
title: Some HTML Tags are Getting Executed in com.nextcloud.client
weakness: Code Injection
team_handle: nextcloud
created_at: '2019-06-28T05:16:33.282Z'
disclosed_at: '2019-07-26T08:02:14.489Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: com.nextcloud.client
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- code-injection
---

# Some HTML Tags are Getting Executed in com.nextcloud.client

## Metadata

- HackerOne Report ID: 631227
- Weakness: Code Injection
- Program: nextcloud
- Disclosed At: 2019-07-26T08:02:14.489Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

###What is the Vulnerability? 
HTML Tags such as <h1> , <small> , <href> and <img> are Getting Executed in Next Cloud Client Mobile Application for Android which can then Results to Code Injection.

###Reproduction Steps

1.) Using Next Cloud Client Mobile App on Android, Rename a Folder to ```<a href="google.com">test```
Our HTML tag Was Executed
{F518303}

2.)Rename the folder to ```small<h1>BIG```
Our HTML tag Was Executed
{F518304}

3.) Rename the Folder to ```normal<small>small<h1>BIG```
Our HTML tag Was Executed
{F518305}

## Impact

If successfully exploited, impact could cover loss of confidentiality, loss of integrity, loss of availability, and/or loss of accountability

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
