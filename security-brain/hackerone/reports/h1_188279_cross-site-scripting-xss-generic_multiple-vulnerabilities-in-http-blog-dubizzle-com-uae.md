---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '188279'
original_report_id: '188279'
title: Multiple vulnerabilities in http://blog.dubizzle.com/uae
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-12-04T21:03:20.668Z'
disclosed_at: '2017-02-14T13:05:30.168Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Multiple vulnerabilities in http://blog.dubizzle.com/uae

## Metadata

- HackerOne Report ID: 188279
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2017-02-14T13:05:30.168Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

http://blog.dubizzle.com/uae/ uses outdated Yoast Seo plugin which has following vulnerabilities:
[!] Title: Yoast SEO <= 3.2.4 - Subscriber Settings Sensitive Data Exposure
    Reference: https://wpvulndb.com/vulnerabilities/8487

[!] Title: Yoast SEO <= 3.2.5 - Unspecified Cross-Site Scripting (XSS)
    Reference: https://wpvulndb.com/vulnerabilities/8569

[!] Title: Yoast SEO <= 3.4.0 - Authenticated Stored Cross-Site Scripting (XSS)
    Reference: https://wpvulndb.com/vulnerabilities/8583

Update the Yoast SEO plugin to fix the issues.

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
