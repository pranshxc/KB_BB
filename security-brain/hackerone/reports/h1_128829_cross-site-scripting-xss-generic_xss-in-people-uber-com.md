---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '128829'
original_report_id: '128829'
title: XSS in people.uber.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-05-24T19:33:25.885Z'
disclosed_at: '2016-07-26T00:55:27.387Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in people.uber.com

## Metadata

- HackerOne Report ID: 128829
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-07-26T00:55:27.387Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

From the HTML source code of http://people.uber.com I came to know that it uses Yoast WordPress SEO plugin v2.1.1

But it is known to suffer from XSS bug.

Check it for more details and steps:
https://wpvulndb.com/vulnerabilities/8045

Bug can be easily fixed upgrading the plugin.

Thanks.

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
