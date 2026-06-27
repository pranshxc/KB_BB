---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1200992'
original_report_id: '1200992'
title: No admin audit log for auth tokens
team_handle: nextcloud
created_at: '2021-05-18T14:01:59.027Z'
disclosed_at: '2021-06-16T08:40:39.060Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# No admin audit log for auth tokens

## Metadata

- HackerOne Report ID: 1200992
- Weakness: 
- Program: nextcloud
- Disclosed At: 2021-06-16T08:40:39.060Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

There seems to be no audit trail for auth tokens.

* Creating tokens
* Revoking tokens
* Scope changes
* Renames
* Marking the token to be wiped

## Impact

As auth tokens are used to access your data having a track record when they are created helps a lot.
If you also take https://hackerone.com/reports/1193321 into account this would have been good information to track down what happened and by who.

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
