---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '199286'
original_report_id: '199286'
title: Group admin can remove user from all his groups via API
team_handle: nextcloud
created_at: '2017-01-18T08:30:23.166Z'
disclosed_at: '2017-02-23T12:23:06.457Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
---

# Group admin can remove user from all his groups via API

## Metadata

- HackerOne Report ID: 199286
- Weakness: 
- Program: nextcloud
- Disclosed At: 2017-02-23T12:23:06.457Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

### Steps
1. As admin make user1 group admin for group1 and group2
2. As user1 create a new user user2
3. As user1 try to remove the user from both groups via the UI
4. Take the first `togglegroup.php` request and replay it with `group2` on curl

### Expected
Should not work

### Actual
The group-admin can escape his groups and create users that are not part of his groups.

Also possible via the provisioning_api.

Either the restriction should be enforced on the api endpoints (not only in the UI), or the restriction in the UI should be removed.

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
