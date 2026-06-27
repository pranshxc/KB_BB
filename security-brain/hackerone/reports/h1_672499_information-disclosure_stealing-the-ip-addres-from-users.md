---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '672499'
original_report_id: '672499'
title: Stealing the ip addres from users
weakness: Information Disclosure
team_handle: vanilla
created_at: '2019-08-13T15:30:35.696Z'
disclosed_at: '2020-07-29T16:13:49.938Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: https://github.com/vanilla/vanilla/
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Stealing the ip addres from users

## Metadata

- HackerOne Report ID: 672499
- Weakness: Information Disclosure
- Program: vanilla
- Disclosed At: 2020-07-29T16:13:49.938Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi team!

#Summary
Pixel that steals your data. 
By creating an image in https://iplogger.org/ and inserting it in the forum we can steal some data (ip, language, geo location) of the users who see the message.

#Steps to reproduce
+ Set "wyswyg" on
+ Create an image from https://iplogger.org/ and use the link to capture data
+ Insert a link (external img) in a forum or private message (https://iplogger.org/2Znmm5)
+ Enter the forum / message with another browser
+ Show the "listfull" link provided by "ipblogger.org" to see the ip captured by the image (https://iplogger.org/listfull/36r492Znmm5)
+ The data was captured

#Solution
You can fix this in different ways, but in my opinion, it would be better if you proxy all objects from third-party resources and create a CSP.

## Impact

A malicious user can capture sensitive information from forum users. In the case of private messages, you can easily detect if the user read or not the message .. simulating the "read" of whatsapp.

Find out the geo location with https://iplookup.flagfox.net/

Regards!

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
