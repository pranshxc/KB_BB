---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '179121'
original_report_id: '179121'
title: Information disclosure of website
weakness: Information Disclosure
team_handle: brave
created_at: '2016-10-31T15:43:28.602Z'
disclosed_at: '2016-11-16T06:21:09.486Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Information disclosure of website

## Metadata

- HackerOne Report ID: 179121
- Weakness: Information Disclosure
- Program: brave
- Disclosed At: 2016-11-16T06:21:09.486Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

> NOTE! Thanks for submitting a report! Please fill all sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty.

## Summary:
Malicious application can see what the user is browsing
[add summary of the vulnerability]

## Products affected: 
BRave browser for android
 * operating system, Brave version or Brave website page, etc.
Android Version Os : 4.4, App version:1.9.56
## Steps To Reproduce:
1)Open adb shell
2)ps | grep "app process id"
3)logcat *:D | grep "process id of app"

YOu will see all the url that the user is browsing 

 * List the steps needed to reproduce the vulnerability

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)
http://www.androidsecurity.guru/category/logging/

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
