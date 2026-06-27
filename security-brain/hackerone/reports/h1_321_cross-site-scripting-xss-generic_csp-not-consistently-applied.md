---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '321'
original_report_id: '321'
title: CSP not consistently applied
weakness: Cross-site Scripting (XSS) - Generic
team_handle: security
created_at: '2013-11-08T09:59:03.704Z'
disclosed_at: '2013-11-30T01:10:30.353Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# CSP not consistently applied

## Metadata

- HackerOne Report ID: 321
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: security
- Disclosed At: 2013-11-30T01:10:30.353Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Also thought I'd formally submitted the issue we discussed yesterday, that sometimes the CSP response headers served are missing for browsers that don't support them, but then the page without these headers can be cached by Cloudflare. This makes it easier to mount a XSS attack.

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
