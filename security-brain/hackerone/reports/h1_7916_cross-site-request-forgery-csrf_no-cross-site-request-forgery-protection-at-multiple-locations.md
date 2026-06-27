---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7916'
original_report_id: '7916'
title: No Cross-Site Request Forgery protection at multiple locations
weakness: Cross-Site Request Forgery (CSRF)
team_handle: localize
created_at: '2014-04-17T20:12:51.600Z'
disclosed_at: '2014-04-18T08:35:52.718Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# No Cross-Site Request Forgery protection at multiple locations

## Metadata

- HackerOne Report ID: 7916
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: localize
- Disclosed At: 2014-04-18T08:35:52.718Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The Localize application does not provide protection against CSRF attacks at various locations. 
For example, the following actions/pages are vulnerable:

`POST /pages/create_project`
`POST /pages/settings`
`POST /add_phrase/$var/languages/$var`


See https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF) for more information.

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
