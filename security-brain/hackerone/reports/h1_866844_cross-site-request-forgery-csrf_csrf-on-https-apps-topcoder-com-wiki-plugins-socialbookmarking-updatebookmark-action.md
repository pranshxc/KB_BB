---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '866844'
original_report_id: '866844'
title: CSRF on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action
weakness: Cross-Site Request Forgery (CSRF)
team_handle: topcoder
created_at: '2020-05-05T23:02:01.775Z'
disclosed_at: '2020-05-12T13:37:58.750Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: apps.topcoder.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action

## Metadata

- HackerOne Report ID: 866844
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: topcoder
- Disclosed At: 2020-05-12T13:37:58.750Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi :) There is a CSRF on creating bookmarks form.

## Steps To Reproduce:

There is no CSRF token or anything like that on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action. I added the poc html file below. When someone opens this html file, or we can add it into our website, he/she creates a bookmark unwillingly.

## Impact

An attacker can force other users to create a bookmark without their knowledge.

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
