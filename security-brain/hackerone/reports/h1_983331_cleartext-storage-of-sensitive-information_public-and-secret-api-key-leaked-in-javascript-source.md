---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '983331'
original_report_id: '983331'
title: Public and secret api key leaked  in JavaScript source
weakness: Cleartext Storage of Sensitive Information
team_handle: stripo
created_at: '2020-09-16T10:26:21.957Z'
disclosed_at: '2020-09-29T11:31:14.110Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 136
asset_identifier: stripo.email
asset_type: URL
max_severity: medium
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Public and secret api key leaked  in JavaScript source

## Metadata

- HackerOne Report ID: 983331
- Weakness: Cleartext Storage of Sensitive Information
- Program: stripo
- Disclosed At: 2020-09-29T11:31:14.110Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** [Summary the vulnerabilities]
I am surfing on the stripo website. I found a sensitive data including authentication key written in public accessible javascript file.

**URL Vulnerability**
https://staging.empleio.stripo.email/main.c1965c58f39a0f4aadc3.js

###Steps To Reproduce:
  * Open staging.empleio.stripo.email and add payloads javascript-fuzz
  * Directory sensitive is ``main.c1965c58f39a0f4aadc3.js`` parse this json files using jsonparseronline
  * and look response bytes In response you can see Sensitive ApiKey Disclosure
  * Sensitive Information has been leaked on this source page ``main.c1965c58f39a0f4aadc3.js``
  * Open your network browser , this javascript source has high files can leads to (DoS)

**Proof On Concept**
```javascript
projectId: null,
userFullName: null,
unSubscribeLink: null,
viewInBrowserLink: null,
initialTab: i.TAB_NAME_CONTENT,
aviaryApiKey: "████████",
youtubeApiKey: "███████",
onChangeFromCodeEditor: null,
onSaveEmail: null,
onSaveTemplate: null,
onUnauthorized: function(e)
```
**Screenshots Proof**
F989906
F989907

## Impact

Information Disclosure & DoS json files

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
