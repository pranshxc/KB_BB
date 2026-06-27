---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '390429'
original_report_id: '390429'
title: Reflected XSS on help.steampowered.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: valve
created_at: '2018-08-04T08:13:15.999Z'
disclosed_at: '2019-01-07T20:14:15.601Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: support.steampowered.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on help.steampowered.com

## Metadata

- HackerOne Report ID: 390429
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: valve
- Disclosed At: 2019-01-07T20:14:15.601Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

URL: https://help.steampowered.com/en/wizard/HelpWithGameIssue/?appid=704740&issueid=125&option=%3Ch1%3Eunfiltered

It puts `option` option into a translation token `<div class="help_page_title">#Help_Game_MissingItemsTitle{user controlled string here}`

And if there's no such translation token, it just prints out the entire user input unescaped.

## Impact

XSS.

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
