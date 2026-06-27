---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '361957'
original_report_id: '361957'
title: Unsanitized input in email field
weakness: Cross-site Scripting (XSS) - Stored
team_handle: vanilla
created_at: '2018-06-05T02:55:26.228Z'
disclosed_at: '2018-09-27T07:15:06.470Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
asset_identifier: '*.vanillaforums.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Unsanitized input in email field

## Metadata

- HackerOne Report ID: 361957
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: vanilla
- Disclosed At: 2018-09-27T07:15:06.470Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Users are able to inject javascript payloads in the email field which leads to stored XSS

Steps to produce :
1. Go to profile and add  "<script>alert(1)</script>"@example.com as your email .
2. We can see the popup at https://discuss.paytm.com/profile/preferences/profilename

## Impact

Users can store malicious payloads and ask any moderator to review their profile and popup will be executed leading to cookie theft and other attacks.

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
