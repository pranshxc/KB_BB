---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1519099'
original_report_id: '1519099'
title: Renderers can obtain access to random bluetooth device without permission
weakness: Improper Access Control - Generic
team_handle: ibb
created_at: '2022-03-22T18:27:19.473Z'
disclosed_at: '2022-04-23T17:23:03.981Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: https://github.com/Electron
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Renderers can obtain access to random bluetooth device without permission

## Metadata

- HackerOne Report ID: 1519099
- Weakness: Improper Access Control - Generic
- Program: ibb
- Disclosed At: 2022-04-23T17:23:03.981Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

With the default configuration in Electron, renderer processes (which should not have access to system resources by default) can gain read/write access to a nearby bluetooth device. To reproduce:

* Run the electron-quick-start app with a vulnerable version of Electron: https://github.com/electron/electron-quick-start
* Using the developer tools, run `await navigator.bluetooth.requestDevice({acceptAllDevices: true})`
* You should get a permission error, but in vulnerable versions you will get a bluetooth device object instead.

## Impact

If an Electron app loads remote or untrusted content in a renderer process (which is normally fine, as the process should not have any privileges), the remote content would have read/write access to nearby bluetooth devices. The impact would then depend on what devices the user has nearby.

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
