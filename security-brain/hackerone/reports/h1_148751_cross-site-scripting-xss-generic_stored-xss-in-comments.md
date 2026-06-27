---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148751'
original_report_id: '148751'
title: Stored XSS in comments
weakness: Cross-site Scripting (XSS) - Generic
team_handle: paragonie
created_at: '2016-07-01T20:48:22.410Z'
disclosed_at: '2016-07-01T22:18:55.990Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in comments

## Metadata

- HackerOne Report ID: 148751
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: paragonie
- Disclosed At: 2016-07-01T22:18:55.990Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Comments can contain an author's website. This website is used in the href attribute of link elements and isn't filtered. Thus it allows URLs like `javascript:alert(1)` to be used. These URLs must be filtered by protocol, e.g. only allow http and https.

These attacks are blocked by the default CSP, but clients not supporting CSP or changed CSPs may be affected.

This issue affects [Airship](https://github.com/paragonie/airship) Version 1.1.2 and lower.

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
