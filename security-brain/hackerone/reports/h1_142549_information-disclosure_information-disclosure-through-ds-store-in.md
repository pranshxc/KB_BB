---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '142549'
original_report_id: '142549'
title: Information Disclosure through .DS_Store in ██████████
weakness: Information Disclosure
team_handle: x
created_at: '2016-06-01T20:14:50.732Z'
disclosed_at: '2016-12-12T18:58:51.313Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
tags:
- hackerone
- information-disclosure
---

# Information Disclosure through .DS_Store in ██████████

## Metadata

- HackerOne Report ID: 142549
- Weakness: Information Disclosure
- Program: x
- Disclosed At: 2016-12-12T18:58:51.313Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello!

Description:
The website located at █████████ suffers from an information disclosure through ".DS_Store" file, accessible to unauthorised external users.
In the Apple OS X operating system, .DS_Store is a file that stores custom attributes of its containing folder.

Reproduction Steps:
Guide for installing DS_Store parser - https://digi.ninja/projects/fdb.php

First link: (See pic 0 and 1)
███████.DS_Store

Second link: (See pic 2 and 3)
████Packages/.DS_Store
This directory contain tons of packages for MacOS
Including licence keys (See pic 4 and 5) 
██████████Packages/█████████
██████████Packages/████
and etc
Certificate for WIFI (See pic 6)
█████████Packages/█████
Twitter Root certificate (See pic 8)
█████████Packages/███████
And other juicy stuff which is intended only for Twitter employees

Third link (See pic 7)
██████████Scripts/.DS_Store
This directory contain tons of scripts for installation and configuring corporate computers.

In one case the attacker can just use Twitter licenses and etc (for obvious reasons, I didn't check whether this licences is still active ), in other this information can be useful for future attacks.

Please let me know if you need some extra information.
Thanks in advance!

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
