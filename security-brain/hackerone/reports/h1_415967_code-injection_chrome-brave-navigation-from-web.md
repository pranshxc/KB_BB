---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '415967'
original_report_id: '415967'
title: chrome://brave navigation from web
weakness: Code Injection
team_handle: brave
created_at: '2018-09-28T22:10:33.055Z'
disclosed_at: '2018-10-23T19:13:25.251Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: https://github.com/brave/browser-laptop
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
- code-injection
---

# chrome://brave navigation from web

## Metadata

- HackerOne Report ID: 415967
- Weakness: Code Injection
- Program: brave
- Disclosed At: 2018-10-23T19:13:25.251Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

It's possible to navigate to the infamous 'chrome://brave' (and all other) privileged page from web, requiring only a single click. This is possible by opening popups with the 'noopener' attribute.

## Products affected: 

 
Brave: 0.24.0 
V8: 6.9.427.23 
rev: f657f15bf7e0e0c50a2b854c6b05edb59bfc556c 
Muon: 8.1.6 
OS Release: 10.0.17134 
Update Channel: Release 
OS Architecture: x64 
OS Platform: Microsoft Windows 
Node.js: 7.9.0 
Brave Sync: v1.4.2 
libchromiumcontent: 69.0.3497.100

## Steps To Reproduce:

1. Host attached PoC from web
2. Click button

## Impact

This is a direct violation of SOP, we can open any URL of which chrome://brave is the worst as it could lead to RCE.

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
