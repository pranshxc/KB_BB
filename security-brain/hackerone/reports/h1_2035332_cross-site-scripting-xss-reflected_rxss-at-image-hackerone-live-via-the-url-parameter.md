---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2035332'
original_report_id: '2035332'
title: RXSS at image.hackerone.live via the `url` parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: security
created_at: '2023-06-22T23:40:46.844Z'
disclosed_at: '2023-08-11T12:08:01.238Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 155
asset_identifier: hackerone.live
asset_type: URL
max_severity: low
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# RXSS at image.hackerone.live via the `url` parameter

## Metadata

- HackerOne Report ID: 2035332
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: security
- Disclosed At: 2023-08-11T12:08:01.238Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

good day

https://image.hackerone.live:8443/;/;/resource/md/get/url?url=http://oast.pro


is allowing full read ssrf wirh permission can try for aws creds.

-Eric

## Impact

full read ssrf

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
