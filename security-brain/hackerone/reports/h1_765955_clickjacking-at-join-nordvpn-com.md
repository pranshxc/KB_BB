---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '765955'
original_report_id: '765955'
title: Clickjacking at join.nordvpn.com
team_handle: nordsecurity
created_at: '2019-12-30T06:40:58.670Z'
disclosed_at: '2020-02-13T22:24:13.233Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
asset_identifier: '*.nordvpn.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Clickjacking at join.nordvpn.com

## Metadata

- HackerOne Report ID: 765955
- Weakness: 
- Program: nordsecurity
- Disclosed At: 2020-02-13T22:24:13.233Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

PoC at attach

Create a new HTML file
Put <iframe src ="https://join.nordvpn.com" width="500" height="500"></iframe>
Save the file
Open document in browser

## Impact

https://www.owasp.org/index.php/Clickjacking

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
