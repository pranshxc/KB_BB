---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '106678'
original_report_id: '106678'
title: '[now.informatica.com] Reflective XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2015-12-23T21:36:50.432Z'
disclosed_at: '2016-12-09T10:10:18.321Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [now.informatica.com] Reflective XSS

## Metadata

- HackerOne Report ID: 106678
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2016-12-09T10:10:18.321Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

XSS vulnerability lies on `http://now.informatica.com/launch-next-bigdata-registration-inxpo.html?Source=homepage`

#POC

* Sign up for big data management Virtual launch event

* on parameter `company_name`  inject `'"><img src=x onerror=alert(1)>`

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
