---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '866433'
original_report_id: '866433'
title: Reflected XSS on https://apps.topcoder.com/wiki/page/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: topcoder
created_at: '2020-05-05T13:53:05.387Z'
disclosed_at: '2020-05-12T13:49:07.302Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
asset_identifier: apps.topcoder.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://apps.topcoder.com/wiki/page/

## Metadata

- HackerOne Report ID: 866433
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: topcoder
- Disclosed At: 2020-05-12T13:49:07.302Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Hi :) A reflected XSS occurs on https://apps.topcoder.com/wiki/pages/doeditattachment.action when editing wiki pages attachments.

## Steps To Reproduce:

A user can add attachments on https://apps.topcoder.com/wiki/pages/viewpageattachments.action?pageId=165871793 a wiki page and can edit on https://apps.topcoder.com/wiki/pages/editattachment.action?pageId=165871793&fileName=sss.svg. If there is an error, user redirected to `doeditattachment` path with an error message. An attacker can change the filename parameter and add JS codes. When a victim opens this url, XSS will execute. 

PoC:
https://apps.topcoder.com/wiki/pages/doeditattachment.action?pageId=165871793&fileName=s%22%3E%3Cimg%20src=X%20onerror=alert(document.domain)%3Ess.svg
{F816100}

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
