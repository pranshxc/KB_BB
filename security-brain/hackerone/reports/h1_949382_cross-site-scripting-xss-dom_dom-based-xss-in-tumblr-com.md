---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '949382'
original_report_id: '949382'
title: DOM-Based XSS in tumblr.com
weakness: Cross-site Scripting (XSS) - DOM
team_handle: automattic
created_at: '2020-08-01T20:04:10.345Z'
disclosed_at: '2021-02-02T21:38:45.747Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 56
asset_identifier: www.tumblr.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM-Based XSS in tumblr.com

## Metadata

- HackerOne Report ID: 949382
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: automattic
- Disclosed At: 2021-02-02T21:38:45.747Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Description

Hi, i would like to report DOM-Based XSS that it's exactly like this one #882546, this one work just because  the page /reblog/ID/OTHER_ID doesn't have a correct CSP rule.

# Steps to reproduce
1. go to `https://www.tumblr.com/reblog/620008931446652928/JBuEvzz5`
2. click in `click me`
3. click in open
4. XSS will be triggered

## Impact

it is possible to perform malicious actions on the victim's account

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
