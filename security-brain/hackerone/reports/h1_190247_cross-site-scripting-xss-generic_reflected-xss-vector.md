---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '190247'
original_report_id: '190247'
title: Reflected XSS vector
weakness: Cross-site Scripting (XSS) - Generic
team_handle: gocd
created_at: '2016-12-11T00:39:09.185Z'
disclosed_at: '2017-02-22T17:41:20.978Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS vector

## Metadata

- HackerOne Report ID: 190247
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: gocd
- Disclosed At: 2017-02-22T17:41:20.978Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello GoCD team,

I noticed a reflected / stored XSS vulnerability vector that could potentially be used to impact security of GoCD users.

- https://www.go.cd/user/upoad/..%2F..%2F
- https://docs.go.cd/current/user/upoad/..%2F..%2F

As you should see, this link is considered as valid by the HTTP service and thus does not cause redirect to root of *.go.cd nor return of an HTTP error code (e.g., 404 not found) as it should be...

Such a link can be used to load an unexpected script located on the HTTP server of *.go.cd, eventually uploaded by user (see screenshot)

Please let me know if you need more information!

Looking forward!

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
