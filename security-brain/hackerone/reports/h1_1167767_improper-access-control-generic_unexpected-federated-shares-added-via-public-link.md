---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1167767'
original_report_id: '1167767'
title: Unexpected federated shares added via public link
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2021-04-18T13:00:13.625Z'
disclosed_at: '2021-04-26T15:55:55.138Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Unexpected federated shares added via public link

## Metadata

- HackerOne Report ID: 1167767
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2021-04-26T15:55:55.138Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

So I'm not 100% sure if this is an security issue or not. But it is in my opinion at least unexpected and could be handled better to make sure people trust the system.

1. Get a public link share (again plenty of those around)
2. Click the 'add to your Nextcloud'
3. A federated share is added/created

However now the owner of the public link at 1 has a new federated share added.
Without any idea where it comes from. Which would be reason for concern in my book. Esp for people that do not know about the functionality etc.

## Impact

Missing descriptions or notifications can limit the trust in the system. Esp for regular users without technical knowledge on how things work.
I'd expect a notification. Or at the very least a description in the sharing tab (? is that the correct name?) for the federated share 'mounted from public link X'

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
