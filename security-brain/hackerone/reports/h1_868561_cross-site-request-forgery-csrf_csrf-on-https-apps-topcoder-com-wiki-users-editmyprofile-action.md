---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '868561'
original_report_id: '868561'
title: CSRF on https://apps.topcoder.com/wiki/users/editmyprofile.action
weakness: Cross-Site Request Forgery (CSRF)
team_handle: topcoder
created_at: '2020-05-07T22:30:08.048Z'
disclosed_at: '2020-05-12T13:36:42.153Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: apps.topcoder.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF on https://apps.topcoder.com/wiki/users/editmyprofile.action

## Metadata

- HackerOne Report ID: 868561
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: topcoder
- Disclosed At: 2020-05-12T13:36:42.153Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi :) There is a CSRF on changing user details.

## Steps To Reproduce:
There is no CSRF token or anything like that on https://apps.topcoder.com/wiki/users/editmyprofile.action . I added the poc html file below. When someone opens this html file, or we can add it into our website, victim's name and information will change.

Note: This only works to signed-in users. Because unauthorized users cannot upload attachments. There is a mistake on https://apps.topcoder.com/wiki/login.action now. If you encounter an error, you can login on main site (https://accounts.topcoder.com/member) then try.

## Impact

An attacker can force other users to change their name and  informations without their knowledge.

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
