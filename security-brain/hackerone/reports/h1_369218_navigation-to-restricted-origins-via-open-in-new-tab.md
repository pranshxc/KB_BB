---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '369218'
original_report_id: '369218'
title: Navigation to restricted origins via "Open in new tab"
team_handle: brave
created_at: '2018-06-20T16:39:40.656Z'
disclosed_at: '2018-10-09T23:16:23.617Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: https://github.com/brave/browser-laptop
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
---

# Navigation to restricted origins via "Open in new tab"

## Metadata

- HackerOne Report ID: 369218
- Weakness: 
- Program: brave
- Disclosed At: 2018-10-09T23:16:23.617Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

It's possible to open links pointing to `file:///` origin from web pages using "Open link in a new tab" in context menu.

> https://hackerone.com/bugs?report_id=369185 shows unsafe `ssh://` protocol handling, which leads to information leak using ssh(OS username and etc.). The vulnerability is highly available, so it's possible to leverage it.

As of, we could get username, it's easy to predict path of the downloaded file:
`file:///Users/${USERNAME_FROM_SSH}/Download/${DOWNLOADED_FILE_NAME}`

### USERNAME_FROM_SSH 

When user initiates ssh session through browser, it's equal to running `ssh os_username@hostname.com`. So the host which receives connection request knows user's OS username.

### DOWNLOADED_FILE_NAME 

DOWNLOADED_FILE_NAME is `download` attribute of the link. That means, it's under the attacker's control.

## Products affected: 

Brave 0.22.810
V8 6.7.288.43
rev 8f30eeb
Muon 7.0.6
OS Release 17.6.0
Update Channel Release
OS Architecture x64
OS Platform macOS
Node.js 7.9.0
Brave Sync v1.4.2
libchromiumcontent 67.0.3396.71
OS: macOS 10.13.5 17F77 x86_64

## Steps To Reproduce:

Live PoC: https://brave-download-execute-local-fs-ifhsmtsbik.now.sh

> I could provide a PoC with "ssh step", if it could increase a bounty. Currently, OS username is hardcoded in `exploit.html`. Insert your **OS username** to run the exploit. (e.g. using devtools or locally)

1. Webpage requests navigation to `ssh://` -  user agrees.
2. Navigation happens, attacker's host received ssh connection request. Attacker knows user's OS username.
3. Webpage asks to download the file. Let's name it `file-load.html`. Downloading happens.
4. User opens a link(using "Open in a new tab") which points to `file:///Users/${USERNAME_FROM_SSH}/Download/file-load.html`
5. Navigation happens, downloaded HTML file executes on local file system.

Screencast attached.

## Impact

Navigation from web pages to `file:///` and executing downloaded (from the web) files on local filesystem is definitely a vulnerability, which additionally opens a wider attack surface for an attacker. 

> ~~Bypassing SOP on `file:///` origin could lead to a full-chain exploit 😈.~~

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
