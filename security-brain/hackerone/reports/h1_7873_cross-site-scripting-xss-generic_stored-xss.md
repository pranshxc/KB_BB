---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7873'
original_report_id: '7873'
title: Stored XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localize
created_at: '2014-04-17T18:29:21.520Z'
disclosed_at: '2014-04-20T02:53:31.284Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS

## Metadata

- HackerOne Report ID: 7873
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localize
- Disclosed At: 2014-04-20T02:53:31.284Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey!!

Steps to reproduce :

1) while making account add xss payload in username like : "><img src=a onerror=prompt(1);>
2) login using this .
3) Go to settings tab (http://www.localize.io/pages/settings)
4) XSS ll get executed .

Attached PoC .

Daksh

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
