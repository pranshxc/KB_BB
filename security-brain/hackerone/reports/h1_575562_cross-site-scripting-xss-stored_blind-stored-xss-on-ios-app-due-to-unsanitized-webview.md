---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '575562'
original_report_id: '575562'
title: Blind Stored XSS on iOS App due to Unsanitized Webview
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nextcloud
created_at: '2019-05-09T17:15:08.282Z'
disclosed_at: '2020-03-07T21:54:57.092Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: it.twsweb.Nextcloud
asset_type: APPLE_STORE_APP_ID
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Blind Stored XSS on iOS App due to Unsanitized Webview

## Metadata

- HackerOne Report ID: 575562
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nextcloud
- Disclosed At: 2020-03-07T21:54:57.092Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team!

I found a Blind XSS can executed on iOS App due to unsanitized webview. Using this issue, attacker can extract information from victim.

##Steps To Reproduce:
1. Upload malicious HTML, share to victim
2. Waiting victim to open it

{F487447}

{F487448}

HTML payload attached, don't forget to change IP Address to yours.

**Recomendation:** Disabling Javascript on Webview
**Reference:**
https://developer.apple.com/documentation/webkit/wkpreferences#//apple_ref/occ/instp/WKPreferences/javaScriptEnabled

## Impact

In this PoC, attacker can extract information from victim such as IP Address, Location, OS.

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
