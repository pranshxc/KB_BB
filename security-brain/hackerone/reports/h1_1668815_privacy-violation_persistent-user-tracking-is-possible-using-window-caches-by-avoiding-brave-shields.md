---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1668815'
original_report_id: '1668815'
title: Persistent user tracking is possible using window.caches, by avoiding Brave
  Shields
weakness: Privacy Violation
team_handle: brave
created_at: '2022-08-14T10:27:27.362Z'
disclosed_at: '2023-06-22T05:50:50.921Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: https://github.com/brave/brave-ios
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
- privacy-violation
---

# Persistent user tracking is possible using window.caches, by avoiding Brave Shields

## Metadata

- HackerOne Report ID: 1668815
- Weakness: Privacy Violation
- Program: brave
- Disclosed At: 2023-06-22T05:50:50.921Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

The recent version of iOS 15 introduced `window.caches` in WKWebView. It provides a persistent cache for web pages, and is also potentially usable for user tracking.
The current [CookieControl.js](https://github.com/brave/brave-ios/blob/development/Client/Frontend/UserContent/UserScripts/CookieControl.js) disables cookie, localStorage and sessionStorage, but it doesn't disable `window.caches`, so it allows client-side user tracking by `window.caches` even when cookie brocker is enabled.

## Products affected: 

* Brave for iOS Version 1.41.1 (22.7.27.20)
* iPhone 8 with iOS 15.6

## Steps To Reproduce:

* Enable Brave Shields and block all cookies
* Visit https://csrf.jp/2022/caches.php
* Push "Set Tracking ID" button, then your tracking ID is set to window.caches
* Push "Get Tracking ID" button, then you can confirm your tracking ID that was set above
* Close your browser and visit the above page again
* Push "Get Tracking ID" button, then you can see your tracking ID again

## Supporting Material/References:

  * Attached is a movie file that demonstrate the above steps to reproduce.

## Impact

As witten in summary, client-side user tracking by `window.caches` is possible even when cookie brocker is enabled.

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
