---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1436558'
original_report_id: '1436558'
title: Universal XSS with Playlist feature
weakness: Cross-site Scripting (XSS) - Stored
team_handle: brave
created_at: '2021-12-27T10:44:49.508Z'
disclosed_at: '2023-06-22T05:51:24.392Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: https://github.com/brave/brave-ios
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Universal XSS with Playlist feature

## Metadata

- HackerOne Report ID: 1436558
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: brave
- Disclosed At: 2023-06-22T05:51:24.392Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Brave iOS has three weaknesses described below. By combining them, Universal XSS can be achieved.

1. Exposure of UserScriptManager.securityToken
[Playlist.js](https://github.com/brave/brave-ios/blob/fdff99ca3997816322015fe5efcd63490193b88d/Client/Frontend/UserContent/UserScripts/Playlist.js#L353) embeds the exact value of the `$<notifyNode>` into `HTMLVideoElement.prototype.setAttribute`. By reading the value, an attacker can retrieve the hidden security token.

2. Exposure of UserScriptManager.messageHandlerToken
Also, [WindowRenderHelper.js](https://github.com/brave/brave-ios/blob/83eb41ac922d7bd18fd311e0a4279e02cdd8e190/Client/Frontend/UserContent/UserScripts/WindowRenderHelper.js#L12) embeds the exact value of the `$<handler>` into `W{securityToken}.postMessage`. By reading the value, an attacker can retrieve the hidden message handler token.

3. UXSS in PlaylistHelper through nodeTag
[PlaylistHelper.swift](https://github.com/brave/brave-ios/blob/83eb41ac922d7bd18fd311e0a4279e02cdd8e190/Client/Frontend/Browser/PlaylistHelper.swift#L228) concatenates strings to build a JavaScript code and executes it on the mainframe of a WebView. Then, `nodeTag` given from a webpage is directly included in the code. So, if the `nodeTag`, named as `tagId` in JS world, passed from the page contained `');alert(document.location);//`, unintended `alert()` is executed on the mainframe.

## Products affected: 

 * Brave iOS 1.32.3 and higher (include the latest Nightly)

## Steps To Reproduce:

 * Visit the Google page: https://sites.google.com/view/nishimunea-brave-uxss1/page
* This page contains a cross origin malicious page https://csrf.jp/brave/playlist.php in an iframe
* The iframe exploits the above three weaknesses to send a message to playlistHelper
* Push `Add to Brave Playlist` and `Open` button in the setting menu
* An alert dialog is appear on the sites.google.com

## Supporting Material/References:

  * Demonstration movie is attached

## Impact

* Universal XSS on the arbitrary domains

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
