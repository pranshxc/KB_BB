---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '409850'
original_report_id: '409850'
title: XSS in steam react chat client
weakness: Cross-site Scripting (XSS) - Stored
team_handle: valve
created_at: '2018-09-14T17:20:41.901Z'
disclosed_at: '2019-01-07T20:00:19.267Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 462
asset_identifier: steamcommunity.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS in steam react chat client

## Metadata

- HackerOne Report ID: 409850
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: valve
- Disclosed At: 2019-01-07T20:00:19.267Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The Steam chat client both sends and receives bbcode format chat messages. These map to HTML elements, and notably the [url] bbcode tag is supported for arbitrary URLs. React has strong XSS mitigations but does not mitigate `javascript:` URI based XSS.

This is rather difficult to exploit as the client transmits sanitised messages and receives over a binary WebSocket. I've attached a video of executing this XSS, which is persistent.

## Impact

I strongly believe an attacker could get remote code execution in Steam via this method. The Steam chat client uses the same codebase as the steam web chat client, and, I imagine does so using electron or some other webview system. These systems all expose functions which allow arbitrary calls to system to allow them to be competitive with e.g. windows forms.

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
