---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '868572'
original_report_id: '868572'
title: CSRF on https://apps.topcoder.com/wiki/users/editmyprofilepicture.action
weakness: Cross-Site Request Forgery (CSRF)
team_handle: topcoder
created_at: '2020-05-07T22:57:10.893Z'
disclosed_at: '2020-12-14T16:00:02.165Z'
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

# CSRF on https://apps.topcoder.com/wiki/users/editmyprofilepicture.action

## Metadata

- HackerOne Report ID: 868572
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: topcoder
- Disclosed At: 2020-12-14T16:00:02.165Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi :) There is a CSRF on uploading user profile photo and saving it.

## Steps To Reproduce:
There is no CSRF token or anything like that on https://apps.topcoder.com/wiki/users/editmyprofilepicture.action . I added the poc html files below. Attacker can upload a new profile photo and update victim's profil photo.

Note: This only works to signed-in users. Because unauthorized users cannot upload attachments. There is a mistake on https://apps.topcoder.com/wiki/login.action now. If you encounter an error, you can login on main site (https://accounts.topcoder.com/member) then try.

## Impact

An attacker can force other users to change their profile pictures without their knowledge.

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
