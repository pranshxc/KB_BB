---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '868590'
original_report_id: '868590'
title: IDOR on deleting drafts on https://apps.topcoder.com/wiki/users/viewmydrafts.action
  via discardDraftId parameter
weakness: Insecure Direct Object Reference (IDOR)
team_handle: topcoder
created_at: '2020-05-07T23:27:18.938Z'
disclosed_at: '2020-05-12T14:42:17.910Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
asset_identifier: apps.topcoder.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR on deleting drafts on https://apps.topcoder.com/wiki/users/viewmydrafts.action via discardDraftId parameter

## Metadata

- HackerOne Report ID: 868590
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: topcoder
- Disclosed At: 2020-05-12T14:42:17.910Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi :)

On https://apps.topcoder.com/wiki/users/viewmydrafts.action, you can see your drafts, edit or delete them. Users can delete their own drafts on `https://apps.topcoder.com/wiki/users/viewmydrafts.action?discardDraftId=<DRAFT_ID>`. 
But there is no check and an attacker can change `discardDraftId` and delete all drafts.

## Impact

An attacker can delete other user's drafts.

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
