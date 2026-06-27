---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '866837'
original_report_id: '866837'
title: Post Based Reflected XSS on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: topcoder
created_at: '2020-05-05T22:44:36.793Z'
disclosed_at: '2020-05-12T13:40:05.095Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: apps.topcoder.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Post Based Reflected XSS on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action

## Metadata

- HackerOne Report ID: 866837
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: topcoder
- Disclosed At: 2020-05-12T13:40:05.095Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi :) A post based reflected XSS occurs when creating bookmarks.

## Steps To Reproduce:
`Title` and `Labels` parameters are vulnerable to XSS on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action. This form uses POST request so i added HTML file below. When someone opens this html file, or we can add it into our website, XSS will execute.

{F816815}
{F816816}

## Impact

XSS can use to steal cookies or to run arbitrary code on victim's browser.

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
