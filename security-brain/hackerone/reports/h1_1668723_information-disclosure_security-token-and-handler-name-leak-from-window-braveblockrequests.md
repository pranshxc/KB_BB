---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1668723'
original_report_id: '1668723'
title: Security token and handler name leak from window.braveBlockRequests
weakness: Information Disclosure
team_handle: brave
created_at: '2022-08-14T05:32:51.972Z'
disclosed_at: '2023-06-22T05:51:03.326Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: https://github.com/brave/brave-ios
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
- information-disclosure
---

# Security token and handler name leak from window.braveBlockRequests

## Metadata

- HackerOne Report ID: 1668723
- Weakness: Information Disclosure
- Program: brave
- Disclosed At: 2023-06-22T05:51:03.326Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Brave for iOS protects privileged JS to native bridges by using random JavaScript handler names and security tokens.
However, by altering [window.braveBlockRequests](https://github.com/brave/brave-ios/blob/08fb4b0ca43625d706b96158267f0b8da6f63250/Client/Frontend/UserContent/UserScripts/RequestBlocking.js#L6) property from scripts on the web page, these secret values can be stolen.

To be specific, `braveBlockRequests` property is set after the execution of the script on the page. Thus, by setting the malicious property as an immutable property from the page beforehand as shown below, it is possible to prevent overwriting by the legitimate property.
```
Object.defineProperty(window, "braveBlockRequests", {
    enumerable: false,
    configurable: false,
    writable: false,
    value: function(args) { window.args = args } // Steal handler name and token here
});
```

## Products affected: 

* Brave for iOS Version 1.41.1 (22.7.27.20) with the default settings

## Steps To Reproduce:

* Open https://csrf.jp/2022/brave_token_leak.php
* Push "Attack" button in the page
* Secret handler name and security token is shown on the page

## Supporting Material/References:

* Attached is a movie file that demonstrate the above steps to reproduce.

## Impact

The impact depends on which bridge is abused. As further features are implemented in the Brave, its potential risk tends to be increased.

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
