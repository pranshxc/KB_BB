---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '430463'
original_report_id: '430463'
title: 'Keybase client: downloaded executables lack "com.apple.quarantine" meta-attribute
  [macOS]'
team_handle: keybase
created_at: '2018-10-29T21:04:34.618Z'
disclosed_at: '2019-09-16T19:58:09.447Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 76
tags:
- hackerone
---

# Keybase client: downloaded executables lack "com.apple.quarantine" meta-attribute [macOS]

## Metadata

- HackerOne Report ID: 430463
- Weakness: 
- Program: keybase
- Disclosed At: 2019-09-16T19:58:09.447Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary

1. Missing quarantine attribute for downloaded files allows remote attacker to send executable file that won't be checked by Gatekeeper (codesign bypass). 

2. Since sent executable files lack `com.apple.quarantine` meta-attribute, no alert about launching executable file from the web will be shown to user.

3. That means, dblclick on file in Finder.app (or any similar gesture to launch the file) immediately launches the attacker's file.

## PoC

1. Attacker sends `exploit.terminal` to the victim (file is unsigned)
2. Victim opens `exploit.terminal`
3. No alert from Gatekeeper about unsigned executable
4. No alert about running executable file downloaded from the web
5. Shell commands from `exploit.terminal` execute with user-level privileges.

> NOTE: if victim is sudoer with no pass, attacker can insert `sudo` commands in `*.terminal` file and gain `root` permissions.

Screencast + `exploit.terminal` file sample attached.

> Screencast: `xattr <file>` shows apple-specific meta-attributes like `com.apple.quarantine`

## Impact

Quarantine + codesigning are basic security mechanisms, which prevents user/device from running untrusted executables.

Keybase allows to send **messages** and share **KBFS** with **any Keybase user** (!), that allows attacker to make a massive spam of `.terminal` files with malicious payload.

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
