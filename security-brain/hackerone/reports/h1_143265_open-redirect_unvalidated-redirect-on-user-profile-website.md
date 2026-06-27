---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '143265'
original_report_id: '143265'
title: Unvalidated redirect on user profile website
weakness: Open Redirect
team_handle: zomato
created_at: '2016-06-06T03:04:50.478Z'
disclosed_at: '2017-05-18T16:55:21.458Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- open-redirect
---

# Unvalidated redirect on user profile website

## Metadata

- HackerOne Report ID: 143265
- Weakness: Open Redirect
- Program: zomato
- Disclosed At: 2017-05-18T16:55:21.458Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The user profile redirect request is not properly validated. The presence of parameter t which is being passed through the request is verified but same value can be reused to any unauthenticated or authenticated user to redirect them to any web site.

Sample link is given below.

https://www.zomato.com/redirect?u=http%3A%2F%2Ftest.com&t=38dc43d5f007f4c5d974f6c74f065158&g=user-profile-website

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
