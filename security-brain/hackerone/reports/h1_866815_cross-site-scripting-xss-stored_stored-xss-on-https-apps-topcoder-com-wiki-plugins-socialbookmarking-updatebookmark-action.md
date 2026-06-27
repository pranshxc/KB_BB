---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '866815'
original_report_id: '866815'
title: Stored XSS on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action
weakness: Cross-site Scripting (XSS) - Stored
team_handle: topcoder
created_at: '2020-05-05T22:12:43.388Z'
disclosed_at: '2020-05-12T13:47:23.015Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: apps.topcoder.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action

## Metadata

- HackerOne Report ID: 866815
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: topcoder
- Disclosed At: 2020-05-12T13:47:23.015Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi :) Adding javascript url causes to stored XSS when creating bookmark.

## Steps To Reproduce:

Go to https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action . Write `javascript:alert(document.domain)` on url input and fill other areas. After create, go `https://apps.topcoder.com/wiki/display/tcwiki/<TITLE>` and when you click the title on this page, XSS will execute.

PoC:
https://apps.topcoder.com/wiki/display/tcwiki/powerpuff_hackerone_test
{F816754}

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
