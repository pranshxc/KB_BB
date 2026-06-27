---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '923759'
original_report_id: '923759'
title: Edit Policy restriction does not prevent comments.
weakness: Improper Access Control - Generic
team_handle: phabricator
created_at: '2020-07-14T17:58:43.758Z'
disclosed_at: '2020-07-17T17:14:06.076Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- improper-access-control-generic
---

# Edit Policy restriction does not prevent comments.

## Metadata

- HackerOne Report ID: 923759
- Weakness: Improper Access Control - Generic
- Program: phabricator
- Disclosed At: 2020-07-17T17:14:06.076Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

- Change the edit policy of a Maniphest Task
- Attempt to comment on the the task with a user who doesn't have access

## Impact

Given a few users I spoke to believe restricting the edit policy blocks comments, This allows an underpriveleged user to gain access to carry out a restrcited action.

(Mongoose)

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
