---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1437004'
original_report_id: '1437004'
title: Improper santization of edit in list feature at twitter leads to delete any
  twitter user's list cover photo.
weakness: Insecure Direct Object Reference (IDOR)
team_handle: x
created_at: '2021-12-28T03:31:20.544Z'
disclosed_at: '2023-09-18T19:38:53.356Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Improper santization of edit in list feature at twitter leads to delete any twitter user's list cover photo.

## Metadata

- HackerOne Report ID: 1437004
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: x
- Disclosed At: 2023-09-18T19:38:53.356Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary:
Improper santization of edit list feature at twitter leads to delete any twitter user's list cover photo.
from this bug attacker can delete any twitter users list's cover photo.

Description:
Improper santization of edit in list feature at twitter leads to delete any twitter user's list cover photo.
from this bug attacker can delete any twitter users list's cover photo.
as changing a media id in attackers  request makes two entity referring to single photo so when attacker deletes his cover photo automatically the media related to that gets deleted so victims cover photo also gets deleted

## Steps To Reproduce:

Step 1: gain media-id(for cover photo of list) of victim easily accessible by visiting list on victims profile.

Step 2: now from attackers account create a list and change cover photo, intercept the request and change the media id to victims cover photo id. 

Step 3 : after that delete list's cover photo from attackers account it will automatically delete victim list's cover photo .

## Impact:
Security Impact : attacker can delete any twitter users list's cover photo.

## Supporting Material/References:
POC Attached Below

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

Security Impact : attacker can delete any twitter users list's cover photo.

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
