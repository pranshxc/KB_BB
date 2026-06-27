---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '968328'
original_report_id: '968328'
title: Redirecting users to malicious torrent-files/websites using WebTorrent
weakness: Violation of Secure Design Principles
team_handle: brave
created_at: '2020-08-27T08:23:54.189Z'
disclosed_at: '2022-06-30T17:46:17.743Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: https://laptop-updates.brave.com/latest/winx64
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Redirecting users to malicious torrent-files/websites using WebTorrent

## Metadata

- HackerOne Report ID: 968328
- Weakness: Violation of Secure Design Principles
- Program: brave
- Disclosed At: 2022-06-30T17:46:17.743Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

An attacker can redirect a user to a malicious torrent file/website using a reverse tab-nabbbing flaw in WebTorrent.


##Description

WebTorrent allows user to open files after download of while they are being downloaded directly from the browser

{F965466}

An attacker can use this to redirect users to malicious websites and torrent files as the anchor tag allowing to open up the file is not prone to reverse tabnabbing attacks.

{F965467}

##Tested on

* Brave Version 1.12.114 Chromium: 84.0.4147.135 (Windows)

## Steps To Reproduce:

 * Visit the POC link https://php-demo-app-shibli.cfapps.io/brave/poc-bave.php?x=.torrent
* Click on "Start Torrent"
* Once the file starts downloading, try opening up the file
* You will see the previous tab will navigate to a different torrent file or website.

Please refer below video poc for better understanding.

{F965473}

## Impact

* An attacker can trick a victim to download a malicious file instead of the original file.
* An attacker can redirect a user to a malicious webpage for other harmful attacks.

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
