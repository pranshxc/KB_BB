---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '257004'
original_report_id: '257004'
title: Privilege Escalation by abusing non-existent path. (Windows)
weakness: Privilege Escalation
team_handle: portswigger
created_at: '2018-11-14T22:16:09.559Z'
disclosed_at: '2019-03-13T08:50:22.266Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 57
asset_identifier: Burp Suite Pro/Community
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: high
tags:
- hackerone
- privilege-escalation
---

# Privilege Escalation by abusing non-existent path. (Windows)

## Metadata

- HackerOne Report ID: 257004
- Weakness: Privilege Escalation
- Program: portswigger
- Disclosed At: 2019-03-13T08:50:22.266Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

# Vulnerability Overview
When Burpsuite runs, it tries to load some DLLs in the path ```C:\Program%20Files```. Because the folder doesn't exists, it can be created **by a low-privileged user** which can inject arbitrary DLL into the process when another ** privileged user** runs Burpsuite. I have verified the vulnerability in the Pro Version but I'm pretty sure the community version is also affected.

# Vulnerability Description
Monitoring the BurpSuite application in Process Monitor, we can see that it tries to load 2 DLLs from a directory that does not exist.
{F375743}

The interesting thing here is, that on Windows (verified for 7,10,Server 2008 R2 and Server 2012) every authenticated user is allowed to add new folders on the ```C:\``` drive. This in turn allows an attacker to create the folder structure and inject arbitrary DLLs to Burpsuite.

# Vulnerability Reproduction Steps
1. Login as a low-privileged user on a system which has Burpsuite installed.
{F375748}
2. Create the directory tree as shown in the image below.
{F375753}
3. Copy the attached ```sunec.dll``` file to the last directory (amd64).
4. Simulate the login of a privileged user , run Burpsuite and a message should pop up.
{F375756}

## Impact

A low privileged user can execute code as a high privileged user.

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
