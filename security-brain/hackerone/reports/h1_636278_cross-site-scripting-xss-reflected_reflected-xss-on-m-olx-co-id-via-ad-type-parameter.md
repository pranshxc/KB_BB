---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '636278'
original_report_id: '636278'
title: Reflected XSS on m.olx.co.id via ad_type parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: olx
created_at: '2019-07-05T08:34:49.794Z'
disclosed_at: '2019-11-03T18:32:50.521Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on m.olx.co.id via ad_type parameter

## Metadata

- HackerOne Report ID: 636278
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: olx
- Disclosed At: 2019-11-03T18:32:50.521Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I have identified a Reflected Cross Site Scripting (XSS) vulnerability on the m.olx.co.id website.

Vulnerable URL: https://m.olx.co.id/iklan/zundapp-1962-cafe-racer-250-cc-made-in-germany-IDA3GpU.html?ad_type=PL"><svg/onload=alert("XSS")><"

Vulnerable Parameter: ad_type

XSS Payload: PL"><svg/onload=alert("XSS")><"

Steps to replicate is fairly simple. Just access the URL and the JavaScript gets reflected in response and gets executed on the browser. The Popup screenshot attached.

Note: This seems similar to my other report: https://hackerone.com/reports/633751 just that the domain is different (m.olx.co.id).

Let me know if any further help is required from my side.

## Impact

1. Redirect user to malicious website like phishing website etc.
2. Rewrite the content of the current HTML page which can result in Brand Abuse.

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
