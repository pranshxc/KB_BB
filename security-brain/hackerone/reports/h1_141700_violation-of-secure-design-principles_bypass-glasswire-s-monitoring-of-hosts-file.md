---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '141700'
original_report_id: '141700'
title: Bypass GlassWire's monitoring of Hosts file
weakness: Violation of Secure Design Principles
team_handle: glasswire
created_at: '2016-05-28T14:20:21.804Z'
disclosed_at: '2016-07-23T21:18:11.898Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Bypass GlassWire's monitoring of Hosts file

## Metadata

- HackerOne Report ID: 141700
- Weakness: Violation of Secure Design Principles
- Program: glasswire
- Disclosed At: 2016-07-23T21:18:11.898Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Product version: 1.2.64beta
OS version: Windows 8.1 Enterprise x86

If a program modifies the Hosts file (C:\Windows\System32\drivers\etc\hosts), GlassWire notifies the user that "system file changed" with the path of the hosts file (see attachment "screenshot_hosts_changed.png"). I discover that a malware (running with admin privilege) can change the content of hosts file without triggering this notification. The method is to use hardlink.

To reproduce:
Step 1: Open cmd.exe as administrator
Step 2: execute "fsutil hardlink create c:\ProgramData\hosts.txt c:\windows\system32\drivers\etc\hosts" in cmd.exe
Step 3: execute "echo ::1 example.local>>c:\ProgramData\hosts.txt" in cmd.exe
You can see that the notification is not triggered after step3. See "screenshot_modified_via_hardlink_no_notification.png".

Now execute "echo ::1 example2.local>>c:\windows\system32\drivers\etc\hosts" in cmd.exe. You receive a notification that hosts file is modified, prompted by GlassWire. See "screenshot_modified_directly_have_notification.png".

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
