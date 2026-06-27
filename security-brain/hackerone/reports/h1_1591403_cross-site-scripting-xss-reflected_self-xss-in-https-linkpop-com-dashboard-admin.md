---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1591403'
original_report_id: '1591403'
title: Self XSS in https://linkpop.com/dashboard/admin
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: shopify
created_at: '2022-06-04T21:20:37.884Z'
disclosed_at: '2022-10-13T21:20:37.442Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: linkpop.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Self XSS in https://linkpop.com/dashboard/admin

## Metadata

- HackerOne Report ID: 1591403
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: shopify
- Disclosed At: 2022-10-13T21:20:37.442Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Hello Shopify team,
Found a self XSS  https://linkpop.com/dashboard/admin, the steps to reproduce are below

## Steps To Reproduce:
1- Visit https://linkpop.com/dashboard/admin
2- Click on links => add links
3- add in the url  input `javascript:alert(document.cookie)`
{F1757141}
4- Click on the link that appeared on the phone image and the alert will appear
{F1757140}
{F1757142}

In your policy page you say that you guys accept self xss as long as its two steps, here its only paste payload in input and click on image so hopefully in scope :)

## Impact

Self XSS.

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
