---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '151583'
original_report_id: '151583'
title: User enumeration in wp-admin
weakness: Improper Authentication - Generic
team_handle: iandunn-projects
created_at: '2016-07-15T19:45:32.488Z'
disclosed_at: '2016-07-16T09:21:08.425Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# User enumeration in wp-admin

## Metadata

- HackerOne Report ID: 151583
- Weakness: Improper Authentication - Generic
- Program: iandunn-projects
- Disclosed At: 2016-07-16T09:21:08.425Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi, I have found that in the page  wp-admin possible to perform user enumeration though differences in error massages:
if user exist the site will return :" ERROR: The password you entered for the username admin is incorrect."
if user not exit: Invalid username.

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
