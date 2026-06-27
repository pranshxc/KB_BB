---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '94909'
original_report_id: '94909'
title: 'XSS risk reduction with X-XSS-Protection: 1; mode=block header'
team_handle: radancy
created_at: '2015-10-20T20:45:36.974Z'
disclosed_at: '2019-08-09T08:30:27.061Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
tags:
- hackerone
---

# XSS risk reduction with X-XSS-Protection: 1; mode=block header

## Metadata

- HackerOne Report ID: 94909
- Weakness: 
- Program: radancy
- Disclosed At: 2019-08-09T08:30:27.061Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

As you can read for example on this Microsoft blog (http://blogs.msdn.com/b/ieinternals/archive/2011/01/31/controlling-the-internet-explorer-xss-filter-with-the-x-xss-protection-http-header.aspx):

" ... X-XSS-Protection: 1; mode=block When this token is present, if a potential XSS Reflection attack is detected, Internet Explorer will prevent rendering of the page. ... "

Thus it is recommended to add X-XSS-Protection: 1; mode=block header to reduce XSS risk.

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
