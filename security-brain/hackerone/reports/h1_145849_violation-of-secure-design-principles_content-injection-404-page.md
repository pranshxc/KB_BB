---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145849'
original_report_id: '145849'
title: Content Injection 404 page
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2016-06-19T12:17:22.540Z'
disclosed_at: '2016-06-19T12:22:53.194Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content Injection 404 page

## Metadata

- HackerOne Report ID: 145849
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2016-06-19T12:22:53.194Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there,

Similar as report #145344 and #145532 it's possbile to spoof the 404 page using http.

PoC URL: http://nextcloud.com/has%2f%20been%20changed%20to%20https://www.ATTACKER.COM.%20so%20please%20visit%20https://www.ATTACKER.COM%20as%20your%20requested%20link

Note: If this redirects you to https, clear the cache or use another browser.

If you need more information, let me know.

Thanks!

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
