---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '378805'
original_report_id: '378805'
title: '`alert()` dialogs on `chrome-extension://` origin (internal pages)'
team_handle: brave
created_at: '2018-07-07T11:43:35.929Z'
disclosed_at: '2018-10-04T00:51:26.567Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 6
asset_identifier: https://github.com/brave/muon
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
---

# `alert()` dialogs on `chrome-extension://` origin (internal pages)

## Metadata

- HackerOne Report ID: 378805
- Weakness: 
- Program: brave
- Disclosed At: 2018-10-04T00:51:26.567Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

## Summary:

Navigation to `chrome-extension` from the web is possible with #378805 (`ftp://` -> `chrome-extension://`).
A blank page is created during navigation to `chrome-extension://` origin. Blank pages have "This page" title.
It's possible to initiate `alert()` with a social-engineering content and "This page" title, that will be displayed on internal pages.

## Products affected: 

Brave: 0.23.31 
V8: 6.7.288.46 
rev: 3148acef36dba0fce89108638bb27927c4937f90 
Muon: 7.1.5 
OS Release: 17.6.0 
Update Channel: Release 
OS Architecture: x64 
OS Platform: macOS 
Node.js: 7.9.0 
Brave Sync: v1.4.2 
libchromiumcontent: 67.0.3396.103

## Steps To Reproduce:

1. Start ftp server (sample ftp server attached, `npm i ftpd && node ftp-server.js`)
2. Open `ftp://localhost:7002/exploit.html`
3. Click "Go to payment settings"
4. Alert dialog with title "This page" will be displayed on `about:preferences#payments` page

> And `ftp://localhost:7002/exploit.html` is blank, non-responsive and can't be reloaded.

> adjust timer in `exploit.html` if it doesn't work

## Impact

An attacker could initiate `alert()` with a social-engineering content and "This page" title, that will be displayed on internal pages.

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
