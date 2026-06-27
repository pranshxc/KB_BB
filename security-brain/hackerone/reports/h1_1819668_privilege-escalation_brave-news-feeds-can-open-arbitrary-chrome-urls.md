---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1819668'
original_report_id: '1819668'
title: 'Brave News feeds can open arbitrary chrome: URLs'
weakness: Privilege Escalation
team_handle: brave
created_at: '2023-01-01T08:55:37.027Z'
disclosed_at: '2023-06-22T05:50:08.953Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: https://github.com/brave/brave-core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Brave News feeds can open arbitrary chrome: URLs

## Metadata

- HackerOne Report ID: 1819668
- Weakness: Privilege Escalation
- Program: brave
- Disclosed At: 2023-06-22T05:50:08.953Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
URL link in Brave News feeds can open arbitrary chrome: URLs.
This behavior can be exploited as a way to bypass SOP and gain access to privileged URLs.

## Products affected: 

 * 1.46.144 Chromium: 108.0.5359.128 (Official Build) （x86_64）

## Steps To Reproduce:

 * Open new tab and click customize button
 * Follow https://csrf.jp/brave/rss_chrome.php as a RSS feed of Brave News
 * Reload the tab
 * RSS feeed that name is "Access chrome: URLs" is shown on Brave News
 * Click the feed
 * `chrome://settings/resetProfileSettings?origin=userclick` is opened on the tab

## Supporting Material/References:

  * See the demonstration movie I attached

## Impact

Bypass SOP and gain access to privileged URLs.

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
