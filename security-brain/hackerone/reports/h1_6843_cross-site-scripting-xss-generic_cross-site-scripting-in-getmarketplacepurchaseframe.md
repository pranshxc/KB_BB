---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6843'
original_report_id: '6843'
title: Cross-Site Scripting in getMarketplacePurchaseFrame
weakness: Cross-site Scripting (XSS) - Generic
team_handle: concretecms
created_at: '2014-04-10T17:43:20.563Z'
disclosed_at: '2014-08-18T16:56:20.902Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross-Site Scripting in getMarketplacePurchaseFrame

## Metadata

- HackerOne Report ID: 6843
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: concretecms
- Disclosed At: 2014-08-18T16:56:20.902Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The `$mp->getProductBlockID()` variable in the `getMarketplacePurchaseFrame` function ([view on Github](https://github.com/concrete5/concrete5/blob/851806af393fa2958d52db9b48e0a8c83100f609/web/concrete/core/libraries/marketplace.php#L176)) is not being filtered properly to protect against HTML injection/XSS.

This leads to XSS vulnerabilities in (for example) `connect.php` on line 14 ([view on Github](https://github.com/concrete5/concrete5/blob/851806af393fa2958d52db9b48e0a8c83100f609/web/concrete/single_pages/dashboard/extend/connect.php#L14)) when visiting a URL like: *dashboard/extend/connect/"%20onmouseover="alert(document.cookie)">*.

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
