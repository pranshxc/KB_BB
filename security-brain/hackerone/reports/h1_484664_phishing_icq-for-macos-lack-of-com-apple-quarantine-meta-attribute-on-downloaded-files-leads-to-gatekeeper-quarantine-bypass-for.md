---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '484664'
original_report_id: '484664'
title: 'ICQ for macOS: lack of `com.apple.quarantine` meta-attribute on downloaded
  files leads to GateKeeper/Quarantine bypass for downloaded executables'
weakness: Phishing
team_handle: mailru
created_at: '2019-01-23T14:08:34.079Z'
disclosed_at: '2019-09-17T10:07:37.332Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: ICQ
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- phishing
---

# ICQ for macOS: lack of `com.apple.quarantine` meta-attribute on downloaded files leads to GateKeeper/Quarantine bypass for downloaded executables

## Metadata

- HackerOne Report ID: 484664
- Weakness: Phishing
- Program: mailru
- Disclosed At: 2019-09-17T10:07:37.332Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary

Quarantine & GateKeeper are important macOS security mechanisms, which prevent user/device from running unsigned executables and warn users about executables downloaded from the remote. 

> Conceptually, Quarantine & GateKeeper are similar to MOTW on Windows.

Applications that could download files should enable file quarantine, because:

1. Missing quarantine attribute for downloaded files allows a remote attacker to send an executable file that won't be checked by Gatekeeper on victim's machine.

2. Launching downloaded executable files without `com.apple.quarantine` meta-attribute won't show an alert about launching an executable file from the remote.

3. Summarizing this: opening of a downloaded executable file immediately leads to code execution bypassing Quarantine(files from remote) & GateKeeper(codesign).

> Tip: check `com.apple.quarantine` meta-attribute with "xattr" util

## Steps To Reproduce:

1. Attacker sends `exploit.terminal` to the victim (file can't be signed)
2. Victim opens `exploit.terminal` file
3. No alert from Gatekeeper about unsigned executable
4. No alert about running executable file downloaded from the web
5. Shell commands from `exploit.terminal` get executed immediately after click.

### .terminal
1. `.terminal` files can't be signed but could lead to code execution. 
2. Disabled quarantine allows attacker to abuse this flaw and decrease required user interaction from `download archive -> unpack archive -> open something from archive` to `download file -> launch file`.
3.  Download&Launch is a common user flow, because macOS doesn't have any executable files which could lead to immediate code execution. macOS users generally feel safe about opening files.

> Also, `.terminal` files are just a plain XML, so it can't be detected by most antivirus/EDR software.

Actual result - Files downloaded through ICQ should have `com.apple.quarantine` meta attribute.
Expected result - Files downloaded through ICQ don't have `com.apple.quarantine` meta attribute.

## Additional info

 `exploit.terminal` file attached to this report (`echo "Hello" && id`)

## Impact

1. Downloaded through ICQ executable files bypass Quarantine/GateKeeper. 
2. `.terminal` files shorten required user interaction to  ~2 clicks.

Additional impact - code execution happens even in environments hardened with "Apps from AppStore only" GateKeeper setting.

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
