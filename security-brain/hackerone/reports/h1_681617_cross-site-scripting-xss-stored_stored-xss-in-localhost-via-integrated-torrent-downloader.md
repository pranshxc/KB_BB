---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '681617'
original_report_id: '681617'
title: Stored XSS in localhost:* via integrated torrent downloader
weakness: Cross-site Scripting (XSS) - Stored
team_handle: brave
created_at: '2019-08-25T12:34:31.859Z'
disclosed_at: '2019-09-24T20:30:52.095Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 122
asset_identifier: https://laptop-updates.brave.com/latest/winx64
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in localhost:* via integrated torrent downloader

## Metadata

- HackerOne Report ID: 681617
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: brave
- Disclosed At: 2019-09-24T20:30:52.095Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Due to filename of downloading torrent file isn't sanitized, an attacker is able to execute arbitrary JavaScript on localhost:* by abusing crafted torrent file.

## Products affected: 

 * Brave 0.68.131 Chromium: 76.0.3809.100 (Official Build)

## Steps To Reproduce:

 1. Open https://exec.ga/browser/brave/xss.torrent in Brave Browser.
 1. Click "Start Torrent" button
 1. Copy link address of "Save File" button.
 1. Paste it to URL bar with only hostname and port (e.g. http://localhost:8080).
 1. Alert will be popped up.

**Note**: Since it can be embedded with iframe (and it's possible to brute force port number), Steps after 2 won't be needed in real attack.

## Video PoC
{F565161}

## Impact

Attacker will be able to store arbitrary JavaScript on localhost:* with service worker, so if victim run any software on same port after attack, any information in the website that on same port can be stolen.

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
