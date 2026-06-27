---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13939'
original_report_id: '13939'
title: information disclosure
weakness: Information Disclosure
team_handle: automattic
created_at: '2014-05-29T06:56:41.052Z'
disclosed_at: '2014-07-16T08:53:44.692Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# information disclosure

## Metadata

- HackerOne Report ID: 13939
- Weakness: Information Disclosure
- Program: automattic
- Disclosed At: 2014-07-16T08:53:44.692Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Use Google chrome  35.0.1916.114m for reproduction  
1. go to https://app.simplenote.com/
2. login into the app.
3. Now press logout, and press back button on browser. You will see the session back.This is the information disclosure vulnerability.

I recommend checking for a valid, authenticated session and if there isn't one redirect to the login page.

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
