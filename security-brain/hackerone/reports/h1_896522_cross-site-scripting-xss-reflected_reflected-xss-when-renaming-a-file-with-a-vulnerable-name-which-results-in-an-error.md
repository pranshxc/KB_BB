---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '896522'
original_report_id: '896522'
title: Reflected XSS when renaming a file with a vulnerable name which results in
  an error
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: nextcloud
created_at: '2020-06-12T08:17:47.751Z'
disclosed_at: '2021-03-01T11:02:05.545Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS when renaming a file with a vulnerable name which results in an error

## Metadata

- HackerOne Report ID: 896522
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: nextcloud
- Disclosed At: 2021-03-01T11:02:05.545Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

It looks like Nextcloud team will accept the XSS protected by the CSP. (Report #896511)
Here is another XSS.
1. Rename an existing filename to <img src=x onerror=prompt(1)>.jpg.
2. Anyone tries to rename this <img src=x onerror=prompt(1)>.jpg with an invalid filename, like add a "\" in it, will trigger the XSS attack.
3. Need bypass the CSP.

Thanks

## Impact

Cross-Site Scripting

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
