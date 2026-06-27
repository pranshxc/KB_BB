---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '866861'
original_report_id: '866861'
title: Reflected XSS on error page on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: topcoder
created_at: '2020-05-05T23:40:24.691Z'
disclosed_at: '2020-05-12T13:40:50.564Z'
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

# Reflected XSS on error page on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action

## Metadata

- HackerOne Report ID: 866861
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: topcoder
- Disclosed At: 2020-05-12T13:40:50.564Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi :) 
In https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action `bookmarkPageId` parameter expects a number value. If you add XSS payload instead of number, an error page displays with XSS.

PoC
`https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action?bookmarkPageId="><img src=x onerror=alert(document.domain)>`
{F816846}

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
