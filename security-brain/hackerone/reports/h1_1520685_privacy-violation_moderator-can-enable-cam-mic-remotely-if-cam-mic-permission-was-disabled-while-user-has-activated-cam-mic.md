---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1520685'
original_report_id: '1520685'
title: Moderator can enable cam/mic remotely if  cam/mic-permission was disabled while
  user has activated cam/mic
weakness: Privacy Violation
team_handle: nextcloud
created_at: '2022-03-24T08:10:53.250Z'
disclosed_at: '2022-06-09T12:42:33.695Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: nextcloud/spreed
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# Moderator can enable cam/mic remotely if  cam/mic-permission was disabled while user has activated cam/mic

## Metadata

- HackerOne Report ID: 1520685
- Weakness: Privacy Violation
- Program: nextcloud
- Disclosed At: 2022-06-09T12:42:33.695Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
[add summary of the vulnerability]

## Steps To Reproduce:

  1. Create a Call as User A (Moderator)
  2. Add User B to the call
  3. Start the call as User A
  4. User B joins the call and enables the camera
  5. User A removes all permissions for User B, cam and mic are now disabled
  6. User A grants all permissions to User B

--> now mic and cam are enabled remotely, if User B didn't disable it before removing permissions by User B

## Used Software Versions:
Nextcloud 23.0.3
spreed-App 13.0.4
nextcloud-spreed-signaling 0.4.0

## Impact

A call moderator can remotely enable user webcams, if there were enabled before removing the permissions. This is a big privacy issue.

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
