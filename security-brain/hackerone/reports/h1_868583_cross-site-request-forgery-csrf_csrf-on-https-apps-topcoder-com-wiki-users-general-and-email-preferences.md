---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '868583'
original_report_id: '868583'
title: CSRF on https://apps.topcoder.com/wiki/users general and email preferences
weakness: Cross-Site Request Forgery (CSRF)
team_handle: topcoder
created_at: '2020-05-07T23:14:40.286Z'
disclosed_at: '2020-05-12T13:36:14.506Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: apps.topcoder.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF on https://apps.topcoder.com/wiki/users general and email preferences

## Metadata

- HackerOne Report ID: 868583
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: topcoder
- Disclosed At: 2020-05-12T13:36:14.506Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi :) There is a CSRF on setting general and email preferences.

## Steps To Reproduce:
There is no CSRF token or anything like that on https://apps.topcoder.com/wiki/users/editmypreferences.action and  https://apps.topcoder.com/wiki/users/editemailpreferences.action . I added the poc html files below. Attacker can change victim's preferences.

Note: This only works to signed-in users. There is a mistake on https://apps.topcoder.com/wiki/login.action now. If you encounter an error, you can login on main site (https://accounts.topcoder.com/member) then try.

## Impact

An attacker can force other users to change their preferences without their knowledge.

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
