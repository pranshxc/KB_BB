---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '229405'
original_report_id: '229405'
title: Csrf in watch-unwatch projects
weakness: Cross-Site Request Forgery (CSRF)
team_handle: weblate
created_at: '2017-05-17T20:13:14.805Z'
disclosed_at: '2017-08-17T16:18:23.597Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Csrf in watch-unwatch projects

## Metadata

- HackerOne Report ID: 229405
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: weblate
- Disclosed At: 2017-08-17T16:18:23.597Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

When you visit any projects from `https://hosted.weblate.org/` , there is a button provided on top-right called `Watch` / `Unwatch` for each projects. when you click on that button, a POST request is sent which contains csrf token.  But this request also works without that token.

Just hit the urls in your browser and you will be able to `Watch` or `Unwatch` the projects

`https://hosted.weblate.org/accounts/watch/androbd/`
https://hosted.weblate.org/accounts/unwatch/androbd/

where androbd is a project name!

Regrads
Ashish

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
