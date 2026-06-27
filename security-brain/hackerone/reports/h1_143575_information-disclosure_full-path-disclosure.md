---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '143575'
original_report_id: '143575'
title: Full path disclosure
weakness: Information Disclosure
team_handle: phabricator
created_at: '2016-06-07T23:24:55.645Z'
disclosed_at: '2016-06-08T10:52:38.895Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# Full path disclosure

## Metadata

- HackerOne Report ID: 143575
- Weakness: Information Disclosure
- Program: phabricator
- Disclosed At: 2016-06-08T10:52:38.895Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Mongoose. The full path of the phabricator install is shown if you go to /login/mustverify/ while being logged out. This could be seen as a server configuration issue, but I think I followed your installation guide closely.

Since I already wrote it I include a little patch, please feel free to ignore it if it's not what you need.

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
