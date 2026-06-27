---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '155657'
original_report_id: '155657'
title: Arbitrary Code Injection in ownCloud’s Windows Client
weakness: Command Injection - Generic
team_handle: owncloud
created_at: '2016-07-31T19:00:09.481Z'
disclosed_at: '2016-11-23T18:45:41.271Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- command-injection-generic
---

# Arbitrary Code Injection in ownCloud’s Windows Client

## Metadata

- HackerOne Report ID: 155657
- Weakness: Command Injection - Generic
- Program: owncloud
- Disclosed At: 2016-11-23T18:45:41.271Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The current ownCloud Windows Desktop client is prone to an arbitrary code injection vulnerability.

The underlying issue is that the ownCloud desktop client tries to load QT extensions from C:\usr\i686-w64-mingw32\sys-root\mingw\lib\qt5\plugins.

As any authenticated user on Windows is allowed to create new folders within C:, the expected folder structure can be created.

What that means is that a local attacker can create a malicious QT extensions that gets automatically loaded on the next launch of the ownCloud Desktop client.

To verify the issue I first tried to simply create a new QT imageformats plugin. However I failed! Have you ever tried to install QT? So I decided to simply modify an existing DLL.

Hence, I used Hopper to disassemble the qwindows.dll platform’s library to learn more about its entry points. With that knowledge I planned to modify the DLL so that it shows a simply message box. The necessary shellcode was created with Metasploit:

msfvenom -a x86 --platform windows -p windows/messagebox TEXT="DLL Loaded" EXTIFUNC=process -f raw > shellcode
cat shellcode |xxd -p

I then overwrote some bytes after one of the previously identified DLL entry points with the shellcode.

After placing the modified payload DLL into C:\usr\i686-w64-mingw32\sys-root\mingw\lib\qt5\plugins\platforms the shellcode got executed after launching the ownCloud desktop client.

Please see the attached PDF for some images documenting the process.
Furthermore I created a private screen capture: https://owncloud.bogner.sh/s/Ik8AYJ9FfY5Rkyq

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
