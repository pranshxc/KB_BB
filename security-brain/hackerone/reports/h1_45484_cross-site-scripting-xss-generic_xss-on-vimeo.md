---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '45484'
original_report_id: '45484'
title: XSS on Vimeo
weakness: Cross-site Scripting (XSS) - Generic
team_handle: vimeo
created_at: '2015-01-28T06:05:28.660Z'
disclosed_at: '2015-01-29T00:16:26.664Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on Vimeo

## Metadata

- HackerOne Report ID: 45484
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: vimeo
- Disclosed At: 2015-01-29T00:16:26.664Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Poc video:
XSS on Vimeo: http://youtu.be/w5QgEEcMARY

1. Go to https://vimeo.com/settings/profile
2. Add a link with the payload on URL: javascript:alert(document.domain+"http://")
3. Click the link and payload will execute.

Thanks
@niyaax

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
