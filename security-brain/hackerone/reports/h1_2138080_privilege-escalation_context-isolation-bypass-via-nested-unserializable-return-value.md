---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2138080'
original_report_id: '2138080'
title: Context isolation bypass via nested unserializable return value
weakness: Privilege Escalation
team_handle: ibb
created_at: '2023-09-06T16:53:57.092Z'
disclosed_at: '2023-10-07T19:47:54.905Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: https://github.com/Electron
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Context isolation bypass via nested unserializable return value

## Metadata

- HackerOne Report ID: 2138080
- Weakness: Privilege Escalation
- Program: ibb
- Disclosed At: 2023-10-07T19:47:54.905Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This issue is exploitable under either of two conditions:

* If an API exposed to the main world via contextBridge can return an object or array that contains a JS object which cannot be serialized, for instance, a canvas rendering context. This would normally result in an exception being thrown `Error: object could not be cloned`.
* If an API exposed to the main world via contextBridge has a return value that throws a user-generated exception while being sent over the bridge, for instance a dynamic getter property on an object that throws an error when being computed.

In both of these cases the context that receives the exception may be able to (via the exception) obtain privileged access to the context on the other side of the bridge.

## Impact

This is a context isolation bypass, meaning that code running in the main world context in the renderer can reach into the isolated Electron context and perform privileged actions.

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
