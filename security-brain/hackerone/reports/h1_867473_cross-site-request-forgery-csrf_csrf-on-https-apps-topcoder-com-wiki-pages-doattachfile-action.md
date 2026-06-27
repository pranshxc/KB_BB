---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '867473'
original_report_id: '867473'
title: CSRF on https://apps.topcoder.com/wiki/pages/doattachfile.action
weakness: Cross-Site Request Forgery (CSRF)
team_handle: topcoder
created_at: '2020-05-06T22:53:20.880Z'
disclosed_at: '2020-12-14T15:59:34.972Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: apps.topcoder.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF on https://apps.topcoder.com/wiki/pages/doattachfile.action

## Metadata

- HackerOne Report ID: 867473
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: topcoder
- Disclosed At: 2020-12-14T15:59:34.972Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi :) There is a CSRF on attaching files to wiki pages.

## Steps To Reproduce:
There is no CSRF token or anything like that on https://apps.topcoder.com/wiki/pages/doattachfile.action?pageId= . I added the poc html file below. When someone opens this html file, or we can add it into our website, he/she creates an attachment unwillingly.

This file creates csrf.txt on https://apps.topcoder.com/wiki/pages/doattachfile.action?pageId=165871793

Note: This only works to signed-in users. Because unauthorized users cannot upload attachments. There is a mistake on https://apps.topcoder.com/wiki/login.action now. If you encounter an error, you can login on main site (https://accounts.topcoder.com/member) then try.

## Impact

An attacker can force other users to upload files without their knowledge.

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
