---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2211561'
original_report_id: '2211561'
title: Self XSS when pasting HTML into Text app with Ctrl+Shift+V
weakness: Cross-site Scripting (XSS) - DOM
team_handle: nextcloud
created_at: '2023-10-16T15:13:18.693Z'
disclosed_at: '2023-12-21T05:24:53.202Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
asset_identifier: nextcloud/text
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Self XSS when pasting HTML into Text app with Ctrl+Shift+V

## Metadata

- HackerOne Report ID: 2211561
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: nextcloud
- Disclosed At: 2023-12-21T05:24:53.202Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
ctrl-shift-v is meant to paste plaintext as is. However it will paste it into a dom elements `innerHtml` and can thus be used to inject malicious html.

## Steps To Reproduce:

  1. copy "<h1>html</h1>"
  1. use ctrl-shift-v to paste it into a .md file
  1. See the heading getting added.

## Supporting Material/References:
https://github.com/nextcloud/text/blob/main/src/extensions/Markdown.js#L97

  * [attachment / reference]

## Impact

If you can trick someone into using ctrl-shift-v to paste content you control you can insert html into the page leading to a possible xss attack.

The html will be inserted into the editors schema - but before that happens it's already pasted into the innerHtml of a dom element.

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
