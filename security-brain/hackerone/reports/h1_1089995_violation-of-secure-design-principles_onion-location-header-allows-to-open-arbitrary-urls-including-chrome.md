---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1089995'
original_report_id: '1089995'
title: 'Onion-Location header allows to open arbitrary URLs including chrome:'
weakness: Violation of Secure Design Principles
team_handle: brave
created_at: '2021-01-29T02:51:18.210Z'
disclosed_at: '2023-06-22T05:52:04.648Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
asset_identifier: https://github.com/brave/brave-core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Onion-Location header allows to open arbitrary URLs including chrome:

## Metadata

- HackerOne Report ID: 1089995
- Weakness: Violation of Secure Design Principles
- Program: brave
- Disclosed At: 2023-06-22T05:52:04.648Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

This [PR](https://github.com/brave/brave-core/pull/6762) introduced "Open in Tor" feature that can open .onion URLs offered through `Onion-Location` response header, but `Onion-Location` header allows to open arbitrary URLs such as `javascript:` and `chrome:`.
This behavior can be exploited as a way to bypass SOP and gain access to privileged URLs.

## Products affected: 

* Brave Nightly for OSX (1.21.28 Chromium: 88.0.4324.96 (Official Build) nightly (x86_64))

## Steps To Reproduce:

* Open https://csrf.jp/brave/onion.php
* Click "Open in Tor" button shown in the Brave's address bar
* Privileged URL `chrome://restart/` is opened, and Brave is restarted.

If a user enabled "Automatically redirect .onion sites" in the settings, `chrome://restart/` is opened automatically and Brave continues to restart endlessly.

## Supporting Material/References:

PoC code in PHP is below

   ```
<?php
header("Onion-Location: chrome://restart/");
?>
   ```

## Impact

As written in the summary, attacker can bypass SOP restrictions and gain access to privileged URLs.

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
