---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150746'
original_report_id: '150746'
title: Reflected XSS in www.olx.ph
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-07-11T20:45:02.785Z'
disclosed_at: '2016-10-11T09:19:48.409Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS in www.olx.ph

## Metadata

- HackerOne Report ID: 150746
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-10-11T09:19:48.409Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Summary
===
The www.olx.ph domain is vulnerable to reflected XSS through the search function.

Proof of concept
===
The following URL contains a (harmless) XSS vector, which causes an alert box to appear
https://www.olx.ph/real-estate/ph-bul/?search[order]=filter_float_price%3A%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E

This test was performed using Mozilla Firefox 47.0.1. A print screen of this PoC XSS vector in action is attached to this report.

Recommended solution
===
All GET parameters should be properly escaped before being printed to the page.

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
