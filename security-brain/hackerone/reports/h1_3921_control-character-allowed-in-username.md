---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '3921'
original_report_id: '3921'
title: Control character allowed in username
team_handle: phabricator
created_at: '2014-03-13T12:32:49.566Z'
disclosed_at: '2014-04-12T19:55:37.054Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
---

# Control character allowed in username

## Metadata

- HackerOne Report ID: 3921
- Weakness: 
- Program: phabricator
- Disclosed At: 2014-04-12T19:55:37.054Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It turns out, that it is possible to register a user with a special sign %0a (appended in proxy). Possible consequences:
1. You can't see the profile of this newly created user after registration (404 response)
2. You can use this to spoof another user - just use the name of another user during registration, append %0a in proxy (when registration request is sent) and you will be finally recognized as this user in Phabricator (the same name presented/displayed). This way you can try to spoof another user.

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
