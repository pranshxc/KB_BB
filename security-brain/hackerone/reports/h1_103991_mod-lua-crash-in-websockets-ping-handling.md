---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '103991'
original_report_id: '103991'
title: 'mod_lua: Crash in websockets PING handling'
team_handle: ibb
created_at: '2015-01-28T00:00:00.000Z'
disclosed_at: '2015-02-04T00:00:00.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: Apache (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# mod_lua: Crash in websockets PING handling

## Metadata

- HackerOne Report ID: 103991
- Weakness: 
- Program: ibb
- Disclosed At: 2015-02-04T00:00:00.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A stack recursion crash in the mod_lua module was found. A Lua script executing the r:wsupgrade() function could crash the process if a malicious client sent a carefully crafted PING request. This issue affected releases 2.4.7 through 2.4.12 inclusive.

https://httpd.apache.org/security/vulnerabilities_24.html

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
