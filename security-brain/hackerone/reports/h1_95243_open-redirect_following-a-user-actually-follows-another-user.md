---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '95243'
original_report_id: '95243'
title: Following a User Actually Follows Another User
weakness: Open Redirect
team_handle: x
created_at: '2015-10-22T23:07:36.649Z'
disclosed_at: '2015-12-02T17:40:51.446Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- open-redirect
---

# Following a User Actually Follows Another User

## Metadata

- HackerOne Report ID: 95243
- Weakness: Open Redirect
- Program: x
- Disclosed At: 2015-12-02T17:40:51.446Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I can display a web intent page to a victim that appears to prompt them to follow one user, but actually ends up following a completely different user when they click "follow". The following is a proof of concept:

https://twitter.com/intent/follow?screen_name=twitter&screen_name=ericrtest3&user_id=113483807

This is somewhat related to the last bug I submitted (see #95217), albeit the impact is more dramatic. This can be used by malicious users such as spammers and social engineers to trick a user into following them.

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
