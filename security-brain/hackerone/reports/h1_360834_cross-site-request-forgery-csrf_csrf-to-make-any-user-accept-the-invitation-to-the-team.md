---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '360834'
original_report_id: '360834'
title: CSRF to make any user accept the invitation to the team
weakness: Cross-Site Request Forgery (CSRF)
team_handle: liberapay
created_at: '2018-06-01T16:04:26.199Z'
disclosed_at: '2018-06-02T13:03:20.245Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF to make any user accept the invitation to the team

## Metadata

- HackerOne Report ID: 360834
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: liberapay
- Disclosed At: 2018-06-02T13:03:20.245Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

#Description:
The victim can be tricked into accepting the invite as a normal GET request is sent while accepting the request.

#Steps to reproduce
Make an html page using the following code:
```
<a href="https://liberapay.com/test/membership/accept">click here</a>
```
Change" test" with your team mate.

## Impact

The impact is low but still it can make a user to accept the request even if he wanted not to.

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
