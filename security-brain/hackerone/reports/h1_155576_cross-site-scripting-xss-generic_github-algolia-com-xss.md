---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '155576'
original_report_id: '155576'
title: '[github.algolia.com] XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: algolia
created_at: '2016-07-31T10:30:18.884Z'
disclosed_at: '2016-09-01T11:32:23.008Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [github.algolia.com] XSS

## Metadata

- HackerOne Report ID: 155576
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: algolia
- Disclosed At: 2016-09-01T11:32:23.008Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello , i found a Cross-Site-Scripting in your github subdomain.
All you have to do is to search in this input ( i attached input.PNG )

Search about ,,document domain'' 
Alert was executed , because you don't sanitize the query which comes from github 

Search about ,,svg onload'' -> github.algolia.com


Thanks.

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
