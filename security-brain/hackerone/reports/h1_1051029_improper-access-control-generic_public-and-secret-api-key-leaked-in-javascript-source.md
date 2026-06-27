---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1051029'
original_report_id: '1051029'
title: Public and secret api key leaked in JavaScript source
weakness: Improper Access Control - Generic
team_handle: top_echelon_software
created_at: '2020-12-05T06:38:02.522Z'
disclosed_at: '2021-01-19T20:14:30.923Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: www.topechelon.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Public and secret api key leaked in JavaScript source

## Metadata

- HackerOne Report ID: 1051029
- Weakness: Improper Access Control - Generic
- Program: top_echelon_software
- Disclosed At: 2021-01-19T20:14:30.923Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary: [Summary the vulnerabilities]**
I am surfing on the bb3jobboard.topechelon.com website. I found a sensitive data including authentication key written in public accessible javascript file.

**URL Vulnerability**
  * https://bb3jobboard.topechelon.com/#!/search?page=1

###Steps To Reproduce:
  * Open bb3jobboard.topechelon.com and add payloads javascript-fuzz
  * Directory sensitive is ``//job_board.js//`` parse this json files using jsonparseronline
  * and look response bytes In response you can see Sensitive ApiKey Disclosure
  * Sensitive Information has been leaked on this source page job_board.js
  * Open your network browser , this javascript source has high files can leads to (DoS)

**Proof On Concept**
```javascript
}]), angular.module("jb").config(["lkGoogleSettingsProvider", function(e) {
    e.configure({
        apiKey: "██████████",
        clientId: "██████t.apps.googleusercontent.com",
        scopes: ["https://www.googleapis.com/auth/drive.readonly"],
        features: ["MULTISELECT_DISABLED"]
    })
}]), angular.module("jb.factories").factory("BoardSettingsFactory", ["railsResourceFactory", "PathToResourceRoute", function(e, t) {
    var n = e({
        url: t.convert(JBRoutes.jobBoardBoardSettingsPath),
        name: "boardSettings"
    });
```
**Screenshots Proof**
████

## Impact

Information disclosure

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
