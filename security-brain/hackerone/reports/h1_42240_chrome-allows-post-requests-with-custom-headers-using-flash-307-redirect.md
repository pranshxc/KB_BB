---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '42240'
original_report_id: '42240'
title: chrome allows POST requests with custom headers using flash + 307 redirect
team_handle: ibb
created_at: '2014-12-31T20:18:20.632Z'
disclosed_at: '2015-02-09T08:03:32.414Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# chrome allows POST requests with custom headers using flash + 307 redirect

## Metadata

- HackerOne Report ID: 42240
- Weakness: 
- Program: ibb
- Disclosed At: 2015-02-09T08:03:32.414Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

well, It was reported directly to google(as It affected specially chrome) https://code.google.com/p/chromium/issues/detail?id=332023 . This vulnerability allowed post request with custom headers be sent to any websites(not respecting same origin policy) which chrome was mainly affected. Don't know if adobe made any code change due to this report and either if this program covers this kind of vulnerabilities, but i'm reporting it anyway.

wonder if this could be eligible for bug bounty ?

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
