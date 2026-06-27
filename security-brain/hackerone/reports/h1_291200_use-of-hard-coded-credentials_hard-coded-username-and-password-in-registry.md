---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '291200'
original_report_id: '291200'
title: Hard Coded username and password in registry
weakness: Use of Hard-coded Credentials
team_handle: kaspersky
created_at: '2017-11-17T14:33:24.774Z'
disclosed_at: '2018-05-06T19:51:42.600Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- use-of-hard-coded-credentials
---

# Hard Coded username and password in registry

## Metadata

- HackerOne Report ID: 291200
- Weakness: Use of Hard-coded Credentials
- Program: kaspersky
- Disclosed At: 2018-05-06T19:51:42.600Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I was using a tool called RegShot to take a snap shot of the registry before and after installation in order to see what changes were being made in the registry and I discovered hard-coded credentials

I have attached the full comparison details of the registry changes

but these are the lines and reg entries where the credentials are stored:

 HKLM\SOFTWARE\Wow6432Node\KasperskyLab\AVP17.0.0\environment\dump\User: "kavdumps"
HKLM\SOFTWARE\Wow6432Node\KasperskyLab\AVP17.0.0\environment\dump\Password: "UxzAbKFLufVBSg8Y"
HKLM\SOFTWARE\Wow6432Node\KasperskyLab\AVP17.0.0\environment\dump\FTP: "kavdumps.kaspersky.com"

I was able to open browser and navigate to ftp://kavdumps.kaspersky.com which gave me a login prompt.
I used the username: kavdumps 
and password of: UxzAbKFLufVBSg8Y

I was able to login. The directory was empty however

I have attached a video and the log file

I have seperated the lines so it is easier to find in the file.

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
