---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '377206'
original_report_id: '377206'
title: '`settingcontent-ms` files lacks "mark of the web" => execute code by dbl click
  in Downloads toolbar'
team_handle: brave
created_at: '2018-07-04T19:36:14.482Z'
disclosed_at: '2018-10-04T00:52:46.884Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
asset_identifier: https://github.com/brave/muon
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
---

# `settingcontent-ms` files lacks "mark of the web" => execute code by dbl click in Downloads toolbar

## Metadata

- HackerOne Report ID: 377206
- Weakness: 
- Program: brave
- Disclosed At: 2018-10-04T00:52:46.884Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:

`settingcontent-ms` files allow launching any binary with any params.
Brave doesn't mark `settingcontent-ms` files with "mark of the web", so the file could be executed by double click in "Downloads" toolbar. Launched `settingcontent-ms` file could lead to code execution with user-level privileges. 

## Products affected: 
Brave: 0.23.19
Muon: 7.1.3
OS: 10.0.17134 (the image was downloaded today from the MS virtualbox images page)
Chromium: 67.0.3396

## Steps To Reproduce:

1. Download `twitter.settingcontent-ms` from attachments.
2. Dbl click on the item in "Downloads" toolbar.
3. Calculator opens (but as I said, it's possible to launch anything).

PoC/Screencast additionally leverages #375259.

## Supporting Material/References:

1. FF patched this somewhere between 60-62 version
2. This bug still works in Edge. As far as I know, that's 1-day.
3. Chrome downloads `settingcontent-ms` files only after a confirmation from the user.
4. This problem is already popular, so you could easily find more info.

PoC + screencast attached.
[Live PoC:](https://win-settingcontent-ms-uosardvltp.now.sh)  (not sure that it works, it'd be better to test it locally)

## Impact

Launched `settingcontent-ms` could lead to code execution with user-level privileges. 
Marked as "high", because it's a native OS feature, all Win users are affected.

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
