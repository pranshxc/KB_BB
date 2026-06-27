---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '128853'
original_report_id: '128853'
title: Information disclosure at lite.uber.com
weakness: Information Disclosure
team_handle: uber
created_at: '2016-04-07T01:27:02.560Z'
disclosed_at: '2016-06-13T22:41:00.934Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Information disclosure at lite.uber.com

## Metadata

- HackerOne Report ID: 128853
- Weakness: Information Disclosure
- Program: uber
- Disclosed At: 2016-06-13T22:41:00.934Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello!
1. At https://lite.uber.com/auth/login I get 302-redirect to https://login.uber.com.
2. After post my email and password I get callback to https://lite.uber.com/auth/callback?code=efopqUAx2uwMOqJafHGj2OP8yNxXkf#_
3. At this page we can see trace stack with names of nodejs modules, full path disclose...

File attached.

Best Wishes!

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
