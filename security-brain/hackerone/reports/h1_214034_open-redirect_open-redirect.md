---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '214034'
original_report_id: '214034'
title: Open redirect
weakness: Open Redirect
team_handle: gitlab
created_at: '2017-03-16T22:56:04.278Z'
disclosed_at: '2017-04-06T08:06:22.582Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- open-redirect
---

# Open redirect

## Metadata

- HackerOne Report ID: 214034
- Weakness: Open Redirect
- Program: gitlab
- Disclosed At: 2017-04-06T08:06:22.582Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

POC:

$GITLAB_INSTANCE = gitlab.com

Visit: 

https://$GITLAB_INSTANCE/dashboard/todos?page=99999999&host=www.google.com

Bug is in Dashboard::TodosController line 10

Likey
Same bug in Projects::IssuesController line 32
and other places in the codebase where you `redirect_to params.merge(..)`

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
