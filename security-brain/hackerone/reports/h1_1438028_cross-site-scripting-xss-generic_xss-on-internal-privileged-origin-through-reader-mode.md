---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1438028'
original_report_id: '1438028'
title: 'XSS on internal: privileged origin through reader mode'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: brave
created_at: '2021-12-30T07:48:36.834Z'
disclosed_at: '2023-06-22T05:51:13.868Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: https://github.com/brave/brave-ios
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on internal: privileged origin through reader mode

## Metadata

- HackerOne Report ID: 1438028
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: brave
- Disclosed At: 2023-06-22T05:51:13.868Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Brave iOS has two weaknesses described below. By combining them, XSS can be achieved on the privileged origin `internal://local`.

1. Exposure of uuidKey through REFERER header
Reader mode in Brave has two HTML templates, [Reader.html](https://github.com/brave/brave-ios/blob/development/Client/Frontend/Reader/Reader.html) and [ReaderViewLoading.html](https://github.com/brave/brave-ios/blob/development/Client/Frontend/Reader/ReaderViewLoading.html). The former template defines [<meta name="referrer" content="never">](https://github.com/brave/brave-ios/blob/development/Client/Frontend/Reader/Reader.html#L10) header for preventing referrer leakage, but the latter template [does not](https://github.com/brave/brave-ios/blob/development/Client/Frontend/Reader/ReaderViewLoading.html#L8). Therefore, by opening an external page through `ReaderViewLoading.html`, the `uuidKey` contained in the Reader mode page URL is leaked.

2. XSS in SessionRestoreHandler
SessionRestoreHandler is used to restore a previously used tab, but [it does not validate an URL to be restored](https://github.com/brave/brave-ios/blob/83eb41ac922d7bd18fd311e0a4279e02cdd8e190/Client/Frontend/Browser/SessionRestoreHandler.swift#L34). Therefore, if a javascript: URL is provided, the code is executed on the `internal:` domain.

Note that the first vulnerability is not reproduced on iOS 15 because WKWebView's referrer policy has been changed to hostname only. However, according to [Apple's report in June 2021](https://developer.apple.com/support/app-store/), more than 90% of users were using iOS 14.

## Products affected: 

* Brave iOS 1.32.3 and higher (include the latest Nightly) on iOS 14.x and below

## Steps To Reproduce:

* Visit https://csrf.jp/brave/reader_uuid_leakage.php
* Open the page in Reader mode
* Long tap a hyperlink in the page and choose "Open in New Private Tab"
* Wait for several seconds and tap "Load original page"
* uuidKey in the reader mode URL is stolen through REFERER header
* Click an exploit URL in the page, then XSS is triggered on `internal://local`

## Supporting Material/References:

* xss_on_internal_origin_through_reader_mode.mov: video of the attack against the vulnerabilities
* reader_uuid_leakage.php: server-side exploit code

## Impact

* Attacker can elevate privileges to `internal:` origin

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
