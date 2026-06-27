---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '415238'
original_report_id: '415238'
title: '[Admin Panel] CSRF to resume/pause runner'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: gitlab
created_at: '2018-09-27T10:33:53.541Z'
disclosed_at: '2020-12-01T04:34:15.871Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 58
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# [Admin Panel] CSRF to resume/pause runner

## Metadata

- HackerOne Report ID: 415238
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: gitlab
- Disclosed At: 2020-12-01T04:34:15.871Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi, 

Just found a CSRF in admin panel of gitlab instance to pause/resume runner.

## Steps to reproduce
- http://{gitlab_instance}/admin/runners/:runner_id/resume
- http://{gitlab_instance}/admin/runners/:runner_id/pause

Video:
███████
password: `██████████`

## Impact

Just found a CSRF in admin panel of gitlab instance to pause/resume runner.

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
